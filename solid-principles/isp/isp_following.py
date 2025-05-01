from abc import ABC, abstractmethod

# Following ISP: Separate interfaces for each functionality
class Printable(ABC):
    @abstractmethod
    def print(self):
        pass

class Scannable(ABC):
    @abstractmethod
    def scan(self):
        pass

class Faxable(ABC):
    @abstractmethod
    def fax(self):
        pass

# BasicPrinter only prints, no need to implement unused methods
class BasicPrinter(Printable):
    def print(self):
        print("Printing...")

# MultiFunctionPrinter supports all features by implementing multiple interfaces
class MultiFunctionPrinter(Printable, Scannable, Faxable):
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

    mfp = MultiFunctionPrinter()
    mfp.print()
    mfp.scan()
    mfp.fax()
