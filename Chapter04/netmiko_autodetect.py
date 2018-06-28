#!/usr/local/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

from netmiko import SSHDetect, Netmiko

device = {
    'device_type': 'autodetect',
    'host': '10.10.88.110',
    'username': 'admin',
    'password': "access123",
}

detect_device = SSHDetect(**device)
device_type = detect_device.autodetect()
print(device_type)
print(detect_device.potential_matches)

device['device_type'] = device_type
connection = Netmiko(**device)
