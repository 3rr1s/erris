
import pandas as pd
from typing import List, Any, Callable
from abc import ABC, abstractmethod
import time
import csv

class DataObject:
    def __init__(self, value: Any, logical_expression: str):
        self.value = value
        self.logical_expression = logical_expression
        self._truth_value = None

    def evaluate_logic(self) -> bool:
        # Simple evaluation of basic logical expressions
        try:
            # Safety: Only allow basic logical operations
            allowed_chars = set('pqr∧∨→↔()True False')
            if not all(c in allowed_chars for c in self.logical_expression):
                raise ValueError("Invalid characters in logical expression")
            self._truth_value = eval(self.logical_expression.replace('∧', 'and')
                                                          .replace('∨', 'or')
                                                          .replace('→', '<=')
                                                          .replace('↔', '=='))
            return self._truth_value
        except:
            return False

    def __str__(self):
        return f"Value: {self.value}, Logic: {self.logical_expression} = {self._truth_value}"

class SortingAlgorithm(ABC):
    @abstractmethod
    def sort(self, data: List[DataObject]) -> List[DataObject]:
        pass

    def measure_time(self, data: List[DataObject]) -> float:
        start_time = time.time()
        self.sort(data)
        return time.time() - start_time

class InsertionSort(SortingAlgorithm):
    def sort(self, data: List[DataObject]) -> List[DataObject]:
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and data[j].value > key.value:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
        
        # Secondary sorting based on truth values
        data.sort(key=lambda x: x.evaluate_logic(), reverse=True)
        return data

class MergeSort(SortingAlgorithm):
    def merge(self, left: List[DataObject], right: List[DataObject]) -> List[DataObject]:
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i].value <= right[j].value:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def sort(self, data: List[DataObject]) -> List[DataObject]:
        if len(data) <= 1:
            return data
            
        mid = len(data) // 2
        left = self.sort(data[:mid])
        right = self.sort(data[mid:])
        
        sorted_data = self.merge(left, right)
        # Secondary sorting based on truth values
        sorted_data.sort(key=lambda x: x.evaluate_logic(), reverse=True)
        return sorted_data

def main():
    # Example usage
    data_objects = [
        DataObject(5, "True and False"),
        DataObject(3, "True or False"),
        DataObject(7, "True and True"),
        DataObject(1, "False or True"),
    ]

    print("Original Data:")
    for obj in data_objects:
        print(obj)

    # Test sorting algorithms
    insertion_sort = InsertionSort()
    merge_sort = MergeSort()

    print("\nInsertion Sort Result:")
    sorted_data = insertion_sort.sort(data_objects.copy())
    for obj in sorted_data:
        print(obj)

    print("\nMerge Sort Result:")
    sorted_data = merge_sort.sort(data_objects.copy())
    for obj in sorted_data:
        print(obj)

    # Performance Analysis
    print("\nPerformance Analysis:")
    insertion_time = insertion_sort.measure_time(data_objects.copy())
    merge_time = merge_sort.measure_time(data_objects.copy())
    
    print(f"Insertion Sort Time: {insertion_time:.6f} seconds")
    print(f"Merge Sort Time: {merge_time:.6f} seconds")

if __name__ == "__main__":
    main()
