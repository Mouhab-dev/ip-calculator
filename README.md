# IP Calculator
IP Calculator is a Python Script to analyse a network given an ip address and subnet mask.

## Description
Given any valid IP address and subnet mask, use this calculator to determine the network ID, the first and last hosts in the network, and the broadcast address and number of hosts this network can provide.

## Usage
Run the script by executing the following command
```
python ip-calc.py
```
Then, Enter ip address and subnet mask when promoted

```
Please, Enter an Ip Address: 10.15.198.16
Please, Enter Subnet Mask: 255.255.128.0
```

## Test
```
C:\Users\'your username'> python ip-calc.py
Welcome to IP Calculator v1.0 by Mouhab-dev
Project Repo on Github: https://github.com/mouhab-dev/ip-calculator
Find me on Github: https://github.com/mouhab-dev

Please, Enter an IP Address: 10.15.198.16
Please, Enter Subnet Mask: 255.255.128.0
--------------------------------------------
CIDR: / 17
Network ID: 10.15.128.0
First Host Address: 10.15.128.1
Last Host Address: 10.15.255.254
Broadcast Address: 10.15.255.255
Total number of Hosts = 32766
```
