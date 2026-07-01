# Python Port Scanner

## Description
A simple TCP port scanner written in Python. It prompts the user for an IP address and checks whether several common TCP ports are open or closed.

## Features
- User enters a target IP address
- Scans common TCP ports
- Displays OPEN or closed for each port
- Uses Python's socket library

## Technologies
- Python 3
- socket

## How to Run

```bash
python3 scanner.py
```

## Example

```
Enter IP address: 192.168.1.1

Scanning 192.168.1.1...

Port 22: OPEN
Port 80: closed
Port 443: OPEN
```

## Disclaimer

Use this program only on systems and networks that you own or have permission to test.
