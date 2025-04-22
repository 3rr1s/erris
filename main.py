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