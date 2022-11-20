#!/usr/bin/env python3
"""Using subproces.run()."""
import subprocess

result = subprocess.run(["ip", "addr"], capture_output=True, text=True)

if result.returncode == 0 and result.stdout:
    print(result.stdout)
