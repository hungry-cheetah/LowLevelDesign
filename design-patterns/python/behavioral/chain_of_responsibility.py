# 🔹 Chain of Responsibility Design Pattern - Python Example
# The Chain of Responsibility Pattern allows multiple handlers to process a request sequentially,
#  where each handler decides:
    # To process the request or
    # To pass it to the next handler
    # 🔹 Use Case: Logging System (INFO → DEBUG → ERROR) 📝
    # Imagine a logging system where logs can have different severity levels (INFO, DEBUG, ERROR).

# INFO logs → Processed by InfoLogger.
# DEBUG logs → Processed by DebugLogger.
# ERROR logs → Processed by ErrorLogger.
# If one logger can’t handle it, it passes it to the next logger in the chain.



from abc import ABC, abstractmethod

# Abstract Logger
class Logger(ABC):
    """Abstract Logger class with a reference to the next logger in the chain"""

    def __init__(self, next_logger=None):
        self.next_logger = next_logger

    @abstractmethod
    def log(self, level, message):
        """Abstract log method to be implemented by subclasses"""
        pass

# Concrete Loggers
class InfoLogger(Logger):
    """Handles INFO level logs, passes others to the next logger"""

    def log(self, level, message):
        if level == "INFO":
            print(f"[INFO] {message}")
        elif self.next_logger:
            self.next_logger.log(level, message)  # Pass to the next logger

class DebugLogger(Logger):
    """Handles DEBUG level logs, passes others to the next logger"""

    def log(self, level, message):
        if level == "DEBUG":
            print(f"[DEBUG] {message}")
        elif self.next_logger:
            self.next_logger.log(level, message)  # Pass to the next logger

class ErrorLogger(Logger):
    """Handles ERROR level logs, passes others to the next logger"""

    def log(self, level, message):
        if level == "ERROR":
            print(f"[ERROR] {message}")
        elif self.next_logger:
            self.next_logger.log(level, message)  # Pass to the next logger

# Client Code
if __name__ == "__main__":
    # Create the chain: INFO → DEBUG → ERROR
    error_logger = ErrorLogger()
    debug_logger = DebugLogger(error_logger)
    info_logger = InfoLogger(debug_logger)

    # Test logging
    info_logger.log("INFO", "System started")  # Handled by InfoLogger
    info_logger.log("DEBUG", "Debugging mode activated")  # Handled by DebugLogger
    info_logger.log("ERROR", "System crash detected")  # Handled by ErrorLogger
    info_logger.log("WARNING", "Disk space low")  # Not handled



