#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

import xlrd

workbook = xlrd.open_workbook(
    r"/media/bassim/DATA/GoogleDrive/Packt/EnterpriseAutomationProject/Chapter14_Creating_and_managing_VMWare_virtual_machines/vm_inventory.xlsx")
sheet = workbook.sheet_by_index(0)
print(sheet.nrows)
print(sheet.ncols)

print(int(sheet.row(1)[1].value))

for row in range(1, sheet.nrows):
    vm_name = sheet.row(row)[0].value
    vm_memory_size = int(sheet.row(row)[1].value)
    vm_cpu = int(sheet.row(row)[2].value)
    cpu_per_socket = int(sheet.row(row)[3].value)
    vm_hdd_size = int(sheet.row(row)[4].value)
    vm_guest_os = sheet.row(row)[5].value
    vm_network1 = sheet.row(row)[6].value
