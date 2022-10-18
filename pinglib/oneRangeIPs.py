"""
Function for returning IP addresses pingable on only one range
"""

def pingableOnOneRange(ip_range1, ip_range2, result1, result2):
    """
    Function to identify IPs that are pingable on one range
    but not pingable on the other range

    param: ip_range1 <list>: list of IP addresses in subnet1
    param: ip_range2 <list>: list of IP addresses in subnet2
    param: result1 <list[bool]>: bool list of pingable(True) and non-pingable(False) IPs in subnet1
    param: result2 <list[bool]>: bool list of pingable(True) and non-pingable(False) IPs in subnet2

    print: IP addresses pingable on one range but not pingable on other range

    return: oneRangeIPs <dict>: Dictionary with hosts as keys and pingable IP addresses as values
    """
    idx = 0
    oneRangeIPs = {}

    while idx < len(result1) and idx < len(result2):
        if result1[idx] is True and result2[idx] is False:
            print(f"{ip_range1[idx]} is pingable but {ip_range2[idx]} is not pingable")
            oneRangeIPs[idx] = ip_range1[idx]
            idx += 1
        elif result1[idx] is False and result2[idx] is True:
            print(f"{ip_range1[idx]} is not pingable but {ip_range2[idx]} is pingable")
            oneRangeIPs[idx] = ip_range2[idx]
            idx += 1
        else:
            idx += 1
            continue

    return oneRangeIPs