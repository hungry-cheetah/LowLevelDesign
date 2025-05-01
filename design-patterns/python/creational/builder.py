# Why Use the Builder Pattern?
# Encapsulates construction logic: Separates complex object creation logic.
# Method chaining for flexibility: Easy to modify or extend object creation.
# Reduces constructor overload: No need for multiple constructors with varying parameters.
# This pattern is useful when creating objects with many optional parameters or configurations.


class Pizza:
    """Represents the final Pizza object."""
    def __init__(self):
        self.size = None
        self.crust = None
        self.sauce = None
        self.toppings = []

    def __str__(self):
        return f"Pizza: {self.size} size, {self.crust} crust, {self.sauce} sauce, Toppings: {', '.join(self.toppings) if self.toppings else 'None'}"

class PizzaBuilder:
    """Builder class to construct Pizza step by step."""
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self

    def set_crust(self, crust_type):
        self.pizza.crust = crust_type
        return self

    def set_sauce(self, sauce_type):
        self.pizza.sauce = sauce_type
        return self

    def add_topping(self, topping):
        self.pizza.toppings.append(topping)
        return self

    def build(self):
        return self.pizza

class PizzaDirector:
    """Predefined pizza recipes using the Builder."""
    @staticmethod
    def build_margherita():
        return PizzaBuilder()\
            .set_size("Medium")\
            .set_crust("Thin")\
            .set_sauce("Tomato")\
            .add_topping("Mozzarella Cheese")\
            .add_topping("Basil")\
            .build()

    @staticmethod
    def build_pepperoni():
        return PizzaBuilder()\
            .set_size("Large")\
            .set_crust("Stuffed")\
            .set_sauce("Barbecue")\
            .add_topping("Pepperoni")\
            .add_topping("Olives")\
            .add_topping("Cheese")\
            .build()

if __name__ == "__main__":
    # Ordering predefined pizzas
    pizza1 = PizzaDirector.build_margherita()
    print(pizza1)

    pizza2 = PizzaDirector.build_pepperoni()
    print(pizza2)

    # Creating a custom pizza using the builder
    custom_pizza = PizzaBuilder()\
        .set_size("Small")\
        .set_crust("Pan")\
        .set_sauce("Pesto")\
        .add_topping("Mushrooms")\
        .add_topping("Feta Cheese")\
        .add_topping("Spinach")\
        .build()

    print(custom_pizza)
