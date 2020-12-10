---
layout: page
title: Docs - Examples - tally
permalink: /docs/examples/tally/
---

[Code at GitHub](https://github.com/clvLabs/PyATEMMax/blob/master/examples/tally.py)

This example is a quick demonstration on how to get tally information for an input source.
```
$ python3 tally.py -h
[Tue Nov 24 22:06:23 2020] PyATEMMax demo script: tally
usage: tally.py [-h] [-m MIXEFFECT] ip source

positional arguments:
  ip                    switcher IP address
  source                video source number

optional arguments:
  -h, --help            show this help message and exit
  -m MIXEFFECT, --mixeffect MIXEFFECT
                        select mix effect (0/1), default 0
```

It connects to the specified switcher and keeps listening for `PGM` changes to show tally changes for the selected source:

```
$ python3 tally.py 192.168.1.111 5
[Tue Nov 24 22:07:23 2020] PyATEMMax demo script: tally
[Tue Nov 24 22:07:23 2020] Connecting to switcher at 192.168.1.111
[Tue Nov 24 22:07:23 2020] Connected, tally 5 is [OFF]
[Tue Nov 24 22:07:23 2020] Watching for tally changes on videoSource 5
[Tue Nov 24 22:07:26 2020] Tally 5 [ON]
[Tue Nov 24 22:07:29 2020] Tally 5 [OFF]
[Tue Nov 24 22:07:41 2020] Tally 5 [ON]
[Tue Nov 24 22:07:41 2020] Tally 5 [OFF]
...
```


## Code walkthrough

Start with the usual initial steps (explained in [Examples](../))

{% highlight python %}
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
parser.add_argument('-m', '--mixeffect', help=f'select mix effect (0/1), default 0', type=int, default=0)
args = parser.parse_args()
{% endhighlight %}

Connect to the switcher and wait for the connection process to finish:

{% highlight python %}
# Connect to the switcher
print(f"[{time.ctime()}] Connecting to switcher at {args.ip}")
switcher = PyATEMMax.ATEMMax()
switcher.connect(args.ip)
switcher.waitForConnection()
{% endhighlight %}

Once it's connected to the switcher it can get information on the selected videoSource for `PGM`.

To do this, it reads the provided `programInput.videoSource` for the selected `mixEffect`:

{% highlight python %}
# Show initial tally state
last_src = switcher.programInput[args.mixeffect].videoSource
print(f"[{time.ctime()}] Connected, tally {args.source} is [{'ON' if last_src == args.source else 'OFF' }]")
{% endhighlight %}

From this point on, the script just keeps on asking for the same data and comparing it to see if it has changed.

{% highlight python %}
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
{% endhighlight %}


## Stripped down version

{% highlight python %}
import time
import PyATEMMax

SOURCE = 5

switcher = PyATEMMax.ATEMMax()
switcher.connect("192.168.1.111")
switcher.waitForConnection()

last_src = switcher.programInput[0].videoSource
print(f"Connected, tally {SOURCE} is [{'ON' if last_src == SOURCE else 'OFF' }]")

while True:
    src = switcher.programInput[0].videoSource
    if src != last_src:
        if src == SOURCE:
            print(f"Tally {SOURCE} [ON]")
        elif last_src == SOURCE:
            print(f"Tally {SOURCE} [OFF]")

        last_src = src

    time.sleep(0.01)     # Avoid hogging processor...
{% endhighlight %}
