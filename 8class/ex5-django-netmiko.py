#!/user/bin/env python

from __future__ import print_function, unicode_literals

from getpass import getpass
from pprint import pprint

from datetime import datetime
from netmiko import ConnectHandler

import django
django.setup()

from net_system.models import NetworkDevice     # noqa


'''

5. Use Netmiko to connect to each of the devices in the database. 
Execute 'show version' on each device. Calculate the amount of time 
required to do this. 

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
    for a_device in devices:
        show_version(a_device)

    elapsed_time = datetime.now() - start_time
    print("Elapsed time: {}".format(elapsed_time))


if __name__ == "__main__":
    main()
