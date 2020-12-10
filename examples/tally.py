#!/usr/bin/env python3
# coding: utf-8
"""tally.py - PyATEMMax demo script.
   Part of the PyATEMMax library."""

import argparse
import time
import PyATEMMax

print(f"[{time.ctime()}] PyATEMMax demo script: tally")

parser = argparse.ArgumentParser()
parser.add_argument('ip', help='switcher IP address')
parser.add_argument('source', help='video source number', type=int)
parser.add_argument('-m', '--mixeffect', help='select mix effect (0/1), default 0', type=int, default=0)
args = parser.parse_args()

# Connect to the switcher
print(f"[{time.ctime()}] Connecting to switcher at {args.ip}")
switcher = PyATEMMax.ATEMMax()
switcher.connect(args.ip)
switcher.waitForConnection()

# Show initial tally state
last_src = switcher.programInput[args.mixeffect].videoSource
print(f"[{time.ctime()}] Connected, tally {args.source} is [{'ON' if last_src == args.source else 'OFF' }]")

# Loop forever watching for changes
print(f"[{time.ctime()}] Watching for tally changes on videoSource {args.source}")
while True:
    # Watch for tally changes
    src = switcher.programInput[args.mixeffect].videoSource
    if src != last_src:
        # print(f"[{time.ctime()}] programInput.videoSource changed!")
        if src == args.source:
            print(f"[{time.ctime()}] Tally {args.source} [ON]")
        elif last_src == args.source:
            print(f"[{time.ctime()}] Tally {args.source} [OFF]")

        last_src = src

    time.sleep(0.01)     # Avoid hogging processor...
