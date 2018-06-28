#!/usr/bin/python

__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

from netmiko import ConnectHandler
from datetime import datetime

with open(
        "/media/bassim/DATA/GoogleDrive/Packt/EnterpriseAutomationProject/Chapter5_Using_Python_to_manage_network_devices/UC1_devices.txt") as devices_file:
    devices = devices_file.readlines()

for line in devices:
    line = line.strip("\n")
    ipaddr = line.split(",")[0]
    username = line.split(",")[1]
    password = line.split(",")[2]
    enable_password = line.split(",")[3]
    vendor = line.split(",")[4]
    if vendor.lower() == "cisco":
        device_type = "cisco_ios"
        backup_command = "show running-config"

    elif vendor.lower() == "juniper":
        device_type = "juniper"
        backup_command = "show configuration | display set"

    print str(datetime.now()) + " Connecting to device {}".format(ipaddr)

    net_connect = ConnectHandler(device_type=device_type,
                                 ip=ipaddr,
                                 username=username,
                                 password=password,
                                 secret=enable_password)
    net_connect.enable()
    running_config = net_connect.send_command(backup_command)

    print str(datetime.now()) + " Saving config from device {}".format(ipaddr)

    f = open("dev_" + ipaddr + "_.cfg", "w")
    f.write(running_config)
    f.close()
    print "=============================================="

# Result should be
# dev_10.10.88.110_.cfg
# dev_10.10.88.111_.cfg
# dev_10.10.88.112_.cfg
# dev_10.10.88.113_.cfg
# dev_10.10.88.114_.cfg
