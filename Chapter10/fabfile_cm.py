#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

from fabric.api import *
from fabric.context_managers import *

env.hosts = [
    '10.10.10.140',  # ubuntu machine
    '10.10.10.193',  # CentOS machine
]

env.user = "root"
env.password = "access123"


def list_directory():
    with cd("/var/log"):
        run("ls")


def list_directory_nested():
    with cd("/var/"):
        with cd("log"):
            run("ls")


def uploading_file():
    with lcd("/root/"):
        put("VeryImportantFile.txt")


def change_shell_env():
    with shell_env(test1='val1', test2='val2', test3='val3'):
        run("echo $test1")  # This command is executed on remote host
        run("echo $test2")
        run("echo $test3")
        local("echo $test1")  # This command is executed on local host


def prefixing_commands():
    with prefix("source ~/env/bin/activate"):
        sudo('pip install wheel')
        sudo("pip install -r requirements.txt")
        sudo("python manage.py migrate")
