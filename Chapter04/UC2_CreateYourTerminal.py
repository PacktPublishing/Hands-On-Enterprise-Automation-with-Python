#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

import telnetlib

connection = telnetlib.Telnet(host="10.10.88.110")
connection.read_until("Username:")
connection.write("admin" + "\n")
connection.read_until("Password:")
connection.write("access123" + "\n")
connection.read_until(">")
connection.write("en" + "\n")
connection.read_until("Password:")
connection.write("access123" + "\n")
connection.read_until("#")
connection.write("terminal length 0" + "\n")
connection.read_until("#")
while True:
    command = raw_input("#:")
    if "health" in command.lower():
        commands = ["show ip int b",
                    "show ip route",
                    "show clock",
                    "show banner motd"
                    ]

    elif "discover" in command.lower():
        commands = ["show arp",
                    "show version | i uptime",
                    "show inventory",
                    ]
    else:
        commands = [command]
    for cmd in commands:
        connection.write(cmd + "\n")
        output = connection.read_until("#")
        print output
        print "==================="
