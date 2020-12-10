---
layout: page
title: Docs - Events
permalink: /docs/events/
---

In order to make it easier to manage the connection with the switcher, you can register event handlers for a few events.

Check the [events example](../examples/events) to see events in action.

## Available events

The list of available events is defined at `ATEMMax.atem.events`:
* `connectAttempt`: a connection/reconnection attempt just started.
* `connect`: connection has been established.
* `disconnect`: disconnection detected.
* `receive`: data command received.
* `warning`: warning message received.

## Creating a handler

To create an event handler, define a function receiving a single parameter of type `Dict`:

{% highlight python %}
def onXXX(params):
    pass
{% endhighlight %}


### Event parameters

The `params` dictionary received will always contain a `switcher` item, pointing to the `ATEMMax` object which raised the event. This is useful if you want to share an event handler with multiple `ATEMMax` instances.

In the case of the `receive` event, the `params` dictionary will also include:
* `cmd` (str): short name of the received command
* `cmdName` (str): long name of the received command

## Registering a handler

Use the `registerEvent()` method before calling `connect()`:

{% highlight python %}
def onConnect(params):
    print(f"Connected to switcher at {params['switcher'].ip}")

switcher = PyATEMMax.ATEMMax()
switcher.registerEvent(switcher.atem.events.connect, onConnect)
switcher.connect("192.168.1.111")
{% endhighlight %}


