#!/usr/bin/env python3
"""Example usage of sys.argv to parse command line arguments."""
import sys
from pathlib import Path


def motder(text):
    filepath = Path("/etc/motd")
    filepath.write_text(text)


if __name__ == "__main__":
    motder(sys.argv[1])
