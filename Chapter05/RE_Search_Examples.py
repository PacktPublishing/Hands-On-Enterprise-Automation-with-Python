#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

# Example 1
import re

intf_ip = 'Gi0/0/0.911            10.200.101.242   YES NVRAM  up                    up'
match = re.search('10.200.101.242', intf_ip)

if match:
    print match.group()

# Example 2
import re

intf_ip = '''Gi0/0/0.705            10.103.17.5      YES NVRAM  up                    up      
Gi0/0/0.900            86.121.75.31  YES NVRAM  up                    up      
Gi0/0/0.911            10.200.101.242   YES NVRAM  up                    up      
Gi0/0/0.7000           unassigned      YES unset  up                    up '''
match = re.search("\d+\.\d+\.\d+\.\d+", intf_ip)

if match:
    print match.group()

# Example 3
import re

log_msg = 'Dec 20 12:11:47.417: %LINK-3-UPDOWN: Interface GigabitEthernet0/0/4, changed state to down'
match = re.search("(\w+\s\d+\s\S+):\s(\S+): Interface (\S+), changed state to (\S+)", log_msg)
if match:
    print match.groups()

# Example 4: Named group
import re

log_msg = 'Dec 20 12:11:47.417: %LINK-3-UPDOWN: Interface GigabitEthernet0/0/4, changed state to down'
match = re.search(
    "(?P<TIMESTAMP>\w+\s\d+\s\S+):\s(?P<EVENT>\S+): Interface (?P<INTF>\S+), changed state to (?P<STATE>\S+)", log_msg)
if match:
    print match.groups()

# Example 5-1: Searching for multiple Lines using re.search()

import re

show_ip_int_br_full = """
GigabitEthernet0/0/0        110.110.110.1   YES NVRAM  up                    up      
GigabitEthernet0/0/1        107.107.107.1   YES NVRAM  up                    up      
GigabitEthernet0/0/2        108.108.108.1   YES NVRAM  up                    up      
GigabitEthernet0/0/3        109.109.109.1   YES NVRAM  up                    up      
GigabitEthernet0/0/4   unassigned      YES NVRAM  up                    up      
GigabitEthernet0/0/5             10.131.71.1     YES NVRAM  up                    up      
GigabitEthernet0/0/6          10.37.102.225   YES NVRAM  up                    up      
GigabitEthernet0/1/0            unassigned      YES unset  up                    up      
GigabitEthernet0/1/1           57.234.66.28   YES manual up                    up      
GigabitEthernet0/1/2           10.10.99.70   YES manual up                    up      
GigabitEthernet0/1/3           unassigned      YES manual deleted               down    
GigabitEthernet0/1/4           192.168.200.1   YES manual up                    up      
GigabitEthernet0/1/5   unassigned      YES manual down                  down    
GigabitEthernet0/1/6         10.20.20.1      YES manual down                  down    
GigabitEthernet0/2/0         10.30.40.1      YES manual down                  down    
GigabitEthernet0/2/1         57.20.20.1      YES manual down                  down    

"""
for line in show_ip_int_br_full.split("\n"):
    match = re.search(r"(?P<interface>\w+\d\/\d\/\d)\s+(?P<ip>\d+.\d+.\d+.\d+)", line)
    if match:
        intf_ip = match.groupdict()
        if intf_ip["ip"].startswith("57"):
            print "Subnet is configured on " + intf_ip["interface"] + " and ip is " + intf_ip["ip"]

# Example 5-2: Searching for multiple Lines using re.findall()

import re
from pprint import pprint

show_ip_int_br_full = """
GigabitEthernet0/0/0        110.110.110.1   YES NVRAM  up                    up      
GigabitEthernet0/0/1        107.107.107.1   YES NVRAM  up                    up      
GigabitEthernet0/0/2        108.108.108.1   YES NVRAM  up                    up      
GigabitEthernet0/0/3        109.109.109.1   YES NVRAM  up                    up      
GigabitEthernet0/0/4   unassigned      YES NVRAM  up                    up      
GigabitEthernet0/0/5             10.131.71.1     YES NVRAM  up                    up      
GigabitEthernet0/0/6          10.37.102.225   YES NVRAM  up                    up      
GigabitEthernet0/1/0            unassigned      YES unset  up                    up      
GigabitEthernet0/1/1           57.234.66.28   YES manual up                    up      
GigabitEthernet0/1/2           10.10.99.70   YES manual up                    up      
GigabitEthernet0/1/3           unassigned      YES manual deleted               down    
GigabitEthernet0/1/4           192.168.200.1   YES manual up                    up      
GigabitEthernet0/1/5   unassigned      YES manual down                  down    
GigabitEthernet0/1/6         10.20.20.1      YES manual down                  down    
GigabitEthernet0/2/0         10.30.40.1      YES manual down                  down    
GigabitEthernet0/2/1         57.20.20.1      YES manual down                  down    
"""

intf_ip = re.findall(r"(?P<interface>\w+\d\/\d\/\d)\s+(?P<ip>57.\d+.\d+.\d+)", show_ip_int_br_full)
pprint(intf_ip)
