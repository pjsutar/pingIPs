""" Testing generateIPs() function """

import pytest
from pinglib.generateIPs import generateIPs

# Output test
def test_generateIPs_output() -> None:
    ip_range = generateIPs("192.168.1.0/24")
    assert ip_range[0] == "192.168.1.0" and ip_range[128] == "192.168.1.128"

# Invalid argument test
def test_generateIPs_invalidArg() -> None:
    with pytest.raises(ValueError):
        for invalidVal in ['1.0', '1.2.2.2.2', 1111]:
            generateIPs(invalidVal)
