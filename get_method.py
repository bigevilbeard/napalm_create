#!/usr/bin/env python

##############################################################
# Introducation to Napalm
# Author: Stuart Clark <stuaclar@cisco.com>
#
# Demo for Devnet Create 2018 - https://github.com/bigevilbeard/napalm_create
##############################################################

import json
from napalm import get_network_driver

driver = get_network_driver('ios')
device = driver(hostname='10.10.20.48', 
	            username='cisco', 
	            password='cisco_1234!')

device.open()
print 'Napalm Is Running........'
get_method = dir(device)


# print get_method
print(json.dumps(get_method, sort_keys=True, indent=4))


device.close()