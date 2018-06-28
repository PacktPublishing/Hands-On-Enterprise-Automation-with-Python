#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

from keystoneauth1.identity import v3
from keystoneauth1 import session

auth = v3.Password(auth_url="http://10.10.10.150:5000/v3",
                   username="admin",
                   password="access123",
                   project_name="admin",
                   user_domain_name="Default",
                   project_domain_name="Default")
sess = session.Session(auth=auth, verify=False)
print(sess)
