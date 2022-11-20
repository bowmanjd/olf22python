#!/usr/bin/env python3
"""Example usage of pathlib to write file content."""
from pathlib import Path

filepath = Path("/etc/motd")
weather = "There will be temperatures today with a chance of weather."
filepath.write_text(weather)
