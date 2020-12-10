#!/usr/bin/env python3
# coding: utf-8
"""scheduled-tasks.py - PyATEMMax demo script.
   Part of the PyATEMMax library."""

import argparse
import time
import threading
import logging
import random
import PyATEMMax

print(f"[{time.ctime()}] PyATEMMax demo script: scheduled-tasks")

parser = argparse.ArgumentParser()
parser.add_argument('ip', help='switcher IP address')
parser.add_argument('-m', '--mixeffect', help='select mix effect (0/1), default 0', type=int, default=0)
parser.add_argument('-i', '--interval',
                    help='wait INTERVAL seconds between scheduled actions, default: 3.0',
                    default=3.0,
                    type=float)
args = parser.parse_args()


# Video sources used in the script
swsrc = PyATEMMax.ATEMVideoSources

SOURCES = [
    swsrc.input1, swsrc.input2, swsrc.input3, swsrc.input4,
    swsrc.input5, swsrc.input6, swsrc.input7, swsrc.input8,
    swsrc.colorBars,
    swsrc.color1, swsrc.color2,
    swsrc.mediaPlayer1, swsrc.mediaPlayer2,
    ]

# --------------------------------------------------------------------------------


def startScheduler(switcher: PyATEMMax.ATEMMax) -> None:
    """Start a timer to run scheduled tasks"""

    threading.Timer(args.interval, timerFunc, [switcher]).start()


def timerFunc(switcher: PyATEMMax.ATEMMax) -> None:
    """Function to run each timer hit"""

    doScheduledTasks(switcher)  # Do scheduled tasks
    startScheduler(switcher)    # Restart the timer


def showSwitcherSettings(switcher: PyATEMMax.ATEMMax) -> None:
    """Show switcher settings after connection"""

    if switcher.warningText:
        log.warning(f"Switcher warning: [{switcher.warningText}]")
    else:
        log.info("No warnings from the switcher.")

    log.info(f"videoMode format: {switcher.videoMode.format}")
    log.info(f"audioMixer master volume: {switcher.audioMixer.master.volume:4.01f}dB")
    log.info(f"audioMixer input1 volume: {switcher.audioMixer.input[switcher.atem.audioSources.input1].volume:4.01f}dB")


def changeSwitcherSettings(switcher: PyATEMMax.ATEMMax) -> None:
    """Initialize switcher settings after connection"""

    # Settings can be changed after connection... uncomment to try out
    # switcher.setInputShortName(1, "PyAM")
    # switcher.setInputLongName(1, "PyATEMMax rules!")
    # switcher.setAudioMixerMasterVolume(0.0)
    # switcher.setAudioMixerInputVolume(switcher.atem.audioSources.input1, 0.0)


def doScheduledTasks(switcher: PyATEMMax.ATEMMax) -> None:
    """Scheduled tasks are defined here"""

    # Randomly change PVW/PGM
    if random.random() < 0.5:
        videoSrc = random.choice(SOURCES)
        switcher.setProgramInputVideoSource(args.mixeffect, videoSrc)
    else:
        videoSrc = random.choice(SOURCES)
        switcher.setPreviewInputVideoSource(args.mixeffect, videoSrc)

    # Randomly force a CUT
    if random.random() < 0.1:
        log.info("Forcing CUT")
        switcher.execCutME(args.mixeffect)

    # Randomly toggle DSK1
    if random.random() < 0.3:
        switcher.setDownstreamKeyerOnAir(switcher.atem.dsks.dsk1, not switcher.downstreamKeyer[switcher.atem.dsks.dsk1].onAir)


# --------------------------------------------------------------------------------

def main():
    """Main loop"""

    log.info("Initializing switcher")
    switcher = PyATEMMax.ATEMMax()
    switcher.setLogLevel(logging.INFO) # Set switcher verbosity (try DEBUG to see more)
    switcher.connect(args.ip)

    log.info("Waiting for connection")
    switcher.waitForConnection()

    log.info("Connected, initializing switcher settings")
    showSwitcherSettings(switcher)
    changeSwitcherSettings(switcher)

    log.info(f"Starting scheduler (every {args.interval}s)")
    startScheduler(switcher)

    # Start listening
    lastPGM = None
    lastPVW = None
    lastDSK1 = None

    log.info("Listening...")
    while True:
        # Watch PGM/PVW changes
        if switcher.programInput[args.mixeffect].videoSource != lastPGM:
            lastPGM = switcher.programInput[args.mixeffect].videoSource
            sourceName = switcher.atem.videoSources.getName(lastPGM)
            shortname = switcher.inputProperties[lastPGM].shortName
            longname = switcher.inputProperties[lastPGM].longName

            log.info(f"PGM [{(lastPGM.value)}: {sourceName}] ({shortname}: {longname})")

        if switcher.previewInput[args.mixeffect].videoSource != lastPVW:
            lastPVW = switcher.previewInput[args.mixeffect].videoSource
            sourceName = switcher.atem.videoSources.getName(lastPVW)
            shortname = switcher.inputProperties[lastPVW].shortName
            longname = switcher.inputProperties[lastPVW].longName

            log.info(f"PVW [{(lastPVW.value)}: {sourceName}] ({shortname}: {longname})")

        if switcher.downstreamKeyer[switcher.atem.dsks.dsk1].onAir != lastDSK1:
            lastDSK1 = switcher.downstreamKeyer[switcher.atem.dsks.dsk1].onAir
            log.info(f"DSK1 {'ON' if lastDSK1 else 'OFF'}")

        # Avoid hogging processor...
        time.sleep(0.01)


# --------------------------------------------------------------------------------

# Initialize logging
logging.basicConfig( datefmt='%H:%M:%S',
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)-8s [%(name)s] %(message)s')

log = logging.getLogger('PyATEMMax-demo')

# Run main loop
log.info("PyATEMMax demo script starting")
main()
