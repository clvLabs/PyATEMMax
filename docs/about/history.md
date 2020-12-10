---
layout: page
title: About - History
permalink: /about/history/
---

Finding myself in the need of a Python library to control ATEM switchers I started searching and noticed a couple things:
* There was Skårhøj's ATEMmax, developed in C++ for the Arduino platform.
* There were a lot of partial ports of this library by many people in many languages.
* There were a few other original libraries (JavaScript, C#, C++), but I found none as complete, well documented and maintained as Skårhøj's is.

So, the solution was obvious... I had to port that library to Python!

The initial intention was to do a direct language translation, leaving a library that resembled the original as much as possible, so anybody familiar with the original ATEMmax could easily work with this new library.

As the development progressed, I started noticing certains aspects of the interface in the original library that were supposedly forced by the language (C++) and platform it was written for (Arduino).
If you want to run your code inside a tiny microprocessor, you have to be very conservative in terms of memory usage.

Having in mind that this library will run on *beefier* platforms (I'm guessing ARM [SBC][sbc-definition], at least), I could do things such as:
* Have bigger transmission buffers.
* Store information for all entities (in some cases memory limitation has imposed restrictions in the Arduino version)
* Run the main loop on an independent thread.
* Make a nice data model to expose data and methods.
* Provide an event system for notifications.

... well, all those nice things you have so cheap when you run Python on a PC/SBC  :)

So, here it is... yet another clone of ATEMmax... hope it helps!


Tony

[skaarhoj-site]: https://www.skaarhoj.com/
[skaarhoj-repo]: https://github.com/kasperskaarhoj/SKAARHOJ-Open-Engineering/tree/master/ArduinoLibs/ATEMmax
[skaarhoj-bmdprotocol]: https://www.skaarhoj.com/fileadmin/BMDPROTOCOL.html
[sbc-definition]: https://en.wikipedia.org/wiki/Single-board_computer
