#!/usr/bin/env python3
"""Example usage of pathlib to read file and check for content."""
from pathlib import Path

filepath = Path("/etc/os-release")
os_info = filepath.read_text()
if "Fedora" in os_info:
    print("I still remember Redhat 5.1")
elif "Alpine" in os_info:
    print("Compiled with love and musl")
elif "archlinux" in os_info:
    print("A wiki and the AUR; it " "doesn't get better than this!")
