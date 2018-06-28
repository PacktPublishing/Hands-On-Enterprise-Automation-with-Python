#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

from fabric.api import *
from fabric.context_managers import *
from pprint import pprint

env.hosts = [
    '10.10.10.140',  # Ubuntu Machine
    '10.10.10.193',  # CentOS Machine
]

env.user = "root"
env.password = "access123"


def discovery_commands():
    discovery_commands = {
        "uptime": "uptime | awk '{print $3,$4}'",
        "hostname": "hostname",
        "kernel_release": "uname -r",
        "architecture": "uname -m",
        "internal_ip": "hostname -I",
        "external_ip": "curl -s ipecho.net/plain;echo",

    }
    for operation, command in discovery_commands.iteritems():
        print("============================={0}=============================".format(operation))
        output = run(command)


def health_commands():
    health_commands = {
        "used_memory": "free  | awk '{print $3}' | grep -v free | head -n1",
        "free_memory": "free  | awk '{print $4}' | grep -v shared | head -n1",
        "cpu_usr_percentage": "mpstat | grep -A 1 '%usr' | tail -n1 | awk '{print $4}'",
        "number_of_process": "ps -A --no-headers | wc -l",
        "logged_users": "who",
        "top_load_average": "top -n 1 -b | grep 'load average:' | awk '{print $10 $11 $12}'",
        "disk_usage": "df -h| egrep 'Filesystem|/dev/sda*|nvme*'"

    }
    for operation, command in health_commands.iteritems():
        print("============================={0}=============================".format(operation))
        output = run(command)


def get_system_health():
    discovery_commands()
    health_commands()
