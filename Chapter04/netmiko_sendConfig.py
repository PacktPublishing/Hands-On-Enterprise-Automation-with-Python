__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

from netmiko import ConnectHandler

SW2 = {
    'device_type': 'cisco_ios',
    'ip': '10.10.88.112',
    'username': 'admin',
    'password': 'access123',
    'secret': 'access123',
}

core_sw_config = ["int range gig0/1 - 2", "switchport trunk encapsulation dot1q",
                  "switchport mode trunk", "switchport trunk allowed vlan 1,2"]

print "########## Connecting to Device {0} ############".format(SW2['ip'])
net_connect = ConnectHandler(**SW2)
net_connect.enable()

print "***** Sending Configuration to Device *****"
net_connect.send_config_set(core_sw_config)

###################################################################################


# Send Configuration from file


from netmiko import ConnectHandler

connect_sw2 = ConnectHandler(**SW2)

connect_sw2.enable()

connect_sw2.send_config_from_file(config_file="/root/" + sw_ip + ".txt")
connect_sw2.disconnect()
