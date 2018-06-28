#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

from scapy.layers.inet import *
from pprint import pprint

pkts = PcapReader("/root/ftp_data.pcap")  # should be in wireshark-tcpdump format

p_out = []

for pkt in pkts:
    new_pkt = pkt.payload

    try:
        new_pkt[IP].src = "10.10.88.100"
        new_pkt[IP].dst = "10.10.88.1"
        del (new_pkt[IP].chksum)
        del (new_pkt[TCP].chksum)
    except:
        pass

    pprint(new_pkt.show())
    p_out.append(new_pkt)
send(PacketList(p_out), iface="eth0")
