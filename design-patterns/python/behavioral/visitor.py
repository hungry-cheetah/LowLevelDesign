# The Visitor Pattern allows adding new operations to a group of related objects without modifying
# their structure. Instead of modifying existing classes, we create a visitor class that encapsulates 
# the new behavior.

# 📌 Why Use Visitor Pattern?
# ✅ Open/Closed Principle → New operations can be added without modifying existing classes.
# ✅ Separation of Concerns → Business logic is separated from the object structure.
# ✅ Double Dispatch Mechanism → Ensures the correct method is called based on both the visitor type and the element type.


from abc import ABC, abstractmethod

# Step 1: Define the Element Interface (Product)
class Product(ABC):
    """Abstract class for products"""

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def accept(self, visitor):
        pass

# Step 2: Concrete Element Classes (Products)
class Electronics(Product):
    """Represents an electronic product"""

    def accept(self, visitor):
        return visitor.visit_electronics(self)

class Clothing(Product):
    """Represents a clothing product"""

    def accept(self, visitor):
        return visitor.visit_clothing(self)

class Food(Product):
    """Represents a food product"""

    def accept(self, visitor):
        return visitor.visit_food(self)

# Step 3: Define the Visitor Interface
class TaxVisitor(ABC):
    """Abstract visitor for calculating tax"""

    @abstractmethod
    def visit_electronics(self, item):
        pass

    @abstractmethod
    def visit_clothing(self, item):
        pass

    @abstractmethod
    def visit_food(self, item):
        pass

# Step 4: Concrete Visitor - Tax Calculator for USA
class USATaxCalculator(TaxVisitor):
    """Applies different tax rates for products in the USA"""

    def visit_electronics(self, item):
        tax = item.price * 0.15  # 15% tax
        final_price = item.price + tax
        print(f"📱 Electronics: {item.name} | Price: ${item.price} | Tax: ${tax:.2f} | Final: ${final_price:.2f}")
        return final_price

    def visit_clothing(self, item):
        tax = item.price * 0.10  # 10% tax
        final_price = item.price + tax
        print(f"👕 Clothing: {item.name} | Price: ${item.price} | Tax: ${tax:.2f} | Final: ${final_price:.2f}")
        return final_price

    def visit_food(self, item):
        tax = item.price * 0.05  # 5% tax
        final_price = item.price + tax
        print(f"🍎 Food: {item.name} | Price: ${item.price} | Tax: ${tax:.2f} | Final: ${final_price:.2f}")
        return final_price

# Step 5: Concrete Visitor - Tax Calculator for India
class IndiaTaxCalculator(TaxVisitor):
    """Applies different tax rates for products in India"""

    def visit_electronics(self, item):
        tax = item.price * 0.18  # 18% GST
        final_price = item.price + tax
        print(f"📱 Electronics: {item.name} | Price: ₹{item.price} | GST: ₹{tax:.2f} | Final: ₹{final_price:.2f}")
        return final_price

    def visit_clothing(self, item):
        tax = item.price * 0.12  # 12% GST
        final_price = item.price + tax
        print(f"👕 Clothing: {item.name} | Price: ₹{item.price} | GST: ₹{tax:.2f} | Final: ₹{final_price:.2f}")
        return final_price

    def visit_food(self, item):
        tax = item.price * 0.05  # 5% GST
        final_price = item.price + tax
        print(f"🍎 Food: {item.name} | Price: ₹{item.price} | GST: ₹{tax:.2f} | Final: ₹{final_price:.2f}")
        return final_price

# Step 6: Client Code - Shopping Cart
if __name__ == "__main__":
    cart = [
        Electronics("Smartphone", 1000),
        Clothing("Jeans", 50),
        Food("Apple", 10),
        Electronics("Laptop", 1500),
        Clothing("T-shirt", 25),
        Food("Milk", 5)
    ]

    print("\n💰 Applying USA Tax Rates:")
    usa_tax_calculator = USATaxCalculator()
    total_price_usa = sum(item.accept(usa_tax_calculator) for item in cart)
    print(f"\n💵 Total Price in USA (with Tax): ${total_price_usa:.2f}")

    print("\n💰 Applying India Tax Rates:")
    india_tax_calculator = IndiaTaxCalculator()
    total_price_india = sum(item.accept(india_tax_calculator) for item in cart)
    print(f"\n💵 Total Price in India (with Tax): ₹{total_price_india:.2f}")
