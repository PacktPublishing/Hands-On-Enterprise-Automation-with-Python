#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

from fabric.api import *

env.hosts = [
    '10.10.10.140',  # ubuntu machine
    '10.10.10.193',  # CentOS machine
    '10.10.10.130',
]

env.roledefs = {
    'webapps': ['10.10.10.140', '10.10.10.193'],
    'databases': ['10.10.10.130'],
}

env.user = "root"
env.password = "access123"


@roles('databases')
def validate_mysql():
    output = run("systemctl status mariadb")


@roles('webapps')
def validate_apache():
    output = run("systemctl status httpd")
