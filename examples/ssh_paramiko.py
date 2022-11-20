#!/usr/bin/env python3
"""Example using paramiko SSH library."""
import paramiko

client = paramiko.SSHClient()
client.load_system_host_keys()
client.connect("server", username="user")

stdin, stdout, stderr = client.exec_command("ls /")
root_directories = stdout.read()

sftp = client.open_sftp()
with sftp.file("/etc/os-release") as f:
    for line in f:
        print(line)
