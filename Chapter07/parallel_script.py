#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

from netmiko import ConnectHandler
from devices import R1, SW1, SW2, SW3, SW4
import multiprocessing as mp
from datetime import datetime

nodes = [R1, SW1, SW2, SW3, SW4]


def connect_to_dev(device):
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show run")
    print output


processes = []

start_time = datetime.now()
for device in nodes:
    print("Adding Process to the list")
    processes.append(mp.Process(target=connect_to_dev, args=[device]))

print("Spawning the Process")
for p in processes:
    p.start()

print("Joining the finished process to the main truck")
for p in processes:
    p.join()

end_time = datetime.now()
print("Script Execution tooks {}".format(end_time - start_time))
