---
title: Frequently Asked Questions
layout: default
meta-description: Frequently Asked Questions of the IRCv3 Working Group.
page-header: >
  Frequently Asked Questions
---

### What about older clients?

We intend for all the specs we put out to be backwards-compatible. In other words, if an old client connects to a server that supports IRCv3 extensions, that old client should work without an issue. Likewise, if a new client connects to a server that doesn't support IRCv3 it'll work fine (just without some of the new features that IRCv3 allows).

### Are you working on the server-to-server protocol as well?

Where there is only one client-to-server (C2S) protocol, there are a multitude of server-to-server (S2S) protocols. The client protocol can be extended in a relatively standard way, whereas the server protocol cannot because there is no single 'server protocol' in use today.

Almost every IRC server out there has its own, or its own variant of an, S2S protocol. As such, we're not working on the server-to-server protocol at this time. The only thing that users see is the client-to-server (C2S) protocol, which is why we're chartered to prototype, develop and specify extensions to it.

### Who runs IRCv3?

Originally, we were setup by the Atheme group to develop extensions to the IRC client protocol. These days, the direction of the IRCv3 WG is led by the [technical board]({{site.baseurl}}/charter.html).

We're just a collection of server, client, and bot/library developers that work together to produce new specifications and try to push IRC forward. Anyone's free to join, and as long as you agree with [our charter](/charter.html) we're happy to get your suggestions, ideas and feedback.

### Is there a roadmap or timeline?

We do have a roadmap which roughly lays out where we want to go and what we're focusing on, which you can find [here](https://github.com/ircv3/ircv3-specifications/milestone/4).

In terms of a timeline, work happens whenever someone writes something up or posts their thoughts on existing documents. Almost all of the people involved with us do so on a volunteer basis, so activity happens when they have free time to contribute. If you want to see something move forward and nobody else has commited to working on it, feel free to write it up and submit it as per our [contribution docs](https://github.com/ircv3/ircv3-specifications/blob/master/CONTRIBUTING.md)!

### Are you working on an RFC?

Various people are working on updated IRC core protocol specifications, but there aren't any we can recommend at this time. If you have trouble understanding / implementing a specific piece of the IRC client protocol, feel free to [have a chat to us]({{site.baseurl}}/contact.html). We can try to work it out and/or point you in the right direction.

As a note, the RFCs are old, outdated, and don't properly represent how the IRC client or server protocols have grown over time. The best place to see how real-world IRC software works is that software itself.

{% include anchors.html %}
