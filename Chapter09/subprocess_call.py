#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

import subprocess

try:
    result = subprocess.check_call(["ping", "HostNotExist", "-c", "3"])
except subprocess.CalledProcessError:
    print("Host is not found")
