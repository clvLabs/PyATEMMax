---
layout: page
title: Docs - Examples - scan
permalink: /docs/examples/scan/
---

[Code at GitHub](https://github.com/clvLabs/PyATEMMax/blob/master/examples/scan.py)

This example scans a whole nework range (1-254) searching for ATEM switchers:
```
$ python3 scan.py -h
[Tue Nov 24 22:26:17 2020] PyATEMMax demo script: scan
usage: scan.py [-h] range

positional arguments:
  range       IP address range (e.g) 192.168.1

optional arguments:
  -h, --help  show this help message and exit
```

It tries to connect to all the addresses in the range and reports result.
```
$ python3 scan.py 192.168.1
[Tue Nov 24 22:27:12 2020] PyATEMMax demo script: scan
[Tue Nov 24 22:27:12 2020] Scanning network range 192.168.1.* for ATEM switchers
[Tue Nov 24 22:27:23 2020] ATEM switcher found at 192.168.1.111
[Tue Nov 24 22:27:38 2020] FINISHED: 1 ATEM switchers found.
```

## Code walkthrough

Start with the usual initial steps (explained in [Examples](./index.md))

{% highlight python %}
#!/usr/bin/env python3
# coding: utf-8
"""scan.py - PyATEMMax demo script.
   Part of the PyATEMMax library."""

import argparse
import time
import PyATEMMax

print(f"[{time.ctime()}] PyATEMMax demo script: scan")

parser = argparse.ArgumentParser()
parser.add_argument('range', help='IP address range (e.g) 192.168.1')
args = parser.parse_args()

print(f"[{time.ctime()}] Scanning network range {args.range}.* for ATEM switchers")
{% endhighlight %}

Start working with the switcher:

First, the `ATEMMax` object is created and the hit count is initialized:

{% highlight python %}
switcher = PyATEMMax.ATEMMax()
count = 0
{% endhighlight %}

After that, a loop starts for values (1-254):

{% highlight python %}
for i in range(1,255):
{% endhighlight %}

* The corresponding ip address is built

{% highlight python %}
    ip = f"{args.range}.{i}"
    print(f"[{time.ctime()}] Checking {ip}", end="\r")

{% endhighlight %}

* The script tries to ping the switcher and shows a message indicating if the connection could be established.

{% highlight python %}
    switcher.ping(ip)
    if switcher.waitForConnection():
        print(f"[{time.ctime()}] ATEM switcher found at {ip}")
        count += 1
    switcher.disconnect()

print(f"[{time.ctime()}] FINISHED: {count} ATEM switchers found.")
{% endhighlight %}


## Stripped down version

{% highlight python %}
import PyATEMMax

switcher = PyATEMMax.ATEMMax()

for i in range(1,255):
    ip = f"192.168.1.{i}"
    print(f"Checking {ip}", end="\r")

    switcher.ping(ip)
    if switcher.waitForConnection():
        print(f"ATEM switcher found at {ip}")
    switcher.disconnect()
{% endhighlight %}
