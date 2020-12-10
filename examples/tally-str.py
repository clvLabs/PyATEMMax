#!/usr/bin/env python3
# coding: utf-8
"""tally-str.py - PyATEMMax demo script.
   Part of the PyATEMMax library."""

import argparse
import time
import PyATEMMax

print(f"[{time.ctime()}] PyATEMMax demo script: tally-str")

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
tally = switcher.tally.bySource.flags[args.source]
last_tally_str = str(tally)
print(f"[{time.ctime()}] Connected, tally {args.source} is {last_tally_str}")

# Loop forever watching for changes
print(f"[{time.ctime()}] Watching for tally changes on videoSource {args.source}")
while True:
    # Watch for tally changes
    tally = switcher.tally.bySource.flags[args.source]
    tally_str = str(tally)
    if tally_str != last_tally_str:
        print(f"[{time.ctime()}] Tally {args.source} is {tally_str}")

        # Demonstrate the use of individual tally flags
        if tally.program:
            print(f"[{time.ctime()}] Source {args.source} is on air !!!!")

        last_tally_str = tally_str

    time.sleep(0.01)     # Avoid hogging processor...
