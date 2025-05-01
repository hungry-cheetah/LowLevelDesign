# The State Design Pattern allows an object to change its behavior when its internal state changes,
# without modifying the object's class. It promotes encapsulation by representing each state as a
# separate class.


# ✅ Encapsulation → Each state is a separate class with its own behavior.
# ✅ Flexible Transitions → Adding/removing states doesn’t require modifying the main class (TrafficLight).
# ✅ Real-World Example → Similar to a Vending Machine where states control actions based on the inserted coin.
# ✅ Loose Coupling → TrafficLight doesn’t need to check conditions explicitly; it delegates to state classes.

# 📌 Real-World Use Cases
# ATM Machine (Idle → Card Inserted → PIN Entered → Transaction Completed)
# Document Workflow (Draft → Review → Approved → Published)
# Elevator System (Idle → Moving Up → Moving Down → Stopped)


from abc import ABC, abstractmethod
import time

# State Interface
class TrafficLightState(ABC):
    """Abstract State class defining the state behavior"""

    @abstractmethod
    def change(self, traffic_light):
        pass

    @abstractmethod
    def display(self):
        pass

# Concrete State: Red Light
class RedLight(TrafficLightState):
    def change(self, traffic_light):
        print("🔴 Red Light -> 🟡 Changing to Green Light...")
        traffic_light.set_state(GreenLight())

    def display(self):
        print("🚦 Red Light - STOP!")

# Concrete State: Yellow Light
class YellowLight(TrafficLightState):
    def change(self, traffic_light):
        print("🟡 Yellow Light -> 🟢 Changing to Red Light...")
        traffic_light.set_state(RedLight())

    def display(self):
        print("🚦 Yellow Light - GET READY!")

# Concrete State: Green Light
class GreenLight(TrafficLightState):
    def change(self, traffic_light):
        print("🟢 Green Light -> 🔴 Changing to Yellow Light...")
        traffic_light.set_state(YellowLight())

    def display(self):
        print("🚦 Green Light - GO!")

# Context: Traffic Light
class TrafficLight:
    """Context that maintains a reference to the current state"""

    def __init__(self):
        self._state = RedLight()  # Default state

    def set_state(self, state):
        """Change the state"""
        self._state = state

    def change(self):
        """Trigger state transition"""
        self._state.change(self)

    def display(self):
        """Show current state"""
        self._state.display()


# Client Code
if __name__ == "__main__":
    traffic_light = TrafficLight()

    for _ in range(6):  # Simulating multiple state changes
        traffic_light.display()
        time.sleep(1)
        traffic_light.change()
        print("-" * 30)
