#!/usr/bin/env python3
# coding: utf-8
"""events.py - PyATEMMax demo script.
   Part of the PyATEMMax library."""

from typing import Dict, Any

import argparse
import time
import random
import PyATEMMax

print(f"[{time.ctime()}] PyATEMMax demo script: events")

DEFAULT_INTERVAL = 1.0

parser = argparse.ArgumentParser()
parser.add_argument('ip', help='switcher IP address')
parser.add_argument('-i', '--interval',
                    help=f'wait INTERVAL seconds between changes, default: {DEFAULT_INTERVAL}',
                    default=DEFAULT_INTERVAL,
                    type=float)
args = parser.parse_args()

print(f"[{time.ctime()}] Changing PGM/PVW on ATEM switcher at {args.ip} every {args.interval} seconds")

# #######################################################################
#
# PyATEMMax Events
#

def onConnectAttempt(params: Dict[Any, Any]) -> None:
    """Called when a connection is attempted"""

    print(f"[{time.ctime()}] Trying to connect to switcher at {params['switcher'].ip}")


def onConnect(params: Dict[Any, Any]) -> None:
    """Called when the switcher is connected"""

    print(f"[{time.ctime()}] Connected to switcher at {params['switcher'].ip}")


def onDisconnect(params: Dict[Any, Any]) -> None:
    """Called when the switcher disconnects"""

    print(f"[{time.ctime()}] DISCONNECTED from switcher at {params['switcher'].ip}")


def onReceive(params: Dict[Any, Any]) -> None:
    """Called when data is received from the switcher"""

    print(f"[{time.ctime()}] Received [{params['cmd']}]: {params['cmdName']}")


def onWarning(params: Dict[Any, Any]) -> None:
    """Called when a warning message is received from the switcher"""

    print(f"[{time.ctime()}] Received warning message: {params['cmd']}")


# #######################################################################
#
# Main code section
#

switcher = PyATEMMax.ATEMMax()

switcher.registerEvent(switcher.atem.events.connectAttempt, onConnectAttempt)
switcher.registerEvent(switcher.atem.events.connect, onConnect)
switcher.registerEvent(switcher.atem.events.disconnect, onDisconnect)
switcher.registerEvent(switcher.atem.events.receive, onReceive)
switcher.registerEvent(switcher.atem.events.warning, onWarning)

switcher.connect(args.ip)

while True:
    if switcher.connected:
        print(f"[{time.ctime()}] Changing PGM")
        switcher.setProgramInputVideoSource(0, random.randint(1,8))

        print(f"[{time.ctime()}] Changing PVW")
        switcher.setPreviewInputVideoSource(0, random.randint(1,8))

    time.sleep(args.interval)
