#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

from pyVim.connect import SmartConnect, Disconnect, SmartConnectNoSSL

esxi_connection = SmartConnectNoSSL(host="10.10.10.115", user="root", pwd='access123')

full_name = esxi_connection.content.about.fullName
version = esxi_connection.content.about.version

print("Server Full name is {}".format(full_name))
print("ESXi version is {}".format(version))

Disconnect(esxi_connection)
