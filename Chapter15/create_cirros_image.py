#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

from keystoneauth1.identity import v3
from keystoneauth1 import session
from glanceclient import client as gclient
from pprint import pprint

auth = v3.Password(auth_url="http://10.10.10.150:5000/v3",
                   username="admin",
                   password="access123",
                   project_name="admin",
                   user_domain_name="Default",
                   project_domain_name="Default")

sess = session.Session(auth=auth, verify=False)

# Upload the image to the Glance


glance = gclient.Client('2', session=sess)

image = glance.images.create(name="CirrosImage",
                             container_format='bare',
                             disk_format='qcow2',
                             )

glance.images.upload(image.id, open('/root/cirros-0.4.0-x86_64-disk.img', 'rb'))

print("===============================Image Details===============================")
for image in glance.images.list(name="CirrosImage"):
    pprint(image)
