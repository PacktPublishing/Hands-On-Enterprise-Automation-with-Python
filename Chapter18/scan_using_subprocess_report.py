#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

import subprocess
from netaddr import IPNetwork, AddrFormatError
from prettytable import PrettyTable
import re


def nmap_report(data):
    mac_flag = ""
    ip_flag = ""
    Host_Table = PrettyTable(["IP", "MAC", "Vendor"])
    number_of_hosts = data.count("Host is up ")

    for line in data.split("\n"):
        if "MAC Address:" in line:
            mac = line.split("(")[0].replace("MAC Address: ", "")
            vendor = line.split("(")[1].replace(")", "")
            mac_flag = "ready"
        elif "Nmap scan report for" in line:
            ip = re.search(r"Nmap scan report for (.*)", line).groups()[0]
            ip_flag = "ready"

        if mac_flag == "ready" and ip_flag == "ready":
            Host_Table.add_row([ip, mac, vendor])
            mac_flag = ""
            ip_flag = ""

    print("Number of Live Hosts is {}".format(number_of_hosts))
    print Host_Table


network = "192.168.1.0/24"

try:
    IPNetwork(network)  # This will validate the network is correctly formatted
    p = subprocess.Popen(["sudo", "nmap", "-sP", network], stdout=subprocess.PIPE)
    nmap_report(p.stdout.read())
except AddrFormatError:
    print("Please Enter a valid network IP address in x.x.x.x/y format")
