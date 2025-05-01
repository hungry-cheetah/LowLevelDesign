# Clients should not be forced to depend on methods that they do not use.


from abc import ABC, abstractmethod

# Violates ISP: A single interface forces all functionalities on classes
class Printer(ABC):
    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def scan(self):
        pass

    @abstractmethod
    def fax(self):
        pass

# BasicPrinter doesn't support scanning or faxing but is forced to implement them
class BasicPrinter(Printer):
    def print(self):
        print("Printing...")

    def scan(self):
        raise NotImplementedError("Scan not supported")

    def fax(self):
        raise NotImplementedError("Fax not supported")

# MultiFunctionPrinter supports all features
class MultiFunctionPrinter(Printer):
    def print(self):
        print("Printing...")

    def scan(self):
        print("Scanning...")

    def fax(self):
        print("Faxing...")

# Usage
if __name__ == "__main__":
    printer = BasicPrinter()
    printer.print()
    try:
        printer.scan()  # Will raise NotImplementedError
    except NotImplementedError as e:
        print(e)
