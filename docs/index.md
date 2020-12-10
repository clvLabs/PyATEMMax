---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
title: PyATEMMax
list_title: Latest news
---

A Python library to monitor and control [Blackmagic Design ATEM][atem-site] video switchers.

{% highlight python %}
# Create ATEMMax object
import PyATEMMax
switcher = PyATEMMax.ATEMMax()

# Connect
switcher.connect("192.168.1.111")
switcher.waitForConnection()

# Have fun!
switcher.setAudioMixerMasterVolume(1.8)    # Set Master Volume: 1.8dB
switcher.setPreviewInputVideoSource(0, 5)  # Set PVW on input 5 for m/e 0
{% endhighlight %}

## Installation
```
pip install PyATEMMax
```
[PyATEMMax on the Python Package Index](https://pypi.org/project/PyATEMMax/)

## Features

* Built using [Python 3][python-site], runs on Windows/Mac/Linux.
    * Tested on Linux/Windows PCs and [Raspberry Pi][raspberry-site].
* **Huge** set of switcher settings available (see [list of 'set' methods](docs/methods/set)).
* Automatic reconnection to the switcher in case of connection loss.
* Switcher settings automatically updated, there's no need to call `update()` methods.
* Able to simultaneously connect to multiple switchers.
* Open source, you can see the code and customize it to fit your needs (see [License](about/license))
* No dependencies, the only thing you need installed on your system is [Python 3][python-site].
* Meant to be user friendly, so you can start playing with your switchers in no time:
    * *Intellisense friendly*: get yourself a Python plugin for your editor and you're ready to go!.
    * Uses Python Type Hints ([PEP 484][pep-484]), which is extremely useful if you are using a linter.

## Ideas

These are just a few possible projects that could be easily built with `PyATEMMax`:
* Custom tallies:
    * DIY _classic_ tally lights (`PGM`/`PVW`/Audio).
    * Audio tallies: play a sound when an input is in `PGM`/`PVW`.
    * _Action_ tallies: move motors, tun on lights, fans... anything!
* _Smart tallies_ (depending on complex factors):
    * You can use all the available switcher settings to build complex notification settings.
* All kinds of crazy DIY controllers, as the most of the settings of the switcher are exposed:
    * Make a touch remote with the MultiViewer from the switcher and a touch screen.
    * Execute a `CUT` when you hit the table with your fist (using a piezo sensor).
    * Change camera settings depending on the input of a light/distance/sound sensor.
    * Change `PVW` input to certain cameras depending on their sound levels.
* Automation
    * Complex macros, depending on many factors (even external ones).
    * Manage many switches from a central point for coordination. If you work on a site with a lot of ATEM switchers you may find this very useful! (see the [examples](docs/examples))

## Talk is cheap. Show me the code.
You can find the code at [github.com/clvLabs/PyATEMMax][pyatemmax-repo].


## Additional resources

* [Blackmagic Design website][bmd-site]
* [Kasper Skårhøj (original libray author) website][skaarhoj-site]
* [Blackmagic ATEM Switcher Protocol][skaarhoj-bmdprotocol] as reverse engineered by Skårhøj




[bmd-site]: https://www.blackmagicdesign.com/
[atem-site]: https://www.blackmagicdesign.com/products/atem
[skaarhoj-site]: https://www.skaarhoj.com/
[skaarhoj-bmdprotocol]: http://skaarhoj.com/fileadmin/BMDPROTOCOL.html
[atemmax-repo]: https://github.com/kasperskaarhoj/SKAARHOJ-Open-Engineering/tree/master/ArduinoLibs/ATEMmax
[raspberry-site]: https://www.raspberrypi.org/
[python-site]: https://www.python.org/
[pep-484]: https://www.python.org/dev/peps/pep-0484/
[pyatemmax-repo]: https://github.com/clvLabs/PyATEMMax
