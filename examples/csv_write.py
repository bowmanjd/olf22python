#!/usr/bin/env python3
"""Example writing a csv file."""
import csv
from pathlib import Path

outpath = Path("output.csv")

with outpath.open("w", newline="", encoding="utf-8-sig") as outfile:
    writer = csv.writer(outfile)
    new_row = {"First": "Jane", "Last": "Smith"}
    writer.writerow(["Name", "Age"])
    writer.writerow(["John Cleese", 83])
