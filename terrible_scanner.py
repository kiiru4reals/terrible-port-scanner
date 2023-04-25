#!/bin/python3

import sys
import socket
from datetime import datetime

# Let us define the target

if len(sys.argv)==2:
    target = socket.gethostbyname(sys.argv[1]) # Translates hostname to IP
else: 
    print ("Invalid amount of arguements")
    print("Syntax: python terrible_scanner.py <ip_address>")

# Adds a banner
print("-" * 50)
print("Scanning target" +target)
print("Start time: " +str(datetime.now()))
print("-" * 50)

try:
    for port in range(1, 1001):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close

# Provision for an interrupt
except KeyboardInterrupt:
    print("\n Exiting program")
    sys.exit()

# Cannot resolve a hosname
except socket.gaierror:
    print("Cannot resolve hostname")
    sys.exit()

# Error resulting from internet connection etc etc
except socket.error:
    print("Could not connect to host, check your internet connection or firewall settings.")
    



