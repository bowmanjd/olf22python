#!/usr/bin/env python3
"""Example HTTP GET request."""
from urllib.request import urlopen

# Avoid unsanitized user inputs, because:
# url = "file:///etc/passwd"
url = "https://wttr.in/Columbus,OH?A1nF"
with urlopen(url) as response:
    print(response.read().decode())
