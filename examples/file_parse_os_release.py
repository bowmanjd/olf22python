#!/usr/bin/env python3
"""Example usage of pathlib and shlex to parse file with shell variables."""
import pathlib
import shlex

os_release_file = pathlib.Path("/etc/os-release")
os_release = os_release_file.read_text()
lexer = shlex.shlex(os_release, posix=True)
lexer.whitespace_split = True
os_info = dict(i.split("=") for i in lexer if "=" in i)
print(os_info["PRETTY_NAME"])
