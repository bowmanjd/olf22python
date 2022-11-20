#!/usr/bin/env python3
"""Example using argparse to parse, um, args."""
import argparse
from pathlib import Path

def motder(text):
  filepath = Path("/etc/motd")
  filepath.write_text(text)

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("message", help="The message of the day")
  args = parser.parse_args()
	motder(args.message)
