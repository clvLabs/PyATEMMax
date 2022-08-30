---
layout: page
title: Docs - Methods - Connect
permalink: /docs/methods/connect/
---

## Connecting to a switcher

{% highlight python %}
switcher.connect("192.168.1.111")
{% endhighlight %}

This will start the connection process with the switcher. Once the connection process is started, the `ATEMMax` object will try to connect to the switcher until it succeeds. While it's connected it will automatically try to reconnect if it detects a connection loss.

{% highlight python %}
switcher.connect("192.168.1.111", connTimeout=30)
{% endhighlight %}

The `connTimeout` parameter can be used to specify a connection timeout in seconds (`5` if not specified). When the `ATEMMax` object sees no activity in this time it assumes a connection loss and tries to reconnect.


## Waiting for connection

You can choose the way to wait for connection:

### Wait: using events

You can register a handler for the `connect` event and it will be called every time the connection is established (also after connection losses).
This is the recommended method for GUI programs (when you don't control the main loop).

See the [Events](../events/index.md) section.

### Wait: using waitForConnection()

With no parameters, `waitForConnection()` will keep on waiting until the switcher is connected.

{% highlight python %}
switcher.connect("192.168.1.111")
switcher.waitForConnection()
{% endhighlight %}

If you specify `infinite=False`, the method will use default timeout values to check if the connection is established in an *acceptable* time.

{% highlight python %}
switcher.connect("192.168.1.111")
connected = switcher.waitForConnection(infinite=False)
{% endhighlight %}

If you just want to wait for the initial handshake (e.g. to check if the switcher is *alive*), you can use the `waitForFullHandshake` parameter:

{% highlight python %}
switcher.connect("192.168.1.111")
connected = switcher.waitForConnection(infinite=False, waitForFullHandshake=False)
{% endhighlight %}

If you want to change the timeout value, use the `timeout` parameter, or change the default values (see below). Note that when `timeout` is specified, `infinite` is assumed to be `False`

{% highlight python %}
switcher.connect("192.168.1.111")
connected = switcher.waitForConnection(timeout=2.5)
{% endhighlight %}

#### Changing default wait timeouts

The default values for wait timeouts are:
* `ATEMProtocol.defaultConnectionTimeout`: full connection: 1.0 seconds
* `ATEMProtocol.defaultHandshakeTimeout`: basic handshake: 0.1 seconds

If you experience problems with these values, you can always change them before calling `connect()`

{% highlight python %}
switcher = PyATEMMax.ATEMMax()
switcher.atem.defaultConnectionTimeout = 2.5
switcher.connect("192.168.1.111")
{% endhighlight %}


### Wait: checking it for yourself

After calling `connect()` you can manually check `switcher.connected` to watch connection status.

See the connection state variables in the [Data - Switcher State](../data/state.md) section.

## Pinging a switcher

If you only want to check if your switcher is *alive* you can use `ping()` instead of `connect()` and then use `waitForConnection` with no parameters.

{% highlight python %}
switcher = PyATEMMax.ATEMMax()
switcher.ping("192.168.1.111")
alive = switcher.waitForConnection()
{% endhighlight %}

`ping()` also accepts a `timeout` parameter:

{% highlight python %}
switcher = PyATEMMax.ATEMMax()
switcher.ping("192.168.1.111", timeout=10)
alive = switcher.waitForConnection()
{% endhighlight %}

## Disconnecting from a switcher

After finishing your work with a switcher (even for `ping`) you should close the connection.

{% highlight python %}
switcher = PyATEMMax.ATEMMax()
switcher.connect("192.168.1.111")
switcher.waitForConnection()
# Whatever your program does
switcher.disconnect()
{% endhighlight %}

If your script connects to the switcher, changes some settings and then exits, it's safe to *forget* calling `disconnect()` as the connection will be dropped when your script exits.
