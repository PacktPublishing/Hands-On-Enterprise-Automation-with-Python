#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

from keystoneauth1.identity import v3
from keystoneauth1 import session
import neutronclient.neutron.client as neuclient

auth = v3.Password(auth_url="http://10.10.10.150:5000/v3",
                   username="admin",
                   password="access123",
                   project_name="admin",
                   user_domain_name="Default",
                   project_domain_name="Default")

sess = session.Session(auth=auth, verify=False)

neutron = neuclient.Client(2, session=sess)

# Create Network

body_network = {'name': 'python_network',
                'admin_state_up': True,
                'port_security_enabled': False,
                'shared': True,
                # 'provider:network_type': 'vlan|vxlan',
                # 'provider:segmentation_id': 29
                # 'provider:physical_network': None,
                # 'mtu': 1450,
                }
neutron.create_network({'network': body_network})
network_id = neutron.list_networks(name="python_network")["networks"][0]["id"]

# Create Subnet

body_subnet = {
    "subnets": [
        {
            "name": "python_network_subnet",
            "network_id": network_id,
            "enable_dhcp": True,
            "cidr": "172.16.128.0/24",
            "gateway_ip": "172.16.128.1",
            "allocation_pools": [
                {
                    "start": "172.16.128.10",
                    "end": "172.16.128.100"
                }
            ],
            "ip_version": 4,
        }
    ]
}
neutron.create_subnet(body=body_subnet)
