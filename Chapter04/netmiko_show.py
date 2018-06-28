__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

from netmiko import ConnectHandler

R1 = {
    'device_type': 'cisco_ios',
    'ip': '10.10.88.110',
    'username': 'admin',
    'password': 'access123',
    'secret': 'access123',
}

connection = ConnectHandler(**R1)

connection.enable()
output = connection.send_command("show ip int b")
print output

###############Show the prompt and command#######################


from netmiko import ConnectHandler

R1 = {
    'device_type': 'cisco_ios',
    'ip': '10.10.88.110',
    'username': 'admin',
    'password': 'access123',
    'secret': 'access123',
}

connection = ConnectHandler(**R1)

connection.enable()
output = connection.send_command("show ip int b", strip_command=False, strip_prompt=False)
print output

print "########## Send Config From File ############"

# connection.send_config_from_file(config_file="/root/"+sw_ip+".txt")


###################################################################################

# CDP Neighbors


from netmiko import ConnectHandler
import time

connect_sw3 = ConnectHandler(**SW3)

connect_sw3.enable()

# prepend the command prompt to the result (used to identify the local host)
result = connect_sw3.find_prompt() + "\n"

# execute the show cdp neighbor detail command
# we increase the delay_factor for this command, because it take some time if many devices are seen by CDP
result += connect_sw3.send_command("show cdp neighbor detail", delay_factor=2)
print result
# close SSH connection
connect_sw3.disconnect()

###################################################################################


print "########## Sending Configuration to Router ############"

router_config = ["int lo0",  # list could be generated from file!
                 "ip add 4.4.4.4 255.255.255.0",
                 "int lo1",
                 "ip add 5.5.5.5 255.255.255.255"]
connect_sw2.enable()
output = connect_sw2.send_config_set(router_config)  # Netmiko will send "conf t"
print output
# connect_sw2.exit_config_mode()
