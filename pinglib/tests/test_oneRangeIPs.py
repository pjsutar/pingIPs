""" Testing pingableOnOneRange() function """

import pytest
from pinglib.oneRangeIPs import pingableOnOneRange


# Fixcture to feed data to tests

@pytest.fixture
def funcRes():
    res = pingableOnOneRange(["192.168.1.0", "192.168.1.1", "192.168.1.2", "192.168.1.3"],
                            ["192.168.2.0", "192.168.2.1", "192.168.2.2", "192.168.2.3"],
                            [True, True, False, True],
                            [True, True, True, False])
    return res

# Test to check pingableOnOneRange() output accuracy

def test_pingableOnOneRange_output1(funcRes) -> None:
    assert 2 in funcRes and 3 in funcRes

def test_pingableOnOneRange_output2(funcRes) -> None:
    assert 0 not in funcRes and 1 not in funcRes

def test_pingableOnOneRange_output3(funcRes) -> None:
    assert funcRes[2] == "192.168.2.2" and funcRes[3] == "192.168.1.3"