""" Testing ping() function """

import multiprocessing
import pytest
from pinglib.ping import ping, toExclude, generateExcludeList
from multiprocessing import Queue

# Output test to check if function returns desired output
# Testing ping() function with exclude hosts list and 3 ping attempts
def test_ping_output() -> None:
    queue = multiprocessing.Queue()
    testList = ping(queue, ["8.8.8.8", "192.168.1.0", "192.168.1.1", "192.168.1.2", "1.1.1.1"], 3, 
                        result := [_ for _ in range(5)], {1})
    assert testList == [True, None, False, False, True]


# Test to check if all values in result array are boolean
# Testing ping() function without exclude hosts list and 1 ping attempt
def test_ping_output_type() -> None:
    queue = multiprocessing.Queue()
    testList = ping(queue, ["8.8.8.8", "192.168.1.0", "192.168.1.1", "192.168.1.2", "1.1.1.1"], 1, 
                        result := [_ for _ in range(5)], None)
    for i in testList:
        assert type(i) == bool