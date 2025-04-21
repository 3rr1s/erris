# hospital_sorting_tool.py

import csv
import time
import operator
import re
from typing import List

# Truth evaluator class
class TruthEvaluator:
    OPERATORS = {
        '\u2227': operator.and_,  # ∧
        '\u2228': operator.or_,   # ∨
        '\u00AC': lambda x: not x,  # ¬
        '\u2192': lambda x, y: (not x) or y,  # →
        '\u2194': lambda x, y: x == y  # ↔
    }

    @staticmethod
    def evaluate(expression: str, variables: dict) -> bool:
        expr = expression
        for var, val in variables.items():
            expr = expr.replace(var, str(val))

        expr = expr.replace('∧', ' and ').replace('∨', ' or ').replace('¬', ' not ').replace('→', ' <= ').replace('↔', ' == ')
        try:
            return eval(expr)
        except:
            return False

# Patient class
class Patient:
    def __init__(self, name, age, score, expression, variables):
        self.name = name
        self.age = int(age)
        self.score = float(score)
        self.expression = expression
        self.variables = {k: v == 'True' for k, v in variables.items()}
        self.logic_result = TruthEvaluator.evaluate(expression, self.variables)

    def __str__(self):
        return f"{self.name}, Age: {self.age}, Score: {self.score}, Expr: {self.expression}, Logic: {self.logic_result}"

# Sorting tool
class SortingTool:

    @staticmethod
    def bubble_sort(patients: List[Patient]) -> List[Patient]:
        n = len(patients)
        for i in range(n):
            for j in range(0, n - i - 1):
                if SortingTool.compare(patients[j], patients[j + 1]) > 0:
                    patients[j], patients[j + 1] = patients[j + 1], patients[j]
        return patients

    @staticmethod
    def merge_sort(patients: List[Patient]) -> List[Patient]:
        if len(patients) <= 1:
            return patients
        mid = len(patients) // 2
        left = SortingTool.merge_sort(patients[:mid])
        right = SortingTool.merge_sort(patients[mid:])
        return SortingTool.merge(left, right)

    @staticmethod
    def merge(left: List[Patient], right: List[Patient]) -> List[Patient]:
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if SortingTool.compare(left[i], right[j]) <= 0:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    @staticmethod
    def compare(p1: Patient, p2: Patient):
        if p1.score != p2.score:
            return -1 if p1.score > p2.score else 1
        if p1.logic_result != p2.logic_result:
            return -1 if p1.logic_result else 1
        return 0

# CSV data loader
class DataLoader:
    @staticmethod
    def load_csv(file_path: str) -> List[Patient]:
        patients = []
        try:
            with open(file_path, mode='r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if not all(k in row for k in ['name', 'age', 'score', 'expression']):
                        print(f"Warning: Skipping row due to missing required fields: {row}")
                        continue
                    name = row['name']
                    age = row['age']
                    score = row['score']
                    expr = row['expression']
                    vars = {k: row[k] for k in row if k not in ['name', 'age', 'score', 'expression']}
                    patients.append(Patient(name, age, score, expr, vars))
            return patients
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found")
            return []
        except Exception as e:
            print(f"Error loading CSV: {str(e)}")
            return []

# CLI Interface
class CLI:
    def __init__(self):
        self.patients = []

    def display_menu(self):
        print("\nHospital Patient Management System")
        print("1. Add Patient")
        print("2. Edit Patient")
        print("3. View Patients")
        print("4. Sort (Bubble Sort)")
        print("5. Sort (Merge Sort)")
        print("6. Search by ID")
        print("7. Load from CSV")
        print("8. Save to CSV")
        print("9. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-9): ")
            
            if choice == '1':
                print("Add Patient - Not implemented yet")
            elif choice == '2':
                print("Edit Patient - Not implemented yet")
            elif choice == '3':
                print("\nCurrent Patients:")
                for p in self.patients:
                    print(p)
            elif choice == '4':
                start = time.time()
                self.patients = SortingTool.bubble_sort(self.patients)
                end = time.time()
                print(f"Sorted using Bubble Sort. Time taken: {end - start:.6f} seconds")
            elif choice == '5':
                start = time.time()
                self.patients = SortingTool.merge_sort(self.patients)
                end = time.time()
                print(f"Sorted using Merge Sort. Time taken: {end - start:.6f} seconds")
            elif choice == '6':
                print("Search by ID - Not implemented yet")
            elif choice == '7':
                file_path = input("Enter path to CSV file: ")
                self.patients = DataLoader.load_csv(file_path)
            elif choice == '8':
                print("Save to CSV - Not implemented yet")
            elif choice == '9':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == '__main__':
    CLI().run()