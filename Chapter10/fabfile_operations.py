#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

from fabric.api import *

env.hosts = [
    '10.10.10.140',  # ubuntu machine
    '10.10.10.193',  # CentOS machine
]

env.user = "root"
env.password = "access123"


def run_ops():
    output = run("hostname")


def get_ops():
    try:
        get("/var/log/messages", "/root/")
    except:
        pass


def put_ops():
    try:
        put("/root/VeryImportantFile.txt", "/root/")
    except:
        pass


def sudo_ops():
    sudo("whoami")  # it should print the root even if you use another account


def prompt_ops():
    prompt("please supply release name", default="7.4.1708")


def reboot_ops():
    reboot(wait=60, use_sudo=True)
