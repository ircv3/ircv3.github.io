---
layout: post
title: Replies and responses
---
We've finalised the [Standard Replies extension](https://ircv3.net/specs/extensions/standard-replies) which lets us respond with information, warnings, and command errors in a more consistent way. It's already in use by the [`SETNAME` draft](https://ircv3.net/specs/extensions/setname.html) and will enable further development of proposals such as the [`CHATHISTORY` extension](https://github.com/ircv3/ircv3-specifications/pull/393) which we're still developing.

We've also ratified the [Labeled responses spec](https://ircv3.net/specs/extensions/labeled-response), which lets client software properly track and handle responses to their commands. Check the support tables to see which software is already prepared for this extension.

[Capability negotiation](https://ircv3.net/specs/core/capability-negotiation) received some [clarifying updates](https://github.com/ircv3/ircv3-specifications/pull/371) around dealing with version numbers (or the lack thereof) as well as how to handle requesting *loads* of capabilities at once.

Other specs from the [roadmap](https://github.com/ircv3/ircv3-specifications/milestone/4) we're continuing to work on include:

* [Message editing and deletion](https://github.com/ircv3/ircv3-specifications/pull/304), which lets users fix typos, and gives moderators a new way to deal with spam and abuse.
* [Multiline messages](https://github.com/ircv3/ircv3-specifications/pull/398), which lets users post messages that exceed the traditional single line of byte limited text.