#!/usr/bin/env python3
"""Example writing a csv file."""
import csv
from pathlib import Path

out = Path("output.csv")

with out.open("w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
    writer.writerow(["John Cleese", 83])
