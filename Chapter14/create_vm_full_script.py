#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

import paramiko
from scp import SCPClient
import time
from jinja2 import FileSystemLoader, Environment
import os
import xlrd


def upload_and_create_directory(vm_name, hdd_size, source_file):
    commands = ["mkdir /vmfs/volumes/datastore1/{0}".format(vm_name),
                "vmkfstools -c {0}g -a lsilogic -d zeroedthick /vmfs/volumes/datastore1/{1}/{1}.vmdk".format(hdd_size,
                                                                                                             vm_name), ]
    register_command = "vim-cmd solo/registervm /vmfs/volumes/datastore1/{0}/{0}.vmx".format(vm_name)

    ipaddr = "10.10.10.115"
    username = "root"
    password = "access123"

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(ipaddr, username=username, password=password, look_for_keys=False, allow_agent=False)

    for cmd in commands:
        try:
            stdin, stdout, stderr = ssh.exec_command(cmd)
            print " DEBUG: ... Executing the command on ESXI server".format(str(stdout.readlines()))

        except Exception as e:
            print e
            pass
            print " DEBUG: **ERR....unable to execute command"
        time.sleep(2)
    with SCPClient(ssh.get_transport()) as scp:
        print(" DEBUG: ... Uploading file to the datastore")
        scp.put(source_file, remote_path='/vmfs/volumes/datastore1/{0}'.format(vm_name))
        print(" DEBUG: ... Register the virtual machine {}".format(vm_name))
        ssh.exec_command(register_command)

    ssh.close()


print("The script working directory is {}".format(os.path.dirname(__file__)))
script_dir = os.path.dirname(__file__)

vmx_env = Environment(
    loader=FileSystemLoader(script_dir),
    trim_blocks=True,
    lstrip_blocks=True
)

workbook = xlrd.open_workbook(os.path.join(script_dir, "vm_inventory.xlsx"))
sheet = workbook.sheet_by_index(0)
print("The number of rows inside the Excel sheet is {}".format(sheet.nrows))
print("The number of columns inside the Excel sheet is {}".format(sheet.ncols))

vmx_data = {}

for row in range(1, sheet.nrows):
    vm_name = sheet.row(row)[0].value
    vm_memory_size = int(sheet.row(row)[1].value)
    vm_cpu = int(sheet.row(row)[2].value)
    cpu_per_socket = int(sheet.row(row)[3].value)
    vm_hdd_size = int(sheet.row(row)[4].value)
    vm_guest_os = sheet.row(row)[5].value
    vm_network1 = sheet.row(row)[6].value

    vmx_data["vm_name"] = vm_name
    vmx_data["vm_memory_size"] = vm_memory_size
    vmx_data["vm_cpu"] = vm_cpu
    vmx_data["cpu_per_socket"] = cpu_per_socket
    vmx_data["vm_hdd_size"] = vm_hdd_size
    vmx_data["vm_guest_os"] = vm_guest_os
    if vm_guest_os == "ubuntu-64":
        vmx_data["vm_image"] = "ubuntu-16.04.4-server-amd64.iso"

    elif vm_guest_os == "centos-64":
        vmx_data["vm_image"] = "CentOS-7-x86_64-Minimal-1708.iso"

    elif vm_guest_os == "windows7-64":
        vmx_data["vm_image"] = "windows_7_ultimate_sp1_ x86-x64_bg-en_IE10_ April_2013.iso"

    vmx_data["vm_network1"] = vm_network1

    vmx_data = vmx_env.get_template("vmx_template.j2").render(vmx_data)
    with open(os.path.join(script_dir, "vmx_files/{}.vmx".format(vm_name)), "w") as f:
        print("Writing Data of {} into directory".format(vm_name))
        f.write(vmx_data)
        print(" DEBUG:Communicating with ESXi server to upload and register the VM")
    upload_and_create_directory(vm_name,
                                vm_hdd_size,
                                os.path.join(script_dir, "vmx_files", "{}.vmx".format(vm_name)))
    vmx_data = {}
