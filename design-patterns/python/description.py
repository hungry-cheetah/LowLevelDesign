# controller layer -> API
# service layer
# data layer -> DB
# entity layer


# Design Patterns are standard solutions to common software design problems. They are categorized into three main types:


##############################################################################################################################
# Creational Design Patterns(Object Creation Mechanisms)
##############################################################################################################################

''''
1. Creational Design Patterns(Object Creation Mechanisms)
These patterns deal with object creation mechanisms, trying to create objects in a way 
that is suitable for the situation.

Examples:
- Singleton        - Ensures a class has only one instance and provides a global point of access.
- Factory Method   - Defines an interface for creating objects but allows subclasses to
                     alter the type of objects that will be created.
- Prototype        - Creates new objects by copying an existing object instead of creating a new instance from scratch.

- Abstract Factory - Provides an interface for creating families of related or dependent
                     objects without specifying their concrete classes.
- Builder          - Used to construct complex objects step by step.
                     It separates the construction of an object from its representation so that
                     the same construction process can create different representations.
----------------------------------------------------------------------------------------------------------------------
'''


##############################################################################################################################
# Structural Design Patterns(Composition of Classes & Objects)
##############################################################################################################################

'''
2. Structural Design Patterns(Composition of Classes & Objects)

These patterns focus on classes and objects composition. These patterns ensure that if one part of the system changes, 
the entire structure will not have an impact

Examples:
- Adapter          - Allows incompatible interfaces to work together by acting as a bridge.
- Bridge           - Decouples an abstraction from its implementation so that both can vary independently.
- Composite        - Composes objects into tree structures to represent part-whole hierarchies.
- Decorator        - Dynamically adds additional responsibilities to an object.
- Facade           - Provides a unified interface to a set of interfaces in a subsystem.
- Flyweight        - Reduces memory usage by sharing as much data as possible with similar objects.
- Proxy            - Provides a placeholder for another object to control access to it.
----------------------------------------------------------------------------------------------------------------------
'''

##############################################################################################################################
# Behavioral Design Patterns (Object Interaction & Responsibility)
##############################################################################################################################


'''
3. Behavioral Design Patterns (Object Interaction & Responsibility)
These patterns focus on how objects communicate and interact, defining how responsibilities
are divided among classes.

Examples:
- COR              – Passes a request along a chain of handlers until one of them handles it.(Chain of Responsibility)
- Command          – Encapsulates a request as an object, allowing parameterization of clients with different requests.
- Interpreter      – Defines a grammar for a language and provides an interpreter to interpret sentences of the language.
- Iterator         – Provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.
- Mediator         – Defines an object that encapsulates how a set of objects interact.
- Memento          – Captures an object’s internal state to restore it later without exposing its structure.
- Observer         – Defines a one-to-many dependency between objects so that when one object changes state, all dependents are notified.
- State            – Allows an object to change its behavior when its internal state changes.
- Strategy         – Defines a family of algorithms, encapsulates each one, and makes them interchangeable.
- Template Method  – Defines the skeleton of an algorithm in a superclass but lets subclasses override specific steps.
- Visitor          – Separates an algorithm from the object structure it operates on.
----------------------------------------------------------------------------------------------------------------------
'''


