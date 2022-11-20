#!/usr/bin/env python3
"""Examples of loops."""
import os


def list_environment_variables():
    for variable in os.environ.keys():
        print(variable)


def list_path_dirs():
    for path in os.getenv("PATH", "").split(":"):
        print(path)


def count_to_ten():
    for num in range(10):
        print(num)


def repeat_10():
    for _ in range(10):
        print("Doing this thing 10 times.")


if __name__ == "__main__":
    list_environment_variables()
    list_path_dirs()
    count_to_ten()
    repeat_10()
