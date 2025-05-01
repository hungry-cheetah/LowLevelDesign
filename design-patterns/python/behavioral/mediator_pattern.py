# The Mediator Design Pattern is used to reduce the dependencies between multiple communicating
#  objects by introducing a mediator that centralizes the communication.

# ✅ Decoupling Communication → Users don’t communicate directly; instead, they use the ChatRoom (Mediator).
# ✅ Scalability → New users can be added without modifying existing users.
# ✅ Centralized Communication → The ChatRoom handles message distribution, reducing dependencies.


from abc import ABC, abstractmethod

# Mediator Interface
class ChatMediator(ABC):
    """Abstract Mediator for Chat System"""

    @abstractmethod
    def send_message(self, message, sender):
        pass

    @abstractmethod
    def add_user(self, user):
        pass


# Concrete Mediator
class ChatRoom(ChatMediator):
    """Concrete Mediator that handles communication"""

    def __init__(self):
        self.users = []

    def add_user(self, user):
        """Register a new user"""
        self.users.append(user)

    def send_message(self, message, sender):
        """Send a message to all users except the sender"""
        for user in self.users:
            if user != sender:
                user.receive_message(message, sender)


# Colleague (User) Class
class User:
    """User participating in the chat"""

    def __init__(self, name, chat_mediator):
        self.name = name
        self.chat_mediator = chat_mediator
        chat_mediator.add_user(self)

    def send_message(self, message):
        """User sends a message"""
        print(f"📤 {self.name} sends: {message}")
        self.chat_mediator.send_message(message, self)

    def receive_message(self, message, sender):
        """User receives a message"""
        print(f"📩 {self.name} received from {sender.name}: {message}")

# Client Code
if __name__ == "__main__":
    chat_room = ChatRoom()  # Create Mediator

    # Create Users
    user1 = User("Alice", chat_room)
    user2 = User("Bob", chat_room)
    user3 = User("Charlie", chat_room)

    # Users send messages
    user1.send_message("Hello, everyone! 👋")
    user2.send_message("Hey Alice! How are you? 😊")
    user3.send_message("Good morning all! ☀️")
