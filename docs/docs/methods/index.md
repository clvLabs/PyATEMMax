---
layout: page
title: Docs - Methods
permalink: /docs/methods/
---

This section contains information about the callable methods in the library.

## ATEMConstant parameters

In many cases these methods use `ATEMConstant` parameters. As an example, let's have a look at the `setProgramInputVideoSource` method:
{% highlight python %}
setProgramInputVideoSource(mE:ATEMConstant, videoSource:ATEMConstant) -> None
{% endhighlight %}
        Args:
            mE: see ATEMMixEffects
            videoSource: see ATEMVideoSources

In this case, the `mE` parameter should be a value contained in `ATEMMixEffects` and `videoSource` should also be a valid `ATEMVideoSources` item.

{% highlight python %}
switcher.setProgramInputVideoSource(switcher.atem.mixEffects.mixEffect1, switcher.atem.videoSources.mediaPlayer1)
{% endhighlight %}

See the [Data - Protocol - ATEMConstant](../data/protocol.md#atemconstant) section for more info.

## In this section

* [Init](init.md): Initialization
* [Connect](connect.md): Connection management
* [Set](set.md): Change switcher settings
* [Exec](exec.md): Execute switcher actions
