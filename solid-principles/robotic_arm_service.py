import json
import uvicorn

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from os.path import exists, join, realpath


from routers.calibration.gripper.src.gripper import gripper_calibration_router
from routers.calibration.camera.src.camera import camera_calibration_router
from routers.cluster_ops.src.gripper import gripper_ops_router
from routers.device.gripper.src.gripper import gripper_device_router
from routers.sanity.gripper.src.gripper import gripper_sanity_router
from routers.device.robotic_arm.src.robotic_arm import robotic_arm_device_router
from routers.layout_installation.layout_installation import layout_installation_router
from routers.cluster_ops.src.scanner import slide_fetch_handler
from routers.cluster_ops.src.drop_basket import slide_drop_handler
from routers.cluster_ops.src.reject_basket import reject_basket_ops as reject_basket_ops_router
from routers.cluster_ops.src.sakura_basket import sakura_basket_ops
from routers.misc.blend_generation import blend_generation_router
from routers.misc.auto_support import auto_support_router
from routers.device.camera.src.camera import camera_device_router


robotic_arm_service_app = FastAPI()
ra_ops = Operations()
err_handler_obj = ErrorHandler()

file_path = realpath(__file__)


@robotic_arm_service_app.on_event("startup")
def service_startup():
    ServiceLogger.get().initialize("robotic_arm_service")

    try:
        PasswordManager().save_secret_ids_in_memory()

        RobotRemote.clear_known_hosts()

        config.CLUSTER_NAME = ClusterConfigurationUtilities().get_cluster_name()
        ServiceLogger.get().log_info(f"Cluster Name: {config.CLUSTER_NAME}")

        DeviceInterface.get().connect()
        ServiceLogger.get().log_info("Connected to all devices")
        TeachPendantInterface().is_in_remote_control()

        DeviceInterface.get().robot_startup_sequence()
        Operations().initiate_play_sequence()
        version = Gripper().get_firmware_version()
        FirmwareVersionDBHandler().insert_document_in_db(version)
    except Exception as err_msg:
        err_msg = "failed to connect to devices: {}".format(err_msg)
        ServiceLogger.get().log_error(err_msg)


@robotic_arm_service_app.post("/robotic-arm/move/relative")
async def move_relative(request: Request):

    api_name = request.url.path

    try:
        request_body = await request.body()

        required_key_list = ['axis', 'direction']
        input_dictionary = PayloadHandler.validator(request_body, required_key_list)

        axis = input_dictionary["axis"]
        direction = int(input_dictionary["direction"])

        delta_value = 5
        move_type = 1

        if "value" in input_dictionary:
            delta_value = float(input_dictionary["value"])

        if "type" in input_dictionary:
            move_type = int(input_dictionary["type"])

        if axis == "pz" or axis == "py" or axis == "px":
            delta_value = delta_value / 1000

        acceleration = Constants.ROBOT_ACCELERATION
        velocity = Constants.ROBOT_VELOCITY
        blend = Constants.ROBOT_BENDING_RADIUS
        time_value = 2
        force_tag = 0
        force_value = 25

        RoboticArmGeneralOps().move_relative(
            RelativeMovementInfo(axis=axis, delta_value=delta_value, direction=direction),
            acceleration, velocity, time_value,
            blend, force_tag, force_value,
            move_type=move_type,
            unlock_protective_stop=True
        )

        pos = DeviceInterface.get().get_robotic_arm_position()

        resp_json = {
                "status": True,
                "px": pos.px*1000.0,
                "py": pos.py*1000.0,
                "pz": pos.pz*1000.0,
                "rx": pos.rx,
                "ry": pos.ry,
                "rz": pos.rz
            }

        resp_json = err_handler_obj.get().\
            modify_json(resp_json, api_name)

    except Exception as err_info:
        resp_json = err_handler_obj.get().\
                classify_error_codes(err_info, api_name)

    return resp_json



async def process_response_payload(request: Request, call_next):
    endpoint = request.url.path
    ServiceLogger.get().log_info(f"API Endpoint: {endpoint}")

    method = request.method
    ServiceLogger.get().log_info(f"API Method: {method}")

    port_number = request.url.port
    ServiceLogger.get().log_info(f"Port Number: {port_number}")

    ServiceLogger.get().log_info(f"API Request Time: {Timer.get_curr_time()}")

    rtde_interface = RTDEInterface.get()

    try:
        # Clone the request body
        request_body_bytes = await request.body()

        if request_body_bytes:
            request_body_str = request_body_bytes.decode('utf-8')
            request_body = json.loads(request_body_str)
            ServiceLogger.get().log_info(f"Request Payload: {request_body}")
        else:
            request_body = {}

        # Recreate request object with the original body (restoring the stream)
        async def receive():
            return {"type": "http.request", "body": request_body_bytes}

        request = Request(request.scope, receive=receive)

        # endpoints where apis are executing in background tasks
        background_tasks_apis_list = [
            "/robotic-arm/pick/basket",
            "/robotic-arm/drop-basket/sanity-check",
            "/robotic-arm/vertical-basket/sanity-check",
            "/robotic-arm/scanner-trajectory/updation"
        ]

        # Trigger rtde_interface operations
        if endpoint not in background_tasks_apis_list:
            rtde_interface.initiate_filename(endpoint, request_body)
            rtde_interface.reset_state(True)
            # rtde_interface.log_triggered_state(True)

            if method !="GET":
                RobotStatusManager().set_status(endpoint,"in-progress", request_body)

        start_time = Timer.get_curr_time()

        # Get the response from the next handler
        response = await call_next(request)

    except Exception as e:
        error_data = {
            "status": False,
            "err_msg": str(e)
        }
        ServiceLogger.get().log_info(f"Response: {error_data}")

        if endpoint not in background_tasks_apis_list:
            rtde_interface.log_state(True, True)
            if method != "GET":
                RobotStatusManager().set_status(endpoint,"error",request_body)

        return JSONResponse(content=error_data, status_code=500)

    if endpoint in background_tasks_apis_list:
        return response

    # Capture response body
    try:
        response_body = [chunk async for chunk in response.body_iterator]
        if response_body:
            modified_response_body = json.loads(response_body[0].decode())
        else:
            modified_response_body = {}

        # Process the response using APIResponseHandler
        modified_response_body = APIResponseHandler(modified_response_body).process_api_response(start_time)

        rtde_interface.log_state(True, not modified_response_body.get("status", False))

        if method !="GET":
                api_response = modified_response_body.get("status", False)

                if api_response is True:
                    RobotStatusManager().set_status(endpoint,"completed",request_body)
                else:
                    RobotStatusManager().set_status(endpoint,"error",request_body)

        # Create a new JSONResponse with the modified body
        modified_response = JSONResponse(
            content=modified_response_body,
            status_code=response.status_code,
            headers=dict(response.headers),
        )
        # Adjust Content-Length header for the new response
        modified_response.headers["Content-Length"] = str(len(modified_response.body))

        ServiceLogger.get().log_info(f"API Response Time: {Timer.get_curr_time()}")

        return modified_response

    except Exception as e:
        ServiceLogger.get().log_info(f"Error processing response: {str(e)}")
        rtde_interface.log_state(True, True)
        if method !="GET":
            RobotStatusManager().set_status(endpoint,"error",request_body)

        return JSONResponse(content={"error": str(e)}, status_code=500)

# Include MiddleWare Functions
robotic_arm_service_app.middleware("http")(process_response_payload)


# Include All Routers
robotic_arm_service_app.include_router(gripper_calibration_router)
robotic_arm_service_app.include_router(gripper_ops_router)
robotic_arm_service_app.include_router(gripper_device_router)
robotic_arm_service_app.include_router(gripper_sanity_router)
robotic_arm_service_app.include_router(robotic_arm_device_router)
robotic_arm_service_app.include_router(layout_installation_router)
robotic_arm_service_app.include_router(slide_fetch_handler)
robotic_arm_service_app.include_router(slide_drop_handler)
robotic_arm_service_app.include_router(reject_basket_ops_router)
robotic_arm_service_app.include_router(sakura_basket_ops)
robotic_arm_service_app.include_router(blend_generation_router)
robotic_arm_service_app.include_router(auto_support_router)
robotic_arm_service_app.include_router(camera_device_router)
robotic_arm_service_app.include_router(camera_calibration_router)

if __name__ == "__main__":  # pragma : no cover

    # REQUIRED FOR HTTPS.
    CRT_PATH = config.SystemInfo.SSL_CERT_PATH.value
    KEY_PATH = config.SystemInfo.SSL_KEY_PATH.value
    DNS = config.CLUSTER_DNS

    # start the service.
    uvicorn.run(robotic_arm_service_app,
                host=DNS,
                port=config.RAS_PORT,
                ssl_certfile=CRT_PATH,
                ssl_keyfile=KEY_PATH)