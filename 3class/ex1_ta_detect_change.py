#!/usr/bin/env python
"""
Using SNMPv3 create a script that detects router configuration changes.

If the running configuration has changed, then send an email notification to
yourself identifying the router that changed and the time that it changed.

In this exercise, you will possibly need to save data to an external file. Use
either JSON or YAML to save the data to an external file.
"""
from __future__ import print_function, unicode_literals

try:
    # PY2
    import cPickle as pickle
except ModuleNotFoundError:
    # PY3
    import pickle

import os.path
from datetime import datetime
from getpass import getpass
from collections import namedtuple

import json
import yaml

from snmp_helper import snmp_get_oid_v3, snmp_extract
from email_helper import send_mail
