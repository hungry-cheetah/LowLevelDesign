# The Template Method Pattern defines the skeleton of an algorithm in a base class but lets
#  subclasses override specific steps of the algorithm without modifying the structure.

# 📌 Key Features of Template Method Pattern
# ✅ Encapsulates algorithm structure in a base class.
# ✅ Allows subclasses to override specific steps while keeping the core structure intact.
# ✅ Avoids duplicate code by reusing common logic.
# ✅ Follows the Open/Closed Principle → The base class is open for extension but closed for modification.

# 📌 Advantages
# ✔ Avoids duplicate code by reusing common logic in the base class.
# ✔ Easy to extend → New processing methods can be added without modifying the existing logic.
# ✔ Maintains consistency → All subclasses follow the same workflow structure.


from abc import ABC, abstractmethod

# Abstract Base Class (Template)
class DataProcessor(ABC):
    """Defines the template method for processing data"""

    def process(self):
        """Template method defining the workflow"""
        self.load_data()
        self.process_data()
        self.save_results()

    @abstractmethod
    def load_data(self):
        """Step 1: Load data (to be implemented by subclasses)"""
        pass

    @abstractmethod
    def process_data(self):
        """Step 2: Process data (to be implemented by subclasses)"""
        pass

    def save_results(self):
        """Step 3: Save results (common for all subclasses)"""
        print("📂 Results saved successfully!\n")

# Concrete Class: CSV Data Processing
class CSVProcessor(DataProcessor):
    def load_data(self):
        print("📄 Loading data from CSV file...")

    def process_data(self):
        print("🔄 Processing CSV data...")

# Concrete Class: JSON Data Processing
class JSONProcessor(DataProcessor):
    def load_data(self):
        print("📜 Loading data from JSON file...")

    def process_data(self):
        print("🔄 Processing JSON data...")

# Client Code
if __name__ == "__main__":
    print("🟢 Running CSV Data Processing:")
    csv_processor = CSVProcessor()
    csv_processor.process()

    print("🟢 Running JSON Data Processing:")
    json_processor = JSONProcessor()
    json_processor.process()
