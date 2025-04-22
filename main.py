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