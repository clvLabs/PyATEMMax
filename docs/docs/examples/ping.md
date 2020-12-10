---
layout: page
title: Docs - Examples - ping
permalink: /docs/examples/ping/
---

[Code at GitHub](https://github.com/clvLabs/PyATEMMax/blob/master/examples/ping.py)

This example is an improvised `ping` utility for ATEM switchers:
```
$ python3 ping.py -h
[Tue Nov 24 21:48:32 2020] PyATEMMax demo script: ping
usage: ping.py [-h] [-i INTERVAL] ip

positional arguments:
  ip                    switcher IP address

optional arguments:
  -h, --help            show this help message and exit
  -i INTERVAL, --interval INTERVAL
                        wait INTERVAL seconds between pings, default: 1.0
```

It tries to connect to the specified ip once a second and reports result. Also allows to specify the interval between `pings` with the `-i` parameter.

```
$ python3 ping.py 192.168.1.111
[Tue Nov 24 21:52:14 2020] PyATEMMax demo script: ping
[Tue Nov 24 21:52:14 2020] Pinging ATEM switcher at 192.168.1.111 every 1.0 seconds
[Tue Nov 24 21:52:14 2020] Switcher connected
[Tue Nov 24 21:52:15 2020] Switcher connected
[Tue Nov 24 21:52:16 2020] Switcher connected
...
```

```
$ python3 ping.py 192.168.1.222 -i 10
[Tue Nov 24 21:52:26 2020] PyATEMMax demo script: ping
[Tue Nov 24 21:52:26 2020] Pinging ATEM switcher at 192.168.1.222 every 10.0 seconds
[Tue Nov 24 21:52:26 2020] Switcher DISCONNECTED
[Tue Nov 24 21:52:36 2020] Switcher DISCONNECTED
[Tue Nov 24 21:52:47 2020] Switcher DISCONNECTED
...
```

## Code walkthrough

Start with the usual initial steps (explained in [Examples](../))

{% highlight python %}
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
{% endhighlight %}

Start working with the switcher:

First, the `ATEMMax` object is created:

{% highlight python %}
switcher = PyATEMMax.ATEMMax()
{% endhighlight %}

Then, the script enters an infinite loop:

{% highlight python %}
while True:
{% endhighlight %}

For each iteration, the script will:
* Ping the switcher using the provided ip address

{% highlight python %}
    switcher.ping(args.ip)
{% endhighlight %}

* Wait for the handshake to finish.

{% highlight python %}
    if switcher.waitForConnection():
{% endhighlight %}

* With the result of `waitForConnection` the script knows which message to print:

{% highlight python %}
        print(f"[{time.ctime()}] Switcher connected")
    else:
        print(f"[{time.ctime()}] Switcher DISCONNECTED")
{% endhighlight %}

* Then, the connection to the switcher is closed:

{% highlight python %}
    switcher.disconnect()
{% endhighlight %}

* And the script *sleeps* for the speciried `interval`

{% highlight python %}
    time.sleep(args.interval)
{% endhighlight %}


## Stripped down version

{% highlight python %}
import time
import PyATEMMax

switcher = PyATEMMax.ATEMMax()
while True:
    switcher.ping("192.168.1.111")

    if switcher.waitForConnection():
        print(f"Switcher connected")
    else:
        print(f"Switcher DISCONNECTED")

    switcher.disconnect()
    time.sleep(1)
{% endhighlight %}
