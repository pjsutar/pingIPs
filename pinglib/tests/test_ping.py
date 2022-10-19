""" Testing ping() function """

import multiprocessing
import subprocess
import platform
import pytest
from pinglib.ping import ping, toExclude, generateExcludeList
from multiprocessing import Queue

# Output test to check if function returns desired output
# Testing ping() function with exclude hosts list and 3 ping attempts

# Function to install 'fping' if running tests on Linux or Darwin
@pytest.fixture
def fpingInstall():
    if platform.system().lower() == "linux":
        subprocess.run("sudo apt install -y fping")
    elif platform.system().lower() == "darwin":
        subprocess.run("sudo port install fping")
    else:
        pass


def test_ping_output(fpingInstall) -> None:
    queue = multiprocessing.Queue()
    testList = ping(queue, ["8.8.8.8", "192.168.1.0", "192.168.1.1", "192.168.1.2", "1.1.1.1"], 3, 
                        result = [_ for _ in range(5)], excludeSet={1})

    while not queue.empty():
        try:
            queue.get(timeout=0.001)
        except:
            pass
    queue.close()

    assert testList == [True, None, False, False, True]


# Test to check if all values in result array are boolean
# Testing ping() function without exclude hosts list and 1 ping attempt

def test_ping_output_type(fpingInstall) -> None:
    queue = multiprocessing.Queue()
    testList = ping(queue, ["8.8.8.8", "192.168.1.0", "192.168.1.1", "192.168.1.2", "1.1.1.1"], 1, 
                        result = [_ for _ in range(5)], excludeSet=None)

    while not queue.empty():
        try:
            queue.get(timeout=0.001)
        except:
            pass
    queue.close()

    for i in testList:
        assert type(i) == bool