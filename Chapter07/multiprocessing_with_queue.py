#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

import multiprocessing
from netmiko import ConnectHandler
from devices import R1, SW1, SW2, SW3, SW4
from pprint import pprint

nodes = [R1, SW1, SW2, SW3, SW4]


def connect_to_dev(device, mp_queue):
    dev_id = device['ip']
    return_data = {}

    net_connect = ConnectHandler(**device)

    output = net_connect.send_command("show run")

    return_data[dev_id] = output
    print("Adding the result to the multiprocess queue")
    mp_queue.put(return_data)


mp_queue = multiprocessing.Queue()
processes = []

for device in nodes:
    p = multiprocessing.Process(target=connect_to_dev, args=[device, mp_queue])
    print("Adding Process to the list")
    processes.append(p)
    p.start()

for p in processes:
    print("Joining the finished process to the main truck")
    p.join()

results = []
for p in processes:
    print("Moving the result from the queue to the results list")
    results.append(mp_queue.get())

pprint(results)
