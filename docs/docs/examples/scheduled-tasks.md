---
layout: page
title: Docs - Examples - scheduled-tasks
permalink: /docs/examples/scheduled-tasks/
---

[Code at GitHub](https://github.com/clvLabs/PyATEMMax/blob/master/examples/scheduled-tasks.py)

This script:
* Connects to an ATEM switcher
* After connection:
  * Shows some switcher settings
  * (optional, commented) Changes some settings
* From that point on:
  * Watches changes in `PVW`/`PGM`/`DSK1`
  * Starts running a scheduled task every n seconds
    * Randomly changes `PVW`/`PGM`
    * Randomly forces a `CUT`
    * Randomly toggles `DSK1`

```
$ python3 scheduled-tasks.py -h
[Tue Nov 24 22:55:31 2020] PyATEMMax demo script: scheduled-tasks
usage: scheduled-tasks.py [-h] [-m MIXEFFECT] [-i INTERVAL] ip

positional arguments:
  ip                    switcher IP address

optional arguments:
  -h, --help            show this help message and exit
  -m MIXEFFECT, --mixeffect MIXEFFECT
                        select mix effect (0/1), default 0
  -i INTERVAL, --interval INTERVAL
                        wait INTERVAL seconds between scheduled actions,
                        default: 3.0
```


```
$ python3 scheduled-tasks.py 192.168.1.111
[Tue Dec  1 04:15:02 2020] PyATEMMax demo script: scheduled-tasks
04:15:02.994 INFO     [PyATEMMax-demo] PyATEMMax demo script starting
04:15:02.994 INFO     [PyATEMMax-demo] Initializing switcher
04:15:02.996 INFO     [ATEMMax] Starting connection with ATEM switcher on 192.168.1.111
04:15:02.996 INFO     [ATEMMax] Connecting for the first time
04:15:02.996 INFO     [PyATEMMax-demo] Waiting for connection
04:15:02.997 INFO     [ATEMMax] Sending HELLO packet
04:15:03.003 INFO     [ATEMMax] Connected to switcher
04:15:03.035 INFO     [ATEMMax] Initialization completed.
04:15:03.045 INFO     [PyATEMMax-demo] Connected, initializing switcher settings
04:15:03.045 INFO     [PyATEMMax-demo] No warnings from the switcher.
04:15:03.045 INFO     [PyATEMMax-demo] videoMode format: f1080p50
04:15:03.045 INFO     [PyATEMMax-demo] audioMixer master volume:  0.0dB
04:15:03.045 INFO     [PyATEMMax-demo] audioMixer input1 volume:  0.0dB
04:15:03.045 INFO     [PyATEMMax-demo] Starting scheduler (every 1.0s)
04:15:03.046 INFO     [PyATEMMax-demo] Listening...
04:15:03.046 INFO     [PyATEMMax-demo] PGM [6: input6] (CAM2: Camera 2 - Adrià)
04:15:03.046 INFO     [PyATEMMax-demo] PVW [3: input3] (BBTY: Backdrop Beauty)
04:15:03.046 INFO     [PyATEMMax-demo] DSK1 OFF
04:15:04.076 INFO     [PyATEMMax-demo] PVW [2: input2] (INTW: Backdrop Interview)
04:15:05.074 INFO     [PyATEMMax-demo] PVW [1000: colorBars] (Bars: Color Bars)
04:15:06.071 INFO     [PyATEMMax-demo] PGM [2002: color2] (Col2: Color 2)
```

## Code walkthrough

Start with the usual initial steps (explained in [Examples](../))

{% highlight python %}
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
parser.add_argument('-m', '--mixeffect', help=f'select mix effect (0/1), default 0', type=int, default=0)
parser.add_argument('-i', '--interval',
                    help=f'wait INTERVAL seconds between scheduled actions, default: 3.0',
                    default=3.0,
                    type=float)
args = parser.parse_args()
{% endhighlight %}

In this case, to prepare the list of sources to be managed, the `PyATEMMax.ATEMVideoSources` constant list is used to avoid writing the raw `ATEM videoSourceId`.

{% highlight python %}
# Video sources used in the script
swsrc = PyATEMMax.ATEMVideoSources

SOURCES = [
    swsrc.input1, swsrc.input2, swsrc.input3, swsrc.input4,
    swsrc.input5, swsrc.input6, swsrc.input7, swsrc.input8,
    swsrc.colorBars,
    swsrc.color1, swsrc.color2,
    swsrc.mediaPlayer1, swsrc.mediaPlayer2,
    ]
{% endhighlight %}

At this point, `startScheduler()` and `timerFunc()` are defined, to manage a basic scheduler using a Python Timer object:

{% highlight python %}
# --------------------------------------------------------------------------------

def startScheduler(switcher: PyATEMMax.ATEMMax) -> None:
    """Start a timer to run scheduled tasks"""

    threading.Timer(args.interval, timerFunc, [switcher]).start()


def timerFunc(switcher: PyATEMMax.ATEMMax) -> None:
    """Function to run each timer hit"""

    doScheduledTasks(switcher)  # Do scheduled tasks
    startScheduler(switcher)    # Restart the timer
{% endhighlight %}

The `showSwitcherSettings()` function will be called when the connection is established and allows to show initial info from the switcher.

{% highlight python %}
def showSwitcherSettings(switcher: PyATEMMax.ATEMMax) -> None:
    """Show switcher settings after connection"""

    if switcher.warningText:
        log.warning(f"Switcher warning: [{switcher.warningText}]")
    else:
        log.info("No warnings from the switcher.")

    log.info(f"videoMode format: {switcher.videoMode.format}")
    log.info(f"audioMixer master volume: {switcher.audioMixer.master.volume:4.01f}dB")
    log.info(f"audioMixer input1 volume: {switcher.audioMixer.input[switcher.atem.audioSources.input1].volume:4.01f}dB")
{% endhighlight %}

The `changeSwitcherSettings()` function will be called when the connection is established and allows to set some initial values.

Note that all code inside this function is commented... just in case. Feel free to uncomment and change everything, play with it!

{% highlight python %}
def changeSwitcherSettings(switcher: PyATEMMax.ATEMMax) -> None:
    """Initialize switcher settings after connection"""

    # Settings can be changed after connection... uncomment to try out
    # switcher.setInputShortName(1, "PyAM")
    # switcher.setInputLongName(1, "PyATEMMax rules!")
    # switcher.setAudioMixerMasterVolume(0.0)
    # switcher.setAudioMixerInputVolume(switcher.atem.audioSources.input1, 0.0)
{% endhighlight %}

The `doScheduledTasks()` function is the one being periodically called.
In this case:
* Either `PGM` or `PVW` will be changed to a random value (50% chances each)
* A `CUT` will be randomly forced (10% chances)
* `DSK1` wil be randomly toggled (30% chances)

{% highlight python %}
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
        switcher.setDownstreamKeyerOnAir(switcher.dsks.dsk1, not switcher.downstreamKeyer[switcher.dsks.dsk1].onAir)


# --------------------------------------------------------------------------------
{% endhighlight %}

The `main()` function contains the startup initialization and the code to watch for changes:

{% highlight python %}
def main():
    """Main loop"""
{% endhighlight %}

In this case we find a `switcher.setLogLevel(logging.INFO)`, which will activate the logging output of the library (that's why you see that much messages on the console), try to set it to `DEBUG` and see what happens.

{% highlight python %}
    log.info("Initializing switcher")
    switcher = PyATEMMax.ATEMMax()
    switcher.setLogLevel(logging.INFO) # Set switcher verbosity (try DEBUG to see more)
    switcher.connect(args.ip)
{% endhighlight %}

This is the first example in which `waitForConnection()` is called without parameters. By default, this function waits indefinitely until the switcher is fully connected. It means that if you start this script and wait a week before you turn your switcher on, the script will wait until it connects. It's really stubborn :)

{% highlight python %}
    log.info("Waiting for connection")
    switcher.waitForConnection()
{% endhighlight %}

At this point, the initialization methods are called (the code was moved outside `main()` to keep it clean)

{% highlight python %}
    log.info("Connected, initializing switcher settings")
    showSwitcherSettings(switcher)
    changeSwitcherSettings(switcher)
{% endhighlight %}

Then, the scheduler is started.

{% highlight python %}
    log.info(f"Starting scheduler (every {args.interval}s)")
    startScheduler(switcher)
{% endhighlight %}

From this point on, the script uses the provided variables
* `PGM` input: `switcher.programInput[mixeffect].videoSource`
* `PVW` input: `switcher.previewInput[mixeffect].videoSource`
* `DSK1` `switcher.downstreamKeyer[dsk].onAir`
    * See how `switcher.dsks.dsk1` is used instead of the value `0`

Note that to show the ATEM source value from `programInput[].videoSource` the script uses `lastPGM.value`. This is because `lastPGM` is an `ATEMConstant` and it would print its name otherwise.

{% highlight python %}
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
{% endhighlight %}

In this script, the `logging` module has been initialized before calling `main()` to demonstrate the logging capabilities of the library.

{% highlight python %}
# Initialize logging
logging.basicConfig( datefmt='%H:%M:%S',
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)-8s [%(name)s] %(message)s')

log = logging.getLogger('PyATEMMax-demo')

# Run main loop
log.info("PyATEMMax demo script starting")
main()
{% endhighlight %}
