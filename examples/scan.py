#!/usr/bin/env python3
# coding: utf-8
"""scan.py - PyATEMMax demo script.
   Part of the PyATEMMax library."""

import argparse
import time
import PyATEMMax

print(f"[{time.ctime()}] PyATEMMax demo script: scan")

parser = argparse.ArgumentParser()
parser.add_argument('range', help='IP address range (e.g) 192.168.1')
args = parser.parse_args()

print(f"[{time.ctime()}] Scanning network range {args.range}.* for ATEM switchers")

switcher = PyATEMMax.ATEMMax()
count = 0

for i in range(1,255):
    ip = f"{args.range}.{i}"
    print(f"[{time.ctime()}] Checking {ip}", end="\r")

    switcher.ping(ip)
    if switcher.waitForConnection():
        print(f"[{time.ctime()}] ATEM switcher found at {ip}")
        count += 1
    switcher.disconnect()

print(f"[{time.ctime()}] FINISHED: {count} ATEM switchers found.")
