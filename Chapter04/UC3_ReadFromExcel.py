__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

from netmiko import ConnectHandler
from netmiko.ssh_exception import AuthenticationException, NetMikoTimeoutException
import xlrd
from pprint import pprint

workbook = xlrd.open_workbook(
    r"/media/bassim/DATA/GoogleDrive/Packt/EnterpriseAutomationProject/Chapter4_Using_Python_to_manage_network_devices/UC3_devices.xlsx")

sheet = workbook.sheet_by_index(0)

for index in range(1, sheet.nrows):
    hostname = sheet.row(index)[0].value
    ipaddr = sheet.row(index)[1].value
    username = sheet.row(index)[2].value
    password = sheet.row(index)[3].value
    enable_password = sheet.row(index)[4].value
    vendor = sheet.row(index)[5].value

    device = {
        'device_type': vendor,
        'ip': ipaddr,
        'username': username,
        'password': password,
        'secret': enable_password,

    }
    # pprint(device)

    print "########## Connecting to Device {0} ############".format(device['ip'])
    try:
        net_connect = ConnectHandler(**device)
        net_connect.enable()

        print "***** show ip configuration of Device *****"
        output = net_connect.send_command("show ip int b")
        print output

        net_connect.disconnect()

    except NetMikoTimeoutException:
        print "=======SOMETHING WRONG HAPPEN WITH {0}=======".format(device['ip'])

    except AuthenticationException:
        print "=======Authentication Failed with {0}=======".format(device['ip'])

    except Exception as unknown_error:
        print "=======SOMETHING UNKNOWN HAPPEN WITH {0}======="
