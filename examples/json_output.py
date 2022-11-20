#!/usr/bin/env python3
"""Example outputting json."""
import json

data = {"name": "OLF conference", "age": 20}
json_data = json.dumps(data, indent=4)
print(json_data)
