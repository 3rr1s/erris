import csv
import time
from typing import List, Dict

# -------------------------------
# Patient Class with Logical Expr
# -------------------------------
class Patient:
  def __init__(self, id: str, name: str, age: int, illness: str, score: