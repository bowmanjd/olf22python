#!/usr/bin/env python3
"""Example usage of pathlib to open file and then iterate line by line."""
from pathlib import Path

filepath = Path("/etc/os-release")
with filepath.open() as f:
    for line in f:
        if line.startswith("PRETTY_NAME"):
            print(line.strip())
