""" Testing ping() function """

import multiprocessing
import subprocess
import platform
import pytest
from pinglib.ping import ping, pingResult, toExclude, generateExcludeList
from multiprocessing import Queue
from mock import Mock, sentinel
from pytest_mock import mocker

# Output test to check if function returns desired output
# Testing ping() function with exclude hosts list and 3 ping attempts

def test_ping_output(mocker) -> None:
    mocker.patch("pinglib.ping", return_value=[0])
    queue = multiprocessing.Queue()
    testList = pingResult(queue, ["8.8.8.8"], 3, 
                        result = [_ for _ in range(1)], excludeSet=None)

    while not queue.empty():
        try:
            queue.get(timeout=0.001)
        except:
            pass
    queue.close()

    assert testList[0] == True
