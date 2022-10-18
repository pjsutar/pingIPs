import ipaddress

def generateIPs(subnet):
    """
    Function to generate range of IP Addresses in given subnet

    :param subnet <str>: network address with CIDR notation
    Eg. 192.168.1.0/24 or 192.168.2.0/24

    :return ip_range <list>: list of IP Addresses in subnet
    """
    # Initializing list to store IP Addresses
    ip_range = []

    # network object 
    network = ipaddress.IPv4Network(subnet)

    for ip in network:
        ip_range.append(str(ip))
    
    return ip_range