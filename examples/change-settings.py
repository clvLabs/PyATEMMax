#!/usr/bin/env python3
# coding: utf-8
"""change-settings.py - PyATEMMax demo script.
   Part of the PyATEMMax library."""

import argparse
import sys
import time
import PyATEMMax

print(f"[{time.ctime()}] PyATEMMax demo script: change-settings")

parser = argparse.ArgumentParser()
parser.add_argument('ip', help='switcher IP address')
parser.add_argument('-v', '--mastervolume', help='master volume (dB)', type=float)
parser.add_argument('-w', '--preview', help='set preview video source', type=int)
parser.add_argument('-p', '--program', help='set program video source', type=int)
parser.add_argument('-m', '--mixeffect', help='select mix effect (0/1), default 0', type=int, default=0)
args = parser.parse_args()

if args.mastervolume is None and args.program is None and args.preview is None:
    print(f"[{time.ctime()}] Please specify a value to change (see help)")
    sys.exit(1)

print(f"[{time.ctime()}] Changing settings in {args.ip}")

if args.mastervolume is not None:
    print(f"[{time.ctime()}] - Master volume: {args.mastervolume}db")

if args.program is not None:
    print(f"[{time.ctime()}] - PGM Video source: {args.program} on m/e {args.mixeffect}")

if args.preview is not None:
    print(f"[{time.ctime()}] - PVW Video source: {args.preview} on m/e {args.mixeffect}")

switcher = PyATEMMax.ATEMMax()
count = 0

print(f"[{time.ctime()}] Starting settings update")
print(f"[{time.ctime()}] Connecting to {args.ip}")

switcher.connect(args.ip)
if switcher.waitForConnection(infinite=False):
    if args.mastervolume is not None:
        switcher.setAudioMixerMasterVolume(args.mastervolume)

    if args.program is not None:
        switcher.setProgramInputVideoSource(args.mixeffect, args.program)

    if args.preview is not None:
        switcher.setPreviewInputVideoSource(args.mixeffect, args.preview)

    print(f"[{time.ctime()}] Settings updated on {switcher.atemModel} at {args.ip}")
    count += 1
else:
    print(f"[{time.ctime()}] ERROR: no response from {args.ip}")
switcher.disconnect()
