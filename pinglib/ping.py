import ipaddress
import multiprocessing
import subprocess
import platform
from multiprocessing import Queue
import time
import os

def ping(queue: Queue, ip_range: list, retries: int, result: list, excludeSet: set = None) -> list:
    """
    Function to ping IP Addresses in a range

    :param ip_range <list>: list of IP Addresses
    :param retries <int>: number of ping retry attempts
    :param result <default empty list>: empty list to store ping result

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
        param = '-n' if platform.system().lower()=='windows' else '-c'

        # Building the command. Ex: "ping -c 1 192.168.x.y"
        command = ['ping', param, str(retries), '-w', '100', ip]

        # Run ping command
        pingCmd = subprocess.run(command, capture_output = True)
        print(pingCmd.stdout.decode())


        # Update result based on subprocess output
        if pingCmd.returncode == 0:
            result[idx] = True
        else:
            result[idx] = False
    
    # Put result in a queue in order to retrieve it while multiprocessing
    queue.put(result)

    return result

# Generate used defined exclude list
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
