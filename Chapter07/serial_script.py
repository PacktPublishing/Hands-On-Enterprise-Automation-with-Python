#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

from netmiko import ConnectHandler
from devices import R1, SW1, SW2, SW3, SW4

nodes = [R1, SW1, SW2, SW3, SW4]

for device in nodes:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show run")
    print output
