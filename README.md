# :rocket: pingIPs
Parallel testing of IP addresses in python
Generates ranges of IP addresses in two subnet IDs provided by user and returns hosts that are accessible in one range and inaccessible in the other.
Refer to [Usage](#memo-usage) to see how to use this

## :tada: About
- Compatible with newer versions of Python 3
- Testing of IPs in two subnets is done in parallel using multiprocessing in Python
- By default there are 2 Workers
- Ping statistics is verbose and displayed

## :sparkles: Support
- Windows, Linux and macOS are supported
- Supports IPv4 IPs by default

## :file_folder: File Structure

    pingIPs                                 # Project root
    ├── readme.md                           # readme
    ├── requirements.txt                    # Requirements
    ├── pinglib                             # Library with utilities
    │   ├── __init__.py            
    |   ├── generateIPs.py                  # Python script
    │   ├── oneRangeIPs.py                  # Python script
    │   ├── ping.py                         # Python script
    │   └── tests                           # Folder with test files
    │       ├── __init__.py                 
    │       ├── test_generateIPs.py         # Function test file
    │       ├── test_oneRangeIPs.py         # Function test file
    │       └── test_ping.py                # Function test file
    │
    ├── main.py                             # main
    ├── demo.py                             # demo code
    ├── Dockerfile                          # Dockerfile
    └── Dockerfile                          # Docker Ignore

## :zap: Install
Following steps are recommended for installation

1. Clone pingIPs repository to your local machine
```bash
$ git clone https://github.com/pjsutar/pingIPs.git
```
2. Use a virtual environment
3. Install requirements in virtual environment
```bash
$ python -m pip install -r requirements.txt
```
4. Run main.py
```bash
$ python main.py
```

## :memo: Usage

```python
# Input subnet ID with CIDR notation
subnet1 = input()
subnet2 = input()

# Input information about IPs to exclude
bToExclude = input()

# Input desired ping retries
retries = input()

# Generate IP ranges
ip_range1 = generateIPs(subnet1)
ip_range_2 = generateIPs(subnet2)

# Ping IP ranges
pingResult1 = ping(ip_range1, params...)
pingResult2 = ping(ip_range2, params...)

# Get IPs pingable only on one range
oneRangeIPs = pingableOnOneRange(ip_range1, ip_range2, pingResult1, pingResult2)
print(oneRangeIPs)
```

## :rotating_light: Tests
To run the tests, run pytest

```bash
$ pytest -v
```

## :scroll: License

[ipaddress library](https://docs.python.org/3/library/ipaddress.html)
[multiprocessing library](https://docs.python.org/3/library/multiprocessing.html)