from abc import ABC, abstractmethod


# Step 1: Define Abstract Product Interfaces
class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        pass

class Sofa(ABC):
    @abstractmethod
    def lie_on(self):
        pass

class CoffeeTable(ABC):
    @abstractmethod
    def place_items(self):
        pass

# Step 2: Create Concrete Products for Modern Style
class ModernChair(Chair):
    def sit_on(self):
        return "Sitting on a Modern Chair"

class ModernSofa(Sofa):
    def lie_on(self):
        return "Lying on a Modern Sofa"

class ModernCoffeeTable(CoffeeTable):
    def place_items(self):
        return "Placing items on a Modern Coffee Table"

# Step 3: Create Concrete Products for Victorian Style
class VictorianChair(Chair):
    def sit_on(self):
        return "Sitting on a Victorian Chair"

class VictorianSofa(Sofa):
    def lie_on(self):
        return "Lying on a Victorian Sofa"

class VictorianCoffeeTable(CoffeeTable):
    def place_items(self):
        return "Placing items on a Victorian Coffee Table"

# Step 4: Create Concrete Products for ArtDeco Style
class ArtDecoChair(Chair):
    def sit_on(self):
        return "Sitting on an ArtDeco Chair"

class ArtDecoSofa(Sofa):
    def lie_on(self):
        return "Lying on an ArtDeco Sofa"

class ArtDecoCoffeeTable(CoffeeTable):
    def place_items(self):
        return "Placing items on an ArtDeco Coffee Table"

# Step 5: Define Abstract Factory Interface
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass

    @abstractmethod
    def create_coffee_table(self) -> CoffeeTable:
        pass

# Step 6: Implement Concrete Factories for Each Style
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()

    def create_sofa(self) -> Sofa:
        return ModernSofa()

    def create_coffee_table(self) -> CoffeeTable:
        return ModernCoffeeTable()

class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_sofa(self) -> Sofa:
        return VictorianSofa()

    def create_coffee_table(self) -> CoffeeTable:
        return VictorianCoffeeTable()

class ArtDecoFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ArtDecoChair()

    def create_sofa(self) -> Sofa:
        return ArtDecoSofa()

    def create_coffee_table(self) -> CoffeeTable:
        return ArtDecoCoffeeTable()

# Step 7: Client Code
def client_code(factory: FurnitureFactory):
    chair = factory.create_chair()
    sofa = factory.create_sofa()
    table = factory.create_coffee_table()

    print(chair.sit_on())
    print(sofa.lie_on())
    print(table.place_items())

# Step 8: Using the Factories
print("Modern Furniture Set:")
client_code(ModernFurnitureFactory())

print("\nVictorian Furniture Set:")
client_code(VictorianFurnitureFactory())

print("\nArtDeco Furniture Set:")
client_code(ArtDecoFurnitureFactory())


