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
import logging

logging.basicConfig( datefmt='%H:%M:%S',
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)-8s [%(name)s] %(message)s')

log = logging.getLogger('PyATEMMax-demo')

log.info("Starting")


switcher = PyATEMMax.ATEMMax()

switcher.setLogLevel(logging.DEBUG)
switcher.setSocketLogLevel(logging.DEBUG)

switcher.registerEvent(switcher.atem.events.connectAttempt, onConnectAttempt)
switcher.registerEvent(switcher.atem.events.connect, onConnect)
switcher.registerEvent(switcher.atem.events.disconnect, onDisconnect)
switcher.registerEvent(switcher.atem.events.receive, onReceive)
switcher.registerEvent(switcher.atem.events.warning, onWarning)

switcher.connect(args.ip)
switcher.waitForConnection()

log.info(f"mediaPlayer.stillBanks {switcher.mediaPlayer.stillBanks}")
log.info(f"mediaPlayer.clipBanks {switcher.mediaPlayer.clipBanks}")


print(switcher.mediaPlayer.stillFile)
print(switcher.mediaPlayer.stillFile.itemClass)
print(switcher.mediaPlayer.stillFile.itemDict)
# print(switcher.mediaPlayer.stillFile._data)
for stillBankId in switcher.mediaPlayer.stillFile._data:
    stillBank = switcher.mediaPlayer.stillFile._data[stillBankId]
    print(f"- [DBG] [{stillBankId}] used [{stillBank.isUsed}] name [{stillBank.fileName}]")
'''
'''

lock_state = True
iteration = 0

while iteration < 1:
    iteration += 1

    if switcher.connected:

        # print("\n"*5)
        # print("-"*80)
        # log.info(f"Setting LKST lock 0 to {lock_state}")
        # switcher.sendSetLockState(0,lock_state)

        # time.sleep(0.5)


        print("\n"*5)
        print("-"*80)
        log.info(f"Acquiring Media Lock")
        switcher.sendAcquireMediaLock(0, 2)

        time.sleep(1)

        switcher.sendInitDownloadToSwitcherRequest(0, 0, 2, 100)


        # log.info(f"Requesting data transfer")
        # switcher.sendDataTransferRequest(1,0,1)

        # lock_state = not lock_state

        # log.info(f"Changing PGM")
        # switcher.setProgramInputVideoSource(0, random.randint(1,8))

        # log.info(f"Changing PVW")
        # switcher.setPreviewInputVideoSource(0, random.randint(1,8))

    # time.sleep(args.interval)
    time.sleep(5)

switcher.disconnect()
