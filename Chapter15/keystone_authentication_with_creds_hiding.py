#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

from keystoneauth1.identity import v3
from keystoneauth1 import session
import ConfigParser

config = ConfigParser.ConfigParser()
config.read(
    "/media/bassim/DATA/GoogleDrive/Packt/EnterpriseAutomationProject/Chapter15_Interacting_with_openstack_API/creds.ini")
auth = v3.Password(auth_url=config.get("os_creds", "auth_url"),
                   username=config.get("os_creds", "username"),
                   password=config.get("os_creds", "password"),
                   project_name=config.get("os_creds", "project_name"),
                   user_domain_name=config.get("os_creds", "user_domain_name"),
                   project_domain_name=config.get("os_creds", "project_domain_name"))
sess = session.Session(auth=auth, verify=False)
print(sess)
