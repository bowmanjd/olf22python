#!/usr/bin/env python3
"""Examples of common comparison operators."""


def compare(a, b):
    """Compare two numbers."""
    if a == b:
        print("equality")
    if not a == b:
        print("inequality")
    if a != b:
        print("also inequality")
    if a > b:
        print("greater than")
    else:
        print("less than or equal")
    if a <= b:
        print("also less than or equal")


if __name__ == "__main__":
    compare(1, 5)
    compare(7, 3)
    compare(112, 112)
