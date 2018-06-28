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


def detect_host_type():
    output = run("uname -s")

    if output.failed:
        print("something wrong happen, please check the logs")

    elif output.succeeded:
        print("command executed successfully")


def list_all_files_in_directory():
    directory = prompt("please enter full path to the directory to list", default="/root")
    sudo("cd {0} ; ls -htlr".format(directory))


def main_tasks():
    detect_host_type()
    list_all_files_in_directory()
