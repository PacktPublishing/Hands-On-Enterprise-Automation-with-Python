#!/usr/bin/python

__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

from jinja2 import Template

template = Template('''
hostname {{hostname}}

aaa new-model
aaa session-id unique
aaa authentication login default local
aaa authorization exec default local none
vtp mode transparent
vlan 10,20,30,40,50,60,70,80,90,100,200

int {{mgmt_intf}}
 no switchport
 no shut
 ip address {{mgmt_ip}} {{mgmt_subnet}}
''')

sw1 = {'hostname': 'switch1', 'mgmt_intf': 'gig0/0', 'mgmt_ip': '10.10.88.111', 'mgmt_subnet': '255.255.255.0'}
print(template.render(sw1))
