#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

import subprocess

print(subprocess.Popen("ifconfig"))

# You can re-write the code and use the list
import subprocess

print(subprocess.Popen(["ifconfig"]))

# using a list, you can bypass additional args to the command
import subprocess

print(subprocess.Popen(["sudo", "ifconfig", "enp60s0:0", "10.10.10.2", "netmask", "255.255.255.0", "up"]))

# using shell=True to spawn the process from string
import subprocess

print(subprocess.Popen("sudo ifconfig enp60s0:0 10.10.10.2 netmask 255.255.255.0 up", shell=True))

# using the cwd
import subprocess

print(subprocess.Popen(["cat", "interfaces"], cwd="/etc/network"))

# using the Pipes
##Output
import subprocess

p = subprocess.Popen(["ping", "8.8.8.8", "-c", "3"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
stdout, stderr = p.communicate()
print("""==========The Standard Output is========== 
{}""".format(stdout))

print("""==========The Standard Error is========== 
{}""".format(stderr))

##Input
# while True:
import subprocess

p = subprocess.Popen(["grep", "subprocess"], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
stdout, stderr = p.communicate(
    input=b"welcome to subprocess module\nthis line is a new line and doesnot contain the require string")

print("""==========The Standard Output is========== 
{}""".format(stdout))

print("""==========The Standard Error is========== 
{}""".format(stderr))

subprocess.call()
