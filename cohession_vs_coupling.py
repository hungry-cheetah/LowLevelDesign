'''
Cohesion vs Coupling in Software

🔗 Coupling
Definition: Coupling refers to how much one module (or class/function) depends on another.
- High Coupling: Modules are highly dependent on each other. A change in one module is likely to 
break or require changes in others.
- Low Coupling: Modules are mostly independent. They communicate via well-defined interfaces.

Goal: LOW coupling
Why? Because it leads to more modular, maintainable, and testable code.

Example:
If a PaymentProcessor class directly creates and uses a CreditCard class, changing how credit cards are processed affects PaymentProcessor. 
That’s high coupling. Instead, if PaymentProcessor uses a PaymentMethod interface, you can swap out different payment types easily — that’s low coupling.

🧩 Cohesion
Definition: Cohesion refers to how closely related and focused the responsibilities of a single module are.
- High Cohesion: A module does one thing and does it well. All its functions are related to its purpose.
- Low Cohesion: A module does many unrelated things, leading to messy, hard-to-understand code.

Goal: HIGH cohesion
Why? Because it improves clarity, reusability, and maintainability.

Example:
A UserManager class that handles user login, file uploads, and payment processing has low cohesion.
A UserAuthenticator class that handles only login/logout is highly cohesive.

📊 Summary Table

| Concept   | Good Practice     | Meaning                        | Benefit                         |
|-----------|-------------------|--------------------------------|----------------------------------|
| Coupling  | Low Coupling      | Modules are independent        | Easier to change/test/maintain  |
| Cohesion  | High Cohesion     | Each module has one purpose    | Clearer code, better reuse      |
"""
'''
