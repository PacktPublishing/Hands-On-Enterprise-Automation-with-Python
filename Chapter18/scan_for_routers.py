#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

from prettytable import PrettyTable
import subprocess
import re


def get_port_status(port, data):
    port_status = re.findall(r"{0}/tcp (\S+) .*".format(port), data)[0]
    return port_status


Router_Table = PrettyTable(["IP Address", "Opened Services"])
router_ports = {"FTP": 21,
                "SSH": 22,
                "TELNET": 23,
                "SMTP": 25,
                "HTTP": 80,
                "HTTPS": 443,
                "SNMP": 161,
                "BGP": 179,
                "LDP": 646,
                "RPCBIND": 111,
                "NETCONF": 830,
                "XNM-CLEAR-TEXT": 3221}

# we can use nmap with -sP flag to get the live hosts as we did in previous script
live_hosts = ["10.10.10.1", "10.10.10.2", "10.10.10.65"]

services_status = {}
for ip in live_hosts:
    for service, port in router_ports.iteritems():
        p = subprocess.Popen(["sudo", "nmap", "-p", str(port), ip], stdout=subprocess.PIPE)
        port_status = get_port_status(port, p.stdout.read())
        services_status[service] = port_status

    services_status_joined = "\n".join("{} : {}".format(key, value) for key, value in services_status.iteritems())

    Router_Table.add_row([ip, services_status_joined])

print Router_Table
