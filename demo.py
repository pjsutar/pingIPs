""" Demo code to run main without user inputs """

import time
import multiprocessing
from pinglib.generateIPs import generateIPs
from pinglib.ping import ping, generateExcludeList, toExclude
from pinglib.oneRangeIPs import pingableOnOneRange

# Network addresses
subnet1 = "192.168.1.0/24"
subnet2 = "192.168.2.0/24"

# Number of ping retries
retries = 1

# Parameter to invoke exclude IPs functionality
bToExclude = False
excludeSet = None


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
    
    result_subnet1 = [0 for _ in range(256)]
    result_subnet2 = [0 for _ in range(256)]

    # Initiate arrays to hold process parameters
    queue = multiprocessing.Queue() # queue holds ping function results
    processes = [] # To hold processes
    results = [] # To hold results of ping function calls

    # Ping all IP addresses
    # Using multiprocessing to execute concurrently

    process1 = multiprocessing.Process(target = ping, args = (queue, ip_range1, retries, result_subnet1, excludeSet))
    processes.append(process1)
    process1.start()

    process2 = multiprocessing.Process(target = ping, args = (queue, ip_range2, retries, result_subnet2, excludeSet))
    processes.append(process2)
    process2.start()

    #Arrange results
    for process in processes:
        result = queue.get()
        results.append(result)
    
    for process in processes:
        process.join()

    subnet1_result = results[0]
    subnet2_result = results[1]

    print("\nPinging is done!\n")

    # Compare ping results and return 
    print("Following IP addresses are pingable only on one range\n")
    oneRangeIPs = pingableOnOneRange(ip_range1, ip_range2, subnet1_result, subnet2_result)
    print(oneRangeIPs)

    return oneRangeIPs

if __name__ == "__main__":

    start_time = time.time()

    main()

    end_time = time.time()

    requiredTime = end_time - start_time

    print(f"Time required for pinging all IPs: {requiredTime} seconds")