import logging
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Abstract Component
class BaseClass(ABC):
    """Abstract base class."""

    @abstractmethod
    def operation(self):
        pass

# Concrete Component: A real class without logging
class ConcreteClass(BaseClass):
    """A simple class that performs an operation."""

    def operation(self):
        return "Performing the main operation..."

# Abstract Decorator (inherits from BaseClass)
class ClassDecorator(BaseClass):
    """Base class for all decorators."""
    
    def __init__(self, base_class: BaseClass):
        self._base_class = base_class  # Store the wrapped object

    def operation(self):
        return self._base_class.operation()  # Default behavior

# Concrete Decorator: Adds logging functionality
class LoggingClassDecorator(ClassDecorator):
    """Decorator that adds logging behavior to any class."""

    def operation(self):
        logging.info("Executing operation...")
        result = self._base_class.operation()
        logging.info(f"Operation executed with result: {result}")
        return result

# Main execution
if __name__ == "__main__":
    # Create the base class instance
    obj = ConcreteClass()
    print(obj.operation())  # No logging, just execution

    print("\nApplying Logging Decorator...\n")

    # Wrap the class instance with logging decorator
    logged_obj = LoggingClassDecorator(obj)
    print(logged_obj.operation())  # Logs and executes


