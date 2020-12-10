---
layout: page
title: Docs - Methods - Init
permalink: /docs/methods/init/
---

## Creating an ATEMMax object

Simply import the `PyATEMMax` library and create a new `PyATEMMax.ATEMMax` object:

{% highlight python %}
import PyATEMMax

switcher = PyATEMMax.ATEMMax()
{% endhighlight %}


## Creating multiple ATEMMax objects

You can create as many `ATEMMax` objects as you want:

{% highlight python %}
import PyATEMMax

switcher1 = PyATEMMax.ATEMMax()
switcher2 = PyATEMMax.ATEMMax()
switcher3 = PyATEMMax.ATEMMax()
switcher4 = PyATEMMax.ATEMMax()
switcher5 = PyATEMMax.ATEMMax()
{% endhighlight %}

You'll be able to connect each of these objects to a different switcher and *command* them all from a single point :)
