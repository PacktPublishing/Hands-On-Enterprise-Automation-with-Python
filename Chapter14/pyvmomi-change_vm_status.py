#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

from pyVim.connect import SmartConnect, Disconnect, SmartConnectNoSSL

esxi_connection = SmartConnectNoSSL(host="10.10.10.115", user="root", pwd='access123')

datacenter = esxi_connection.content.rootFolder.childEntity[0]  # First Datacenter in the ESXI\

virtual_machines = datacenter.vmFolder.childEntity  # Access the child inside the vmFolder

for machine in virtual_machines:
    try:
        powerstate = machine.summary.runtime.powerState
        if "python-vm" in machine.name and powerstate == "poweredOff":
            print(machine.name)
            print("     The Guest Power state is {}".format(powerstate))
            machine.PowerOn()
            print("**Powered On the virtual machine**")

        elif "python-vm" in machine.name and powerstate == "poweredOn":
            print(machine.name)
            print("     The Guest Power state is {}".format(powerstate))
            machine.PowerOff()
            print("**Powered Off the virtual machine**")
    except:
        print("  Can't execute the task")

Disconnect(esxi_connection)
