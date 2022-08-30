---
layout: page
title: About - ATEM version compatibility note
permalink: /about/atem-version/
---

As noticed in [the protocol definition in Skårhøj's site][skaarhoj-bmdprotocol]:
> August 2018: The free open source SKAARHOJ provided Arduino Libraries will only work with ATEM Software Control firmware versions up to 7.5.0.
>
> (SKAARHOJs commercial products will work with ATEM Software Control firmwares beyond 7.5.0)

This means that the Python port may not be able work with firmwares beyond 7.5.0 while it's just a port. Work may be done in the future to partially adapt the port to the new protocol if needed, but it's not guaranteed. If you need to adapt features to new protocol versions, please consider [contributing](../dev/contributing.md) to this project or forking your own copy.

[skaarhoj-bmdprotocol]: http://skaarhoj.com/fileadmin/BMDPROTOCOL.html
