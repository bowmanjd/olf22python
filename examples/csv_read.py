#!/usr/bin/env python3
"""Example reading a csv file."""
import csv
from pathlib import Path

inpath = Path("sample.csv")

with inpath.open(newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header
    for row in reader:
        name = row[0]
        age = row[1]
        print(f"{name} is {age} years old.")
