#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

from keystoneauth1.identity import v3
from keystoneauth1 import session

from novaclient import client as nclient
import neutronclient.neutron.client as neuclient

from glanceclient import client as gclient

import time

auth = v3.Password(auth_url="http://10.10.10.150:5000/v3",
                   username="admin",
                   password="access123",
                   project_name="admin",
                   user_domain_name="Default",
                   project_domain_name="Default")

sess = session.Session(auth=auth, verify=False)

# Initialize Clients

glance = gclient.Client('2', session=sess)
nova = nclient.Client(2.1, session=sess)
neutron = neuclient.Client(2, session=sess)

## Assign Flavor
print("=================Assigning Flavor=================")

instance_flavor = nova.flavors.find(name="m1.small")

## Create Image

print("=================Uploading Image=================")

image = glance.images.create(name="CirrosImage",
                             container_format='bare',
                             disk_format='qcow2',
                             )

glance.images.upload(image.id, open('/root/cirros-0.4.0-x86_64-disk.img', 'rb'))

# Create Network

print("=================Create Network=================")

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

print("=================Create Subnet=================")

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

## Launch the Instance

print("=================Launch The Instance=================")

image_name = glance.images.get(image.id)

network1 = neutron.list_networks(name="python_network")
instance_nics = [{'net-id': network1["networks"][0]["id"]}]

server = nova.servers.create(name="python-instance",
                             image=image_name.id,
                             flavor=instance_flavor.id,
                             nics=instance_nics, )
status = server.status
while status == 'BUILD':
    print("Sleeping 5 seconds till the server status is changed")
    time.sleep(5)
    instance = nova.servers.get(server.id)
    status = instance.status
    print(status)
print("Current Status is: {0}".format(status))
