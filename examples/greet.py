#!/usr/bin/env python3
"""An example of a function with default arguments and f-strings."""


def greet(greeting="Hello", audience="World"):
    return f"{greeting}, {audience}!"


if __name__ == "__main__":
    greet()
    greet("Salutations", "Galaxy")
    greet(audience="Galaxy")
