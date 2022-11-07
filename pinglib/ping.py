""" Ping IP addresses and return if they are accessible or not
This script contains following functions:

1) ping()
Allows user to pass in list of IP addresses, retry attempts and list of IP addresses to exclude rom pinging
and returns a list boolean values for IP addresses based on their accessibility (i.e. True if accessible and False if inaccessible )

2) generateExcludeList()
Prompts user to input space separated host digits to exclude from pinging process and returns a set of hosts that need to be
excluded from pinging

3) toExclude
Updates result list for the hosts that are present in the exclude list. This function is called in the ping() function.

Tests for this script are written in pinglib/tests/test_ping.py file
"""

import ipaddress
import multiprocessing
import subprocess
import platform
from multiprocessing import Queue
import time
import os

def pingResult(queue: Queue, ip_range: list, retries: int, result: list, excludeSet: set = None) -> list:
    """
    Function to ping IP Addresses in a range

    :param queue <ultiprocessing.Queue>: multiprocessing.Queue object to store result to be retrieved in multiprocessing
    :param ip_range <list>: list of IP Addresses
    :param retries <int>: number of ping retry attempts
    :param result <list>: list of zeros to store ping result
    :param excludeSet <set>: set of hosts to exclude from pinging

    :return result <list[bool]>: list of boolean ping results
    """

    # If host is declared to be excluded, update result as pinging will be skipped
    if excludeSet is not None:
        for idx in excludeSet:
            toExclude(idx, ip_range, result)
    

    # Ping IP addresses in 
    for idx in range(len(ip_range)):
        
        # If host is specified in exclude list, skip ping
        if excludeSet is not None and idx in excludeSet:
            continue

        #else:
        ip = ip_range[idx]

        # Option for the number of packets as a function of
        param = '-n' if platform.system().lower()=='windows' else '-C'

        # Building the command for Windows, Linux and Darwin. Ex: "ping -C 1 192.168.x.y"
        if param == '-n':
            command = ['ping', param, str(retries), '-w', '100', ip]
        else:
            command = ['fping', param, str(retries), '-t', '1000', ip]

        # Run ping command
        pingCmdReturn = ping(command)
        #print(pingCmd.stdout.decode())


        # Update result based on subprocess output
        if pingCmdReturn == 0:
            result[idx] = True
        else:
            result[idx] = False
    
    # Put result in a queue in order to retrieve it while multiprocessing
    queue.put(result)

    return result

# Ping IPs
def ping(command):
    pingCmd = subprocess.run(command, capture_output=True)
    print(pingCmd.stdout.decode())
    return pingCmd.returncode

# Generate user defined exclude list
def generateExcludeList():
    """ Generates set of hosts to be excluded from pinging """

    n = int(input("Enter number of hosts to exclude: "))
    excludeList = list(map(int,input("\nEnter hosts to exclude <space separated> : ").strip().split()))[:n]
    excludeSet = set(excludeList)
    return excludeSet

# Exclude certain hosts from pinging list
def toExclude(idx, ip_range, result):
    """ Updates result for IP addresses to be excluded """
    result[idx] = None
    print(f"\n{ip_range[idx]} will not be pinged")
