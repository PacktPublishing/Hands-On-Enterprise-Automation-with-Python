#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

from netmiko import ConnectHandler

device = {"device_type": "cisco_ios",
          "ip": "10.10.88.110",
          "username": "admin",
          "password": "access123"}

net_connect = ConnectHandler(**device)
output = net_connect.send_command("show arp")
