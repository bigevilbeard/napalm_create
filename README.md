#  WS24 Intro to Napalm Devnet Create 2018

## BYOD Requirements
This workshop introduces you to the network automation python module Naplam, and how it can be used for network automation.  

## Objectives

This workshops gets you up-and-running with NAPALM in a Devnet Sandbox environment so you can see it in action in under an hour. We’ll cover the following:

* What is Napalm
* Installing the required tools
* Napalm Command Line Tool
* Manually applying configuration to the device using NAPALM
* Driving NAPALM through Python code


## Prerequisites

For this lab an ssh client is required to connect to the devbox. Using Mac/Linux directly use the OS native SSH client. For connecting using an SSH client such as PuTTY.

```
ssh root@10.10.20.20 / password cisco123

```
Putty Dowload link 
```
https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html 

```


# Create a new directory

```
mkdir napalm
```

# Clone the Repo

```
git clone https://github.com/bigevilbeard/napalm_create.git
```

# Installing Napalm

When installing Napalm installed the latest version 2.X as there were fundamental changes that happened between Naplm 1.X and 2.X.
You can install napalm with pip:

```
pip install -r requirements.txt
```

```
 STUACLAR-M-R6EU:$ pip install napalm
Collecting napalm
  Downloading napalm-2.3.0.tar.gz (147kB)
    100% |████████████████████████████████| 153kB 1.7MB/s
Collecting future (from napalm)
  Downloading future-0.16.0.tar.gz (824kB)
    100% |████████████████████████████████| 829kB 1.1MB/s
Collecting jtextfsm (from napalm)
  Downloading jtextfsm-0.3.1.tar.gz
Collecting jinja2 (from napalm)
  Downloading Jinja2-2.10-py2.py3-none-any.whl (126kB)
    100% |████████████████████████████████| 133kB 2.3MB/s
Collecting netaddr (from napalm)
  Downloading netaddr-0.7.19-py2.py3-none-any.whl (1.6MB)
    100% |████████████████████████████████| 1.6MB 714kB/s
Collecting pyYAML (from napalm)
  Downloading PyYAML-3.12.tar.gz (253kB)
    100% |████████████████████████████████| 256kB 2.4MB/s
Collecting pyeapi (from napalm)
  Downloading pyeapi-0.8.2.tar.gz (133kB)
    100% |████████████████████████████████| 143kB 4.2MB/s
Collecting netmiko>=1.4.3 (from napalm)
  Downloading netmiko-2.1.0.tar.gz (70kB)
    100% |████████████████████████████████| 71kB 2.4MB/s
Collecting pyIOSXR>=0.51 (from napalm)
  Downloading pyIOSXR-0.52.tar.gz
Collecting junos-eznc>=2.1.5 (from napalm)
  Downloading junos_eznc-2.1.7-py2.py3-none-any.whl (150kB)
    100% |████████████████████████████████| 153kB 4.6MB/s
Collecting pynxos (from napalm)
  Downloading pynxos-0.0.3.tar.gz
Collecting scp (from napalm)
  Downloading scp-0.10.2-py2.py3-none-any.whl
Collecting MarkupSafe>=0.23 (from jinja2->napalm)
  Downloading MarkupSafe-1.0.tar.gz
Collecting paramiko>=2.0.0 (from netmiko>=1.4.3->napalm)
  Downloading paramiko-2.4.0-py2.py3-none-any.whl (192kB)
    100% |████████████████████████████████| 194kB 2.5MB/s
Collecting pyserial (from netmiko>=1.4.3->napalm)
  Downloading pyserial-3.4-py2.py3-none-any.whl (193kB)
    100% |████████████████████████████████| 194kB 4.1MB/s
Collecting textfsm (from netmiko>=1.4.3->napalm)
  Downloading textfsm-0.3.2.tar.gz
Collecting lxml>=3.2.4 (from pyIOSXR>=0.51->napalm)
  Downloading lxml-4.1.1-cp27-cp27m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl (8.7MB)
    100% |████████████████████████████████| 8.7MB 155kB/s
Collecting ncclient>=0.5.3 (from junos-eznc>=2.1.5->napalm)
  Downloading ncclient-0.5.3.tar.gz (63kB)
    100% |████████████████████████████████| 71kB 3.9MB/s
Collecting six (from junos-eznc>=2.1.5->napalm)
  Downloading six-1.11.0-py2.py3-none-any.whl
Collecting requests>=2.7.0 (from pynxos->napalm)
  Downloading requests-2.18.4-py2.py3-none-any.whl (88kB)
    100% |████████████████████████████████| 92kB 4.1MB/s
Collecting pyasn1>=0.1.7 (from paramiko>=2.0.0->netmiko>=1.4.3->napalm)
  Downloading pyasn1-0.4.2-py2.py3-none-any.whl (71kB)
    100% |████████████████████████████████| 71kB 3.5MB/s
Collecting bcrypt>=3.1.3 (from paramiko>=2.0.0->netmiko>=1.4.3->napalm)
  Downloading bcrypt-3.1.4-cp27-cp27m-macosx_10_6_intel.whl (51kB)
    100% |████████████████████████████████| 61kB 8.7MB/s
Collecting cryptography>=1.5 (from paramiko>=2.0.0->netmiko>=1.4.3->napalm)
  Downloading cryptography-2.1.4-cp27-cp27m-macosx_10_6_intel.whl (1.5MB)
    100% |████████████████████████████████| 1.5MB 884kB/s
Collecting pynacl>=1.0.1 (from paramiko>=2.0.0->netmiko>=1.4.3->napalm)
  Downloading PyNaCl-1.2.1-cp27-cp27m-macosx_10_6_intel.whl (243kB)
    100% |████████████████████████████████| 245kB 2.3MB/s
Requirement already satisfied: setuptools>0.6 in ./venv/lib/python2.7/site-packages (from ncclient>=0.5.3->junos-eznc>=2.1.5->napalm)
Collecting certifi>=2017.4.17 (from requests>=2.7.0->pynxos->napalm)
  Downloading certifi-2018.1.18-py2.py3-none-any.whl (151kB)
    100% |████████████████████████████████| 153kB 3.7MB/s
Collecting chardet<3.1.0,>=3.0.2 (from requests>=2.7.0->pynxos->napalm)
  Downloading chardet-3.0.4-py2.py3-none-any.whl (133kB)
    100% |████████████████████████████████| 143kB 5.7MB/s
Collecting idna<2.7,>=2.5 (from requests>=2.7.0->pynxos->napalm)
  Downloading idna-2.6-py2.py3-none-any.whl (56kB)
    100% |████████████████████████████████| 61kB 3.3MB/s
Collecting urllib3<1.23,>=1.21.1 (from requests>=2.7.0->pynxos->napalm)
  Downloading urllib3-1.22-py2.py3-none-any.whl (132kB)
    100% |████████████████████████████████| 133kB 5.7MB/s
Collecting cffi>=1.1 (from bcrypt>=3.1.3->paramiko>=2.0.0->netmiko>=1.4.3->napalm)
  Downloading cffi-1.11.5-cp27-cp27m-macosx_10_6_intel.whl (238kB)
    100% |████████████████████████████████| 245kB 2.5MB/s
Collecting enum34; python_version < "3" (from cryptography>=1.5->paramiko>=2.0.0->netmiko>=1.4.3->napalm)
  Downloading enum34-1.1.6-py2-none-any.whl
Collecting asn1crypto>=0.21.0 (from cryptography>=1.5->paramiko>=2.0.0->netmiko>=1.4.3->napalm)
  Downloading asn1crypto-0.24.0-py2.py3-none-any.whl (101kB)
    100% |████████████████████████████████| 102kB 2.9MB/s
Collecting ipaddress; python_version < "3" (from cryptography>=1.5->paramiko>=2.0.0->netmiko>=1.4.3->napalm)
  Downloading ipaddress-1.0.19.tar.gz
Collecting pycparser (from cffi>=1.1->bcrypt>=3.1.3->paramiko>=2.0.0->netmiko>=1.4.3->napalm)
  Downloading pycparser-2.18.tar.gz (245kB)
    100% |████████████████████████████████| 256kB 2.9MB/s
Building wheels for collected packages: napalm, future, jtextfsm, pyYAML, pyeapi, netmiko, pyIOSXR, pynxos, MarkupSafe, textfsm, ncclient, ipaddress, pycparser
  Running setup.py bdist_wheel for napalm ... done
  Stored in directory: /Users/stuaclar/Library/Caches/pip/wheels/4a/ef/3c/ef3eeb561a9dfa53ce530f964d8c3b2047d27b98d4879a7c6d
  Running setup.py bdist_wheel for future ... done
  Stored in directory: /Users/stuaclar/Library/Caches/pip/wheels/c2/50/7c/0d83b4baac4f63ff7a765bd16390d2ab43c93587fac9d6017a
  Running setup.py bdist_wheel for jtextfsm ... done
  Stored in directory: /Users/stuaclar/Library/Caches/pip/wheels/6b/22/6b/b3d6deb6364579238b8017909729b5c1bad7fcd8331b4067c4
  Running setup.py bdist_wheel for pyYAML ... done
  Stored in directory: /Users/stuaclar/Library/Caches/pip/wheels/2c/f7/79/13f3a12cd723892437c0cfbde1230ab4d82947ff7b3839a4fc
  Running setup.py bdist_wheel for pyeapi ... done
  Stored in directory: /Users/stuaclar/Library/Caches/pip/wheels/98/a6/be/1910f4f4beec81424b4ede48457b0ae36e6f440d66d51f57bb
  Running setup.py bdist_wheel for netmiko ... done
  Stored in directory: /Users/stuaclar/Library/Caches/pip/wheels/c6/f0/68/2ee16b66bc1083a2f80f1a3b475c2d8c20cfc0908785b1f841
  Running setup.py bdist_wheel for pyIOSXR ... done
  Stored in directory: /Users/stuaclar/Library/Caches/pip/wheels/90/a8/e4/875d89a75cbb48d65af113c5e2927b50268da7cd8f8250443f
  Running setup.py bdist_wheel for pynxos ... done
  Stored in directory: /Users/stuaclar/Library/Caches/pip/wheels/84/ff/be/f0989593202f198e5872d1258df4956d9f6646d72fe22c2da1
  Running setup.py bdist_wheel for MarkupSafe ... done
  Stored in directory: /Users/stuaclar/Library/Caches/pip/wheels/88/a7/30/e39a54a87bcbe25308fa3ca64e8ddc75d9b3e5afa21ee32d57
  Running setup.py bdist_wheel for textfsm ... done
  Stored in directory: /Users/stuaclar/Library/Caches/pip/wheels/92/7f/36/3dc4b8c2606a92d479b4f986c9deef9c0b293718dd83ace07c
  Running setup.py bdist_wheel for ncclient ... done
  Stored in directory: /Users/stuaclar/Library/Caches/pip/wheels/86/30/68/153d65b60834981c1960737f3f2de488574ba5355fe1329558
  Running setup.py bdist_wheel for ipaddress ... done
  Stored in directory: /Users/stuaclar/Library/Caches/pip/wheels/d7/6b/69/666188e8101897abb2e115d408d139a372bdf6bfa7abb5aef5
  Running setup.py bdist_wheel for pycparser ... done
  Stored in directory: /Users/stuaclar/Library/Caches/pip/wheels/95/14/9a/5e7b9024459d2a6600aaa64e0ba485325aff7a9ac7489db1b6
Successfully built napalm future jtextfsm pyYAML pyeapi netmiko pyIOSXR pynxos MarkupSafe textfsm ncclient ipaddress pycparser
Installing collected packages: future, jtextfsm, MarkupSafe, jinja2, netaddr, pyYAML, pyeapi, pyasn1, six, pycparser, cffi, bcrypt, enum34, idna, asn1crypto, ipaddress, cryptography, pynacl, paramiko, scp, pyserial, textfsm, netmiko, lxml, pyIOSXR, ncclient, junos-eznc, certifi, chardet, urllib3, requests, pynxos, napalm
Successfully installed MarkupSafe-1.0 asn1crypto-0.24.0 bcrypt-3.1.4 certifi-2018.1.18 cffi-1.11.5 chardet-3.0.4 cryptography-2.1.4 enum34-1.1.6 future-0.16.0 idna-2.6 ipaddress-1.0.19 jinja2-2.10 jtextfsm-0.3.1 junos-eznc-2.1.7 lxml-4.1.1 napalm-2.3.0 ncclient-0.5.3 netaddr-0.7.19 netmiko-2.1.0 paramiko-2.4.0 pyIOSXR-0.52 pyYAML-3.12 pyasn1-0.4.2 pycparser-2.18 pyeapi-0.8.2 pynacl-1.2.1 pynxos-0.0.3 pyserial-3.4 requests-2.18.4 scp-0.10.2 six-1.11.0 textfsm-0.3.2 urllib3-1.22
```

```
pip show napalm
Name: napalm
Version: 2.3.0
Summary: Network Automation and Programmability Abstraction Layer with Multivendor support
Home-page: https://github.com/napalm-automation/napalm
Author: David Barroso, Kirk Byers, Mircea Ulinic
Author-email: dbarrosop@dravetech.com, ping@mirceaulinic.net, ktbyers@twb-tech.com
License: UNKNOWN
Location: /root/venv/python2/lib/python2.7/site-packages
Requires: jinja2, future, junos-eznc, pyeapi, netaddr, pyYAML, pyIOSXR, jtextfsm, netmiko, pynxos, scp
```



# Napalm Help

```
napalm --help
usage: napalm [-h] [--user USER] [--password PASSWORD] --vendor VENDOR
              [--optional_args OPTIONAL_ARGS] [--debug]
              hostname {configure,call,validate} ...

Command line tool to handle configuration on devices using NAPALM.The script
will print the diff on the screen

positional arguments:
  hostname              Host where you want to deploy the configuration.

optional arguments:
  -h, --help            show this help message and exit
  --user USER, -u USER  User for authenticating to the host. Default: user
                        running the script.
  --password PASSWORD, -p PASSWORD
                        Password for authenticating to the host.If you do not
                        provide a password in the CLI you will be prompted.
  --vendor VENDOR, -v VENDOR
                        Host Operating System.
  --optional_args OPTIONAL_ARGS, -o OPTIONAL_ARGS
                        String with comma separated key=value pairs passed via
                        optional_args to the driver.
  --debug               Enables debug mode; more verbosity.

actions:
  {configure,call,validate}
    configure           Perform a configuration operation
    call                Call a napalm method
    validate            Validate configuration/state

Automate all the things!!!
```







