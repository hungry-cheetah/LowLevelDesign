# High-level modules should not depend on low-level modules; both should depend on abstractions.


class EmailService:
    def send_email(self, message):
        print(f"Sending email: {message}")

# High-level module directly depends on low-level module (violates DIP)
class Notification:
    def __init__(self):
        self.email_service = EmailService()  # Direct dependency

    def notify(self, message):
        self.email_service.send_email(message)

# Usage
if __name__ == "__main__":
    notification = Notification()
    notification.notify("Hello, DIP is important!")

# Here, EmailService is directly used by Notification without an abstraction.
# If we need to switch from email to SMS, we must modify the Notification class, which violates DIP.

# Notification depends directly on EmailService (a concrete class).
# If we introduce SMSService, we must modify Notification, breaking OCP too.

