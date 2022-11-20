#!/usr/bin/env python3
"""Example of file editing using temporary file."""
import pathlib
import shutil
import subprocess
import tempfile

tempdir = pathlib.Path(tempfile.mkdtemp())
temp_motd = tempdir / "motd"
temp_motd.write_text("Welcome, user!")
motd = pathlib.Path("/etc/motd")
subprocess.check_call(["sudo", "cp", temp_motd, motd])
shutil.rmtree(tempdir, ignore_errors=True)
