---
layout: page
title: Docs - Examples
permalink: /docs/examples/
sidebar: tree.toc
---

A few code examples are provided with the library code. Here you'll find a step-by-step explanation of each one.

You can get the code for all the examples at [the GitHub repo][pyatemmax-examples-repo].

## In this section

* [tally](tally.md): Quick tally indicator.
* [tally-str](tally-str.md): A different (maybe easier) way to access tally information.
* [ping](ping.md): Check if your switcher is alive (ping-like).
* [scan](scan.md): Scan a network for ATEM switchers.
* [scan-query](scan-query.md): Scan a network for ATEM switchers and show some settings.
* [change-settings](change-settings.md): Change some settings on a switcher.
* [change-settings-multi](change-settings-multi.md): Change some settings on multiple switchers at once.
* [events](events.md): Using `PyATEMMax`'s events.
* [scheduled-tasks](scheduled-tasks.md): A more elaborate example, including scheduled tasks.

## Running the examples

If you haven't installed the library you will need to copy the library code into the examples folder before running the examples:

{% highlight bash %}
$ cp -r $(pwd)/PyATEMMax $(pwd)/examples/PyATEMMax
{% endhighlight %}

A better option, which you will need if you want to modify `PyATEMMax`'s code, is to create a [symbolic link][ln-manpage]:

{% highlight bash %}
$ ln -s $(pwd)/PyATEMMax $(pwd)/examples/PyATEMMax
{% endhighlight %}

## Hey! There's strange code in the examples!
In order to provide some level of *Type Checking* and make it easier to not mix variable types, this code uses Python Type Hints ([PEP 484][pep-484]).

This can make the code look *a little strange* if you're used to the *classic Python*. As an example, in `scheduled-tasks.py` you can find this function:
{% highlight python %}
def changeSwitcherSettings(switcher: PyATEMMax.ATEMMax) -> None:
{% endhighlight %}

This is equivalent to:
{% highlight python %}
def changeSwitcherSettings(switcher):
{% endhighlight %}

... but includes a couple *hints* that can help your code editor warn you if you're using a wrong variable type somewhere.

If you don't know what `linting` is or you don't want to know, you can safely ignore it, you don't have to write your code like this.

## Common structure in all/most examples

The usual format in these example scripts follows::

* [Shebang][shebang-def] and [Python source encoding mark][pep-263]

{% highlight python %}
#!/usr/bin/env python3
# coding: utf-8
{% endhighlight %}

* [Docstring][pep-257]

{% highlight python %}
"""ping.py - PyATEMMax demo script.
   Part of the PyATEMMax library."""
{% endhighlight %}

* the necessary `import` statements for the script

{% highlight python %}
import argparse
import time
import PyATEMMax
{% endhighlight %}

* welcome message

{% highlight python %}
print(f"[{time.ctime()}] PyATEMMax demo script: ping")
{% endhighlight %}

* constant initialization for the script

{% highlight python %}
DEFAULT_INTERVAL = 1.0
{% endhighlight %}

* read of command line arguments

{% highlight python %}
parser = argparse.ArgumentParser()
parser.add_argument('ip', help='switcher IP address')
parser.add_argument('-i', '--interval',
                    help=f'wait INTERVAL seconds between pings, default: {DEFAULT_INTERVAL}',
                    default=DEFAULT_INTERVAL,
                    type=float)
args = parser.parse_args()
{% endhighlight %}

* after all this initialization the `ATEMMax` object is usually created

{% highlight python %}
switcher = PyATEMMax.ATEMMax()
{% endhighlight %}

* at some point the script will tell the `ATEMMax` object to connect

{% highlight python %}
switcher.connect(args.ip)
{% endhighlight %}

* after calling `connect()` it's usual to wait for the connection to be established

{% highlight python %}
switcher.waitForConnection()
{% endhighlight %}

* and then, after doing its stuff the script normally closes the `ATEMMax` object

{% highlight python %}
switcher.disconnect()
{% endhighlight %}

Having this in mind, the *step-by-step* explanations will omit detail in these initialization sections, as
* they are (more or less) the same in all the examples.
* they do stuff with other Python libraries.

## Stripped down (*no-nonsense*) versions

Some examples include a *stripped down version* which removes all *non-essential clutter*:
* Command line argument management.
* Console messages.
* Fancy constants.
* Shebangs and Python source encoding marks.
* Docstrings.

While the *full* examples could even serve as a general CLI utilities, the stripped down versions are more likely what someone will build as a *quickScript* to solve a problem at hand. If you always connect to the same switcher (more likely than not) you will not need code to get the IP address from the command line, etc.


[shebang-def]: https://en.wikipedia.org/wiki/Shebang_(Unix)
[pep-263]: https://www.python.org/dev/peps/pep-0263/
[pep-257]: https://www.python.org/dev/peps/pep-0257/
[pep-484]: https://www.python.org/dev/peps/pep-0484/

[ln-manpage]: https://man7.org/linux/man-pages/man1/ln.1.html

[pyatemmax-examples-repo]: https://github.com/clvLabs/PyATEMMax/tree/master/examples
