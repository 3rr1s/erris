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

# --------------------------
# Main Management System
# --------------------------
class HospitalManagementSystem:
    def __init__(self):
        self.patients: Dict[str, Patient] = {}

def add_patient(self):
    id = input("Enter patient ID: ")
    if id in self.patients:
        print("Patient ID already exists!")
        return
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    illness = input("Enter patient illness: ")
    score = float(input("Enter patient score (0-10): "))
    logic_expr = input("Enter logical expression (e.g., 'age > 50 ∧ score > 7'): ")
    self.patients[id] = Patient(id, name, age, illness, score, logic_expr)
    print("Patient added successfully!")

def view_patients(self, key: str = None):
    if not self.patients:
        print("No patients in the system!")
        return

for patient in self.patients.values():
    if key:
        print(getattr(patient, key))
    else:
        print(patient)

def edit_patient(self):
    id = input("Enter the ID of the patient to edit: ")
    if id not in self.patients:
        print("Patient not found.")
        return

    patient = self.patients[id]

print(f"Editing Patient: {patient}")
name = input(f"Enter new name (leave blank to keep '{patient.name}'): ") or patient.name
age = input(f"Enter new age (leave blank to keep '{patient.age}'): ") or patient.age
illness = input(f"Enter new illness (leave blank to keep '{patient.illness}'): ") or patient.illness
score = input(f"Enter new score (leave blank to keep '{patient.score}'): ") or patient.score
logic_expr = input(f"Enter new logical expression (leave blank to keep '{patient.logic_expr}'): ") or patient.logic_expr