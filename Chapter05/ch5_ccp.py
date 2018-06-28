__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

from ciscoconfparse import CiscoConfParse
from pprint import pprint

# EX1: Find All shutdown interfaces.

orig_config = CiscoConfParse(
    "/media/bassim/DATA/GoogleDrive/Packt/EnterpriseAutomationProject/Chapter5_Extract_useful_data_from_network_devices/Cisco_Config.txt")

shutdown_intfs = orig_config.find_parents_w_child(parentspec=r"^interface", childspec='shutdown')
pprint(shutdown_intfs)

# EX2: Does this configuration has a router

from ciscoconfparse import CiscoConfParse
from pprint import pprint

orig_config = CiscoConfParse(
    "/media/bassim/DATA/GoogleDrive/Packt/EnterpriseAutomationProject/Chapter5_Extract_useful_data_from_network_devices/Cisco_Config.txt")

check_router = orig_config.has_line_with(r"^router")
pprint(check_router)

# --
from ciscoconfparse import CiscoConfParse

orig_config = CiscoConfParse(
    "/media/bassim/DATA/GoogleDrive/Packt/EnterpriseAutomationProject/Chapter5_Extract_useful_data_from_network_devices/Cisco_Config.txt")
print orig_config.has_line_with("^aaa new-model")

# EX3: Does OSPF enabled? if yes then find advertised networks

from ciscoconfparse import CiscoConfParse
from pprint import pprint

orig_config = CiscoConfParse(
    "/media/bassim/DATA/GoogleDrive/Packt/EnterpriseAutomationProject/Chapter5_Extract_useful_data_from_network_devices/Cisco_Config.txt")

if orig_config.has_line_with(r"^router ospf"):
    ospf_config = orig_config.find_all_children(r"^router ospf")
    networks = []
    for line in ospf_config:
        if 'network' in line:
            networks.append(line.split(" ")[2])

    print networks

orig_config.find
