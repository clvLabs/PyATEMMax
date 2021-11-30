---
layout: page
title: Docs - Methods - Exec
permalink: /docs/methods/exec/
---

The `exec` methods allow executing actions on the switcher.

## List of exec methods


### execCutME
{% highlight python %}
execCutME(mE: ATEMConstant) -> None
{% endhighlight %}
Execute: Cut

        Args:
            mE: see ATEMMixEffects


### execAutoME
{% highlight python %}
execAutoME(mE: ATEMConstant) -> None
{% endhighlight %}
Execute: AutoMixEffect

        Args:
            mE: see ATEMMixEffects


### execDownstreamKeyerAutoKeyer
{% highlight python %}
execDownstreamKeyerAutoKeyer(dsk: Union[ATEMConstant, int]) -> None
{% endhighlight %}
Execute: DownstreamKeyer AutoKeyer

        Args:
            dsk: see ATEMDSKs


### execFadeToBlackME
{% highlight python %}
execFadeToBlackME(mE: ATEMConstant) -> None
{% endhighlight %}
Execute: FadeToBlack

        Args:
            mE: see ATEMMixEffects


### execMacroRecord
{% highlight python %}
execMacroRecord(macro: ATEMConstant) -> None
{% endhighlight %}
Execute: Macro Record (use macro.stop to stop recording)

        Args:
            macro: see ATEMMacros


### execMacroStopRecording
{% highlight python %}
execMacroStopRecording() -> None
{% endhighlight %}
Execute: Macro Stop Recording
