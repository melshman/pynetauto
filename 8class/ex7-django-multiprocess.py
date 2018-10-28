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


def show_version(a_device):
    """Execute show version command using Netmiko."""
    creds = a_device.credentials
    remote_conn = ConnectHandler(device_type=a_device.device_type,
                                 ip=a_device.ip_address,
                                 username=creds.username,
                                 password=creds.password,
                                 port=a_device.port, secret='')
    print()
    print('#' * 80)
    print(remote_conn.send_command_expect("show version"))
    print('#' * 80)
    print()


def main():
    """
    Use Netmiko to connect to each of the devices in the database. Execute
    'show version' on each device.
    """
    start_time = datetime.now()
    devices = NetworkDevice.objects.all()
    procs = []

    for a_device in devices:
        my_proc = Process(target=show_version, args=(a_device,))
        my_proc.start()
        procs.append(my_proc)
    
    for a_proc in procs:
        if some_thread != main_thread:
            print(a_proc)
            a_proc.join()

    elapsed_time = datetime.now() - start_time
    print("Elapsed time: {}".format(elapsed_time))


if __name__ == "__main__":
    main()
