#!/usr/bin/python
import telnetlib
import getpass
import time

switch_ips = ["10.10.88.111", "10.10.88.112", "10.10.88.113", "10.10.88.114"]
username = raw_input("Please Enter your username:")
password = getpass.getpass("Please Enter your Password:")
enable_password = getpass.getpass("Please Enter your Enable Password:")

for sw_ip in switch_ips:
    print "\n#################### Working on Device " + sw_ip + " ####################"
    connection = telnetlib.Telnet(host=sw_ip.strip())
    connection.read_until("Username:")
    connection.write(username + "\n")
    connection.read_until("Password:")
    connection.write(password + "\n")
    connection.read_until(">")
    connection.write("enable" + "\n")
    connection.read_until("Password:")
    connection.write(enable_password + "\n")
    connection.read_until("#")
    connection.write("config terminal" + "\n")  # now i'm in config mode
    vlans = range(300, 400)
    for vlan_id in vlans:
        print "\n********* Adding VLAN " + str(vlan_id) + "**********"
        connection.read_until("#")
        connection.write("vlan " + str(vlan_id) + "\n")
        time.sleep(1)
        connection.write("exit" + "\n")
        connection.read_until("#")
    connection.close()
