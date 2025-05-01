from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def show_details(self, index=0):
        pass

class IC(Employee):
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def show_details(self, index=0):
        print(" "*index + f"|-- {self.position}: {self.name}")

class Manager(Employee):
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.team = []

    def add(self, employee):
        self.team.append(employee)

    def remove(self, employee):
        self.team.remove(employee)

    def show_details(self, index=0):
        # super().show_details()
        print(" " * index + f"|-- {self.position}: {self.name}")  # Print manager details

        for employee in self.team:
            employee.show_details(index+4)


if __name__ == "__main__":
    # Creating individual employees
    emp1 = IC("Alice", "Developer")
    emp2 = IC("Bob", "Designer")
    emp3 = IC("Charlie", "Tester")
    
    # Creating managers
    manager1 = Manager("David", "Team Lead")
    manager1.add(emp1)
    manager1.add(emp2)
    
    manager2 = Manager("Eve", "QA Lead")
    manager2.add(emp3)

    # Creating the CEO
    ceo = Manager("Frank", "CEO")
    ceo.add(manager1)
    ceo.add(manager2)

    print("")
    # Displaying the organization structure
    ceo.show_details()
