'''

Key Differences

Feature	          Factory Pattern	                    Strategy Pattern

Type	        Creational Pattern	                Behavioral Pattern

Purpose	        Encapsulates object creation	    Encapsulates interchangeable behaviors

Main Role	    Creates instances of classes        Defines multiple algorithms and lets you choose at runtime
                based on input

Flexibility	    Decides which class to              Decides which behavior to apply
                instantiate

Use Cases	    Creating objects like               Selecting payment methods, sorting algorithms, etc.
                ShapeFactory, CarFactory, etc

'''

from abc import ABC

class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass

class Truck(Transport):
    def deliver(self):
        print("Delivering by truck")

class Ship(Transport):
    def deliver(self):
        print("Delivering by ship")

class Logistics(ABC):
    @abstractmethod
    def create_transport(self):
        pass

class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()

class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()


if __name__ == "__main__":
    Logistics = RoadLogistics()
    transport = Logistics.create_transport()
    transport.deliver()  # Output: Delivering by truck
