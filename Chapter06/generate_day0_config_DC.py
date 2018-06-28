#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

import yaml
from jinja2 import Template

with open(
        '/media/bassim/DATA/GoogleDrive/Packt/EnterpriseAutomationProject/Chapter6_Configuration_generator_with_python_and_jinja2/network_dc.yml',
        'r') as yaml_file:
    yaml_data = yaml.load(yaml_file)

router_day0_template = Template("""
hostname {{hostname}}
int {{mgmt_intf}}
  no shutdown
  ip add {{mgmt_ip}} {{mgmt_subnet}}

lldp run

ip domain-name EnterpriseAutomation.net
ip ssh version 2
ip scp server enable
crypto key generate rsa general-keys modulus 1024

snmp-server community public RW
snmp-server trap link ietf
snmp-server enable traps snmp linkdown linkup
snmp-server enable traps syslog
snmp-server manager

logging history debugging
logging snmp-trap emergencies
logging snmp-trap alerts
logging snmp-trap critical
logging snmp-trap errors
logging snmp-trap warnings
logging snmp-trap notifications
logging snmp-trap informational
logging snmp-trap debugging

""")

switch_day0_template = Template("""
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

snmp-server community public RW
snmp-server trap link ietf
snmp-server enable traps snmp linkdown linkup
snmp-server enable traps syslog
snmp-server manager

logging history debugging
logging snmp-trap emergencies
logging snmp-trap alerts
logging snmp-trap critical
logging snmp-trap errors
logging snmp-trap warnings
logging snmp-trap notifications
logging snmp-trap informational
logging snmp-trap debugging

""")

for device, config in yaml_data['dc1'].iteritems():
    if config['device_template'] == "vIOSL2_Template":
        device_template = switch_day0_template
    elif config['device_template'] == "vIOSL3_Template":
        device_template = router_day0_template

    print("rendering now device {0}".format(device))
    Day0_device_config = device_template.render(config)

    print Day0_device_config
    print "=" * 30
