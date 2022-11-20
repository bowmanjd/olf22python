#!/usr/bin/env python3
"""Using subproces.check_output()."""
import subprocess

output = subprocess.check_output(["ip", "addr"], text=True)

print(output)
