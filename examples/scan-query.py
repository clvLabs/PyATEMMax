#!/usr/bin/env python3
# coding: utf-8
"""scan-query.py - PyATEMMax demo script.
   Part of the PyATEMMax library."""

import argparse
import time
import PyATEMMax

print(f"[{time.ctime()}] PyATEMMax demo script: scan-query")

parser = argparse.ArgumentParser()
parser.add_argument('range', help='IP address range (e.g) 192.168.1')
parser.add_argument('-m', '--mixeffect', help='select mix effect (0/1), default 0', type=int, default=0)
args = parser.parse_args()

print(f"[{time.ctime()}] Scanning network range {args.range}.* for ATEM switchers")

switcher = PyATEMMax.ATEMMax()
count = 0

for i in range(1,255):
    ip = f"{args.range}.{i}"
    print(f"[{time.ctime()}] Checking {ip}", end="\r")

    switcher.connect(ip)
    if switcher.waitForConnection(infinite=False, waitForFullHandshake=False):
        # If the switcher answered the handshake we can wait a bit longer...
        if switcher.waitForConnection(infinite=False):
            # Now we have all switcher settings!
            pvw = switcher.previewInput[args.mixeffect].videoSource
            pgm = switcher.programInput[args.mixeffect].videoSource
            pvwName = switcher.inputProperties[pvw].shortName
            pgmName = switcher.inputProperties[pgm].shortName

            print(f"[{time.ctime()}] {switcher.atemModel} found at {ip}"
                    f" - Master Volume: {switcher.audioMixer.master.volume}dB"
                    f" - PVW: {pvwName}"
                    f" - PGM: {pgmName}" )
            count += 1
    switcher.disconnect()

print(f"[{time.ctime()}] FINISHED: {count} ATEM switchers found.")
