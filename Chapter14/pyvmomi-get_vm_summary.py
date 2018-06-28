#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

from pyVim.connect import SmartConnect, Disconnect, SmartConnectNoSSL

esxi_connection = SmartConnectNoSSL(host="10.10.10.115", user="root", pwd='access123')

datacenter = esxi_connection.content.rootFolder.childEntity[0]  # First Datacenter in the ESXI\

virtual_machines = datacenter.vmFolder.childEntity  # Access the child inside the vmFolder

print virtual_machines

for machine in virtual_machines:
    print(machine.name)
    try:
        guest_vcpu = machine.summary.config.numCpu
        print("  The Guest vCPU is {}".format(guest_vcpu))

        guest_os = machine.summary.config.guestFullName
        print("  The Guest Operating System is {}".format(guest_os))

        guest_mem = machine.summary.config.memorySizeMB
        print("  The Guest Memory is {}".format(guest_mem))

        ipadd = machine.summary.guest.ipAddress
        print("  The Guest IP Address is {}".format(ipadd))
        print "================================="
    except:
        print("  Can't get the summary")

Disconnect(esxi_connection)
