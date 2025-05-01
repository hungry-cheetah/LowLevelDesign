'''
Why Use the Adapter Pattern?
Decouples the system from specific implementations.
Allows seamless integration of third-party or legacy components.
Helps avoid modifying existing code (which could introduce bugs).

The Adapter Design Pattern is a structural pattern that allows objects with incompatible interfaces to work together.
It's often used to make existing classes work with others without modifying their source code.

Real-life Analogy
Imagine a laptop with a USB-C port, but your mouse uses a USB-A connector.
 You use a USB-A to USB-C adapter so they can connect. The Adapter Pattern does something similar in code'
'''


# Legacy code (incompatible interface)
class OldPaymentGateway:
    def make_payment(self, amount):
        print(f"Processing payment of ${amount} through OldPaymentGateway.")

# Modern interface expected by your application
class NewPaymentProcessor:
    def pay(self, amount):
        pass

# Adapter class
class PaymentAdapter(NewPaymentProcessor):
    def __init__(self, old_gateway):
        self.old_gateway = old_gateway

    def pay(self, amount):
        # Translate the expected method to the legacy method
        self.old_gateway.make_payment(amount)

# Client code
def process_payment(processor: NewPaymentProcessor, amount: int):
    processor.pay(amount)

# Usage
legacy_gateway = OldPaymentGateway()
adapter = PaymentAdapter(legacy_gateway)

process_payment(adapter, 100)

