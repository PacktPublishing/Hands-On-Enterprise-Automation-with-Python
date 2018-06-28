#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

from scapy.layers.inet import *
from pprint import pprint

pkts = PcapReader("/root/ftp_data.pcap")  # should be in wireshark-tcpdump format

ftp_data = b""
for pkt in pkts:
    try:
        ftp_data += pkt.get_layer(Raw).load
    except:
        pass
