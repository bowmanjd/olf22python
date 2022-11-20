#!/usr/bin/env python3
"""Example reading a csv file with csv.DictReader."""
import csv
from pathlib import Path

inpath = Path("sample.csv")

with inpath.open(newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row["Name"]
        age = row["Age"]
        print(f"{name} is {age} years old.")
