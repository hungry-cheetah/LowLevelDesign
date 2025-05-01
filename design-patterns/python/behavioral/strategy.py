# The Strategy Design Pattern allows a class's behavior to be selected at runtime.
# It defines a family of algorithms, encapsulates each one, and makes them interchangeable
# without modifying client code.


# ✅ Encapsulation → Each sorting algorithm is implemented as a separate class.
# ✅ Interchangeability → The sorting strategy can be changed dynamically at runtime.
# ✅ Loose Coupling → The Sorter class doesn’t need to know how each sorting method works.
# ✅ Real-World Example → Similar to e-commerce websites, where users can sort products by Price, Ratings, or Popularity.


from abc import ABC, abstractmethod

# Strategy Interface
class SortingStrategy(ABC):
    """Abstract Strategy defining the sorting behavior"""

    @abstractmethod
    def sort(self, data):
        pass

# Concrete Strategy: Bubble Sort
class BubbleSort(SortingStrategy):
    def sort(self, data):
        arr = data[:]
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print("📊 Sorted using Bubble Sort:", arr)
        return arr

# Concrete Strategy: Quick Sort
class QuickSort(SortingStrategy):
    def sort(self, data):
        arr = data[:]
        self.quick_sort_helper(arr, 0, len(arr) - 1)
        print("⚡ Sorted using Quick Sort:", arr)
        return arr

    def quick_sort_helper(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.quick_sort_helper(arr, low, pi - 1)
            self.quick_sort_helper(arr, pi + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

# Concrete Strategy: Merge Sort
class MergeSort(SortingStrategy):
    def sort(self, data):
        arr = data[:]
        self.merge_sort_helper(arr)
        print("🔀 Sorted using Merge Sort:", arr)
        return arr

    def merge_sort_helper(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            self.merge_sort_helper(left_half)
            self.merge_sort_helper(right_half)

            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

# Context: Sorting Context
class Sorter:
    """Context that uses a sorting strategy"""

    def __init__(self, strategy: SortingStrategy):
        self._strategy = strategy  # Set the strategy at runtime

    def set_strategy(self, strategy: SortingStrategy):
        """Dynamically change the strategy"""
        self._strategy = strategy

    def sort(self, data):
        """Delegate sorting to strategy"""
        return self._strategy.sort(data)

# Client Code
if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]

    # Create a Sorter with Bubble Sort
    sorter = Sorter(BubbleSort())
    sorter.sort(numbers)

    # Switch to Quick Sort
    sorter.set_strategy(QuickSort())
    sorter.sort(numbers)

    # Switch to Merge Sort
    sorter.set_strategy(MergeSort())
    sorter.sort(numbers)
