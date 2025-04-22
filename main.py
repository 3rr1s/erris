import csv
import time
from typing import List, Dict

# -------------------------------
# Patient Class with Logical Expr
# -------------------------------
class Patient:
    def __init__(self, id: str, name: str, age: int, illness: str, score: float = 0.0, logic_expr: str = ""):
        self.id = id
        self.name = name
        self.age = age
        self.illness = illness
        self.score = score
        self.logic_expr = logic_expr

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Illness: {self.illness}, Score: {self.score}, Logic: {self.logic_expr}"
        
        def evaluate_logic(self):
            expr = self.logic_expr.replace("age", str(self.age)).replace("score", str(self.score))
            expr = expr.replace("∧", "and").replace("∨", "or").replace("¬", "not ").replace("→", "<=").replace("⇔", "==")
            try:
                return eval(expr)
            except Exception as e:
                return False

        # --------------------------
        # Sorting Strategy (OOP Add)
        # --------------------------
        class SortingStrategy:
            def sort(self, data: List[Patient], key: str):
                raise NotImplementedError("This method should be overridden.")

class BubbleSort(SortingStrategy):
    def sort(self, data: List[Patient], key: str):
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if str(getattr(data[j], key)).lower() > str(getattr(data[j + 1], key)).lower():
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data

class MergeSort(SortingStrategy):
    def sort(self, data: List[Patient], key: str):
        def merge(left, right):
            result = []
            i = j = 0
            while i < len(left) and j < len(right):
                if str(getattr(left[i], key)).lower() <= str(getattr(right[j], key)).lower():
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result

def recursive_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = recursive_sort(arr[:mid])
    right = recursive_sort(arr[mid:])
    return merge(left, right)

return recursive_sort(data)