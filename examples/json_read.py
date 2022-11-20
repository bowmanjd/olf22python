#!/usr/bin/env python3
"""Example reading dockerd config JSON."""
import json
from pathlib import Path

filepath = Path("/etc/docker/daemon.conf")
filetext = filepath.read_text()
dockerd_conf = json.loads(filetext)
