---
title: Frequently Asked Questions
layout: default
meta-description: Frequently Asked Questions of the IRCv3 Working Group.
---
# Frequently Asked Questions

These are questions and issues which are raised to us reasonably often. If you have a question not in this list, feel free to [talk to us](/contact.html).

### What about older clients?

We intend for all the specs we put out to be backwards-compatible. In other words, if an old client connects to a server that supports IRCv3, that old client should work without an issue. Likewise, if a new client connects to a server that doesn't support IRCv3 it'll work fine (just without some of the new features that IRCv3 allows).

### Are you working on the server-to-server protocol as well?

The only thing that users see is the client-to-server (C2S) protocol, which is why we're chartered to prototype, develop and specify extensions to it. As far as end users are concerned, the server-to-server (S2S) protocol can be implemented in a multitude of different ways without making a difference to their experience.

As well, almost every IRC server out there today has its' own S2S protocol. Corralling that is best left to the community itself.

### Who runs IRCv3?

Originally, we were setup by the Atheme group to develop extensions to the IRC client protocol. We're just a collection of server, client, and bot/library developers that work together to produce new specifications and try to push IRC forward. Anyone's free to join, and as long as you agree with [our charter](/charter.html) we're happy to get your opinions, suggestions and feedback.

### Is there a roadmap or timeline?

We do have a roadmap which roughly lays out where we want to go and what we're focusing on, which you can find [here](https://github.com/ircv3/ircv3-specifications/milestone/4).

In terms of a timeline, work happens whenever someone writes something up or posts their thoughts on existing documents. Almost all of the people involved with us do so on a volunteer basis, so activity happens when they have free time to contribute. If you want to see something move forward and nobody else has commited to working on it, feel free to write it up and submit it as per our [contribution docs](https://github.com/ircv3/ircv3-specifications/blob/master/CONTRIBUTING.md)!

### Are you working on an RFC?

The RFCs are old and don't properly represent how the IRC client or server protocols have grown over time. The best place to look for how real-world IRC software works is that software itself.

Various people are working on updated IRC core protocol specifications, but there aren't any we can recommend at this time. If you have trouble understanding / implementing a specific piece of the IRC client protocol, feel free to [have a chat to us](/contact.html). We can try to work it out and/or point you in the right direction.

{% include anchors.html %}
