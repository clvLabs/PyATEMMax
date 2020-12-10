#!/usr/bin/env python3
# coding: utf-8
"""ping.py - PyATEMMax demo script.
   Part of the PyATEMMax library."""

import argparse
import time
import PyATEMMax

print(f"[{time.ctime()}] PyATEMMax demo script: ping")

DEFAULT_INTERVAL = 1.0

parser = argparse.ArgumentParser()
parser.add_argument('ip', help='switcher IP address')
parser.add_argument('-i', '--interval',
                    help=f'wait INTERVAL seconds between pings, default: {DEFAULT_INTERVAL}',
                    default=DEFAULT_INTERVAL,
                    type=float)
args = parser.parse_args()

print(f"[{time.ctime()}] Pinging ATEM switcher at {args.ip} every {args.interval} seconds")

switcher = PyATEMMax.ATEMMax()
while True:
    switcher.ping(args.ip)

    if switcher.waitForConnection():
        print(f"[{time.ctime()}] Switcher connected")
    else:
        print(f"[{time.ctime()}] Switcher DISCONNECTED")

    switcher.disconnect()
    time.sleep(args.interval)
