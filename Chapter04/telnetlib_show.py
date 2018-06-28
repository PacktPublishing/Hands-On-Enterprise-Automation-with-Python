__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

import telnetlib

username = "admin"
password = "access123"
enable_password = "access123"
cnx = telnetlib.Telnet(host="10.10.88.110")
cnx.read_until("Username:")
cnx.write(username + "\n")
cnx.read_until("Password:")
cnx.write(password + "\n")
cnx.read_until(">")
cnx.write("en" + "\n")
cnx.read_until("Password:")
cnx.write(enable_password + "\n")
cnx.read_until("#")
cnx.write("show ip int b" + "\n")
output = cnx.read_until("#")
cleaned_output = output.replace("show ip int b", "").replace("R1#", "")
print cleaned_output

exit()

# Ask users to enter the username and password

import telnetlib
import time

username = raw_input("please Enter your username:")
password = raw_input("please Enter your password:")
enable_password = raw_input("please Enter your enable password:")
cnx = telnetlib.Telnet(host="10.10.88.110")
# cnx.set_debuglevel(1000)
cnx.read_until("Username:")
cnx.write(username + "\n")
cnx.read_until("Password:")
cnx.write(password + "\n")
cnx.read_until(">")
cnx.write("en" + "\n")
cnx.read_until("Password:")
cnx.write(enable_password + "\n")
cnx.read_until("#")
cnx.write("show ip int b" + "\n")
time.sleep(5)
output = cnx.read_until("#")
print output

# Hide the password

import telnetlib
import time
import getpass

username = raw_input("please Enter your username:")
password = getpass.getpass("please Enter your password:")
enable_password = getpass.getpass("please Enter your enable password:")
cnx = telnetlib.Telnet(host="10.10.88.110")
# cnx.set_debuglevel(1000)
cnx.read_until("Username:")
cnx.write(username + "\n")
cnx.read_until("Password:")
cnx.write(password + "\n")
cnx.read_until(">")
cnx.write("en" + "\n")
cnx.read_until("Password:")
cnx.write(enable_password + "\n")
cnx.read_until("#")
cnx.write("show ip int b" + "\n")
time.sleep(5)
output = cnx.read_until("#")
print output

hosts = ["10.10.88.110", "10.10.88.111"]
username = raw_input("Please Enter your username:")
password = getpass.getpass("Please Enter your Password:")
enable_password = getpass.getpass("Please Enter your Enable Password:")
for ip_address in hosts:
    cnx = telnetlib.Telnet(ip_address)
    cnx.read_until("Username:")
    cnx.write(username + "\n")
    cnx.read_until("Password:")
    cnx.write(password + "\n")
    cnx.read_until(">")
    cnx.write("en" + "\n")
    cnx.read_until("Password:")
    cnx.write(enable_password + "\n")
    cnx.read_until("#")
    cnx.write("show ip int b" + "\n")
    # time.sleep(1)
    # cnx.read_until("#")
    output = cnx.read_until("#")  # You need to print the variable

    print "\n#################### EXECUTING COMMAND ON {0} ###############################".format(ip_address)

    print output.replace("show ip int b", "")

    cnx.close()
