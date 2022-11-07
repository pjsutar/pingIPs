""" Execute the work flow
This script contains the main function to execute following steps
- Get information from user
- Generate IP address ranges
- Ping IP address ranges
- Exclude IP addresses pinging if defined by user
- Return IP addresses that are pingable on only one range

Pinging task is executed concurrently on two IP ranges using multiprocessing
"""

import time
import multiprocessing
from pinglib.generateIPs import generateIPs
from pinglib.ping import pingResult, ping, generateExcludeList, toExclude
from pinglib.oneRangeIPs import pingableOnOneRange

def main():
    """
    Function to execute work flow

    :return :oneRangeIPs<dict>: Dictionary containing IP addresses
    pingable only on one range

    Ex. If 192.168.1.99 is not pingable and 192.168.2.99 is pingable
    oneRangeIP: {'99': '192.168.2.99'}

    """

    # Generate lists containing IP addresses in subnets
    ip_range1 = generateIPs(subnet1)
    ip_range2 = generateIPs(subnet2)
    
    # Initializing arrays to store ping results
    result_subnet1 = [0 for _ in range(len(ip_range1))]
    result_subnet2 = [0 for _ in range(len(ip_range2))]

    # Initiate arrays to hold process parameters
    queue = multiprocessing.Queue() # queue holds ping function results
    processes = [] # To hold processes
    results = [] # To hold results of ping function calls

    # Ping all IP addresses
    # Using multiprocessing to execute concurrently

    process1 = multiprocessing.Process(target = pingResult, args = (queue, ip_range1, retries, result_subnet1, excludeSet))
    processes.append(process1)
    process1.start()

    process2 = multiprocessing.Process(target = pingResult, args = (queue, ip_range2, retries, result_subnet2, excludeSet))
    processes.append(process2)
    process2.start()

    #Arrange results
    for process in processes:
        result = queue.get()
        results.append(result)
    
    for process in processes:
        process.join()

    # Extract results from queue
    subnet1_result = results[0]
    subnet2_result = results[1]

    # Gracefully close the queue
    queue.close()

    print("\nPinging is done!\n")

    # Compare ping results and return IPs pingable on only one range
    print("Following IP addresses are pingable only on one range\n")
    oneRangeIPs = pingableOnOneRange(ip_range1, ip_range2, subnet1_result, subnet2_result)
    print(oneRangeIPs)

    return oneRangeIPs


def userInputs():
    """ Function to get information about parameters used in pinging process """

    # Parameters specified by user
    global subnet1
    global subnet2
    global bToExclude
    global excludeSet
    global retries

    # Get network addresses from user
    subnet1 = input("Enter network 1 address with CIDR notation (192.168.1.0/24): ")
    subnet2 = input("Enter network 2 adrress with CIDR notation (192.168.2.0/24): ")

    # Implement skip IPs functionality
    """ 
    bToExclude- Parameter to specify if certain IP addresses need to be excluded
    from pinging list. If True, it calls a function to generate a list of hosts 
    that will be excluded from the pinging list
    """
    retry = 0

    while True:
        bToExclude = input("Do you want to exclude certain hosts(Eg. 1, 56) from pinging (y/n): ")
        retry += 1
        if bToExclude in {'y', 'yes', 'Yes', 'YES'}:
            bToExclude = True
            break
        elif bToExclude in {'n', 'no', 'No', 'NO'}:
            bToExclude = False
            break
        else:
            print("Please type valid response (y/n): ")

    # Get info of hosts if user wants to exclude certain IPs
    if bToExclude:
        excludeSet = generateExcludeList()
    else:
        excludeSet = None

    # Get ping retry attempts information
    retries = int(input("Enter required ping retry attempts: "))


if __name__ == "__main__":

    userInputs()

    start_time = time.time()

    main()

    end_time = time.time()

    requiredTime = end_time - start_time

    print(f"Time required for pinging process: {requiredTime} seconds\n")


