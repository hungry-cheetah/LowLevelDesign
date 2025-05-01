from abc import ABC, abstractmethod

# Abstraction (Interface)
class MessageService(ABC):
    @abstractmethod
    def send(self, message):
        pass

# Concrete implementation 1
class EmailService(MessageService):
    def send(self, message):
        print(f"Sending email: {message}")

# Concrete implementation 2
class SMSService(MessageService):
    def send(self, message):
        print(f"Sending SMS: {message}")

# High-level module depends on abstraction, not concrete classes
class Notification:
    def __init__(self, service: MessageService):
        self.service = service  # Dependency Injection

    def notify(self, message):
        self.service.send(message)

# Usage
if __name__ == "__main__":
    email_notification = Notification(EmailService())
    email_notification.notify("Hello via Email!")

    sms_notification = Notification(SMSService())
    sms_notification.notify("Hello via SMS!")


# Notification does not depend on concrete classes (Email/SMS).
# Notification only depends on MessageService (an abstraction).
# Easier to add new services (e.g., PushNotificationService) without modifying existing code.
