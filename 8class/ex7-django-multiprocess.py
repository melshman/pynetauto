#!/user/bin/env python

from __future__ import print_function, unicode_literals

from getpass import getpass
from pprint import pprint

from datetime import datetime
from netmiko import ConnectHandler

import django
django.setup()

from net_system.models import NetworkDevice

from multiprocessing import Process, current_process, Queue

'''

6. Use threads and Netmiko to execute 'show version' 
on each device in the database. Calculate the amount 
of time required to do this. What is the difference in 
time between executing 'show version' sequentially versus 
using threads?

'''


def show_version(a_device, q):
    """Execute show version command using Netmiko."""
    output_dict = {}
    creds = a_device.credentials
    remote_conn = ConnectHandler(device_type=a_device.device_type,
                                 ip=a_device.ip_address,
                                 username=creds.username,
                                 password=creds.password,
                                 port=a_device.port, secret='')
    
    output = ('#' * 80) + "\n" 
    output += remote_conn.send_command_expect("show version") + "\n"
    output = ('#' * 80) + "\n" 

    output_dict[a_device.device_name] = output
    q.put(output_dict)

def main():
    """
    Use Netmiko to connect to each of the devices in the database. Execute
    'show version' on each device.
    """
    start_time = datetime.now()
    devices = NetworkDevice.objects.all()
    procs = []
    q = Queue(maxsize=20)

    for a_device in devices:
        my_proc = Process(target=show_version, args=(a_device, q))
        my_proc.start()
        procs.append(my_proc)
    
    #  Make sure all processes completed
    for a_proc in procs:
        print(a_proc)
        a_proc.join()

    while not q.empty():
        my_dict = q.get()
        for k,v in my_dict.iteritems():
            print(k)
            print(v)

    elapsed_time = datetime.now() - start_time
    print("Elapsed time: {}".format(elapsed_time))


if __name__ == "__main__":
    main()
