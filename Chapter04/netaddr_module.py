#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

from netaddr import IPNetwork, IPAddress


def check_ip_address(ipaddr):
    ip_attributes = []
    ipaddress = IPAddress(ipaddr)

    if ipaddress.is_private():
        ip_attributes.append("IP Address is Private")

    else:
        ip_attributes.append("IP Address is public")

    if ipaddress.is_unicast():
        ip_attributes.append("IP Address is unicast")
    elif ipaddress.is_multicast():
        ip_attributes.append("IP Address is multicast")

    if ipaddress.is_loopback():
        ip_attributes.append("IP Address is loopback")

    return "\n".join(ip_attributes)


def operate_on_ip_network(ipnet):
    net_attributes = []
    net = IPNetwork(ipnet)

    net_attributes.append("Network IP Address is " + str(net.network) + " and Network Mask is " + str(net.netmask))

    net_attributes.append("The Broadcast is " + str(net.broadcast))

    net_attributes.append("IP Version is " + str(net.version))
    net_attributes.append("Information known about this network is " + str(net.info))

    net_attributes.append("The IPv6 representation is " + str(net.ipv6()))

    net_attributes.append("The Network size is " + str(net.size))

    net_attributes.append("Generating a list of ip addresses inside the subnet")

    for ip in net:
        net_attributes.append("\t" + str(ip))

    return "\n".join(net_attributes)


ipaddr = raw_input("Please Enter the IP Address: ")
print check_ip_address(ipaddr)

ipnet = raw_input("Please Enter the IP Network: ")
print operate_on_ip_network(ipnet)
