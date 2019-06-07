---
layout: post
title: Caps, Tags, IDs and WebIRC
---
Time for our annual blog post! There's been a lot going on so we'll summarize what we've been up to lately.

First, we've rewritten the [Capability Negotiation spec](https://ircv3.net/specs/core/capability-negotiation.html). Previously, capabilities were described in three separate documents, which made things pretty hard-to-understand for implementers. The updated document makes it a lot easier to understand and write software that negotiates capabilities.

We've ratified the [Message Tags spec](https://ircv3.net/specs/extensions/message-tags.html), which merges the two separate tag-describing documents we used to have. The final version includes a boosted size limit for tags and defines the `ERR_INPUTTOOLONG (417)` numeric, so clients can send more data and know when they've reached the limit. Clients can also exchange tag data between themselves with the new `TAGMSG` message.

We've also ratified the [Message IDs spec](https://ircv3.net/specs/extensions/message-ids.html), which lets servers assign IDs to chat messages and any other events sent to clients. This, for example, lets users react or refer to specific messages.

[The WebIRC command](https://ircv3.net/specs/extensions/message-ids.html) has been documented and extended as a formal standard, letting gateways now flag when an incoming connection is using TLS.

The [STARTTLS command](https://ircv3.net/specs/extensions/tls-3.1.html) has been **deprecated** in favour of `sts`. The [Strict Transport Security extension](https://ircv3.net/specs/extensions/sts.html) is recommended as it can also protect connections after the initial one. We're also exploring options around preload lists and other ways of protecting users' connections before plaintext hits the wire.

The proposed [`SETNAME` command](https://ircv3.net/specs/extensions/setname.html) is now an IRCv3 draft. This command lets users change their realname on the fly, which is especially useful for clients that use this value as a display name or to link to avatars.

The proposed [`typing` client tag](https://ircv3.net/specs/client-tags/typing.html) is now an IRCv3 draft. This feature allows clients to send and receive typing notifications, which can make conversations richer

On our roadmap, we're working on:

- The [Standard Replies extension](https://github.com/ircv3/ircv3-specifications/pull/357) which lets us respond with information, warnings, and command errors in a more consistent way.
- The [Account Management Framework](https://github.com/ircv3/ircv3-specifications/pull/276) which lets users register for accounts using clean, consistent interfaces rather than having to message services bots.
- The [`labeled-response` extension](https://github.com/ircv3/ircv3-specifications/pull/378), which lets client software properly track and handle responses to their commands.
- The [`resume` extension](https://github.com/ircv3/ircv3-specifications/pull/306), which lets users reconnect and get back to chatting more quickly and cleanly if their connection drops.

We've cleaned up and refreshed our support tables, and the footer of each specification now shows which software supports it.

Lastly, some changes to our technical board. We aim to maintain an active, broad and representative mix of board members to steer the working group. NoOneButMe from the Colloquy project has had other priorities outside of IRCv3 lately, and has stepped down. In their place we're welcoming justjanne from [Quassel](https://quasseldroid.info/) onto the board.

There's been a lot of progress this past year, and even more to come. Thanks to our wonderful contributors for the help, and to the IRC community in general.

We're always looking for help with our [roadmap](https://github.com/ircv3/ircv3-specifications/milestone/4), as well as more [general suggestions](https://github.com/ircv3/ircv3-ideas)! If you're interested in chatting, we hang out on [`irc.freenode.net/#ircv3`](https://ircv3.net/contact.html).
