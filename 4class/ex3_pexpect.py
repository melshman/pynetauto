#!/usr/bin/env python
"""Use Pexpect to retrieve the output of 'show ip int brief'."""
from __future__ import print_function, unicode_literals
import pexpect
import time
from getpass import getpass


def login(ssh_conn):
    """Handle sending password."""
    password = getpass()

    ssh_conn.expect('ssword:')
    ssh_conn.sendline(password)
    ssh_conn.expect('#')


def find_prompt(ssh_conn):
    """
    Find the current prompt

    Pexpect is non-greedy which is problematic
    """
    ssh_conn.send('\n')
    time.sleep(1)
    ssh_conn.expect('#')
    prompt = ssh_conn.before + ssh_conn.after
    return prompt.strip()


def main():
    """Use Pexpect to retrieve the output of 'show ip int brief'."""
    try:
        ip_addr = raw_input("Enter IP address: ")
    except NameError:
        ip_addr = input("Enter IP address: ")
    username = 'pyclass'
    port = 22

    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
    ssh_conn.timeout = 6

    login(ssh_conn)
    prompt = find_prompt(ssh_conn)

    ssh_conn.sendline('terminal length 0')
    ssh_conn.expect(prompt)

    ssh_conn.sendline('show ip int brief')
    ssh_conn.expect(prompt)

    print('\n>>>>')
    print(ssh_conn.before.decode('utf-8', 'ignore'))
    print('>>>>\n')


if __name__ == "__main__":
    main()
