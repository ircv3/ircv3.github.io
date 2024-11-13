---
layout: post
title: 2024 Spec round-up

---

2023 had been a slow year, so we skipped on our traditional annual update, but it is back this year. here's a summary of everything that's been happening since Nov 2022.
Most of the progress these last two years have been around making [`chathistory`](https://ircv3.net/specs/extensions/chathistory) more suitable for the real world, and reducing bandwidth usage for mobile clients.

### Specs ratified

Sadly, none during this time span. We'll try to do better next year.

### New drafts

* Aug 2023 [`pre-away`](https://ircv3.net/specs/extensions/pre-away) - Allows clients to update - or not update - their AWAY status early in the connection, when connecting to a bouncer or server that supports multiple connections per user [#514](https://github.com/ircv3/ircv3-specifications/pull/514)
* Oct 2023 [`no-implicit-names`](https://ircv3.net/specs/extensions/no-implicit-names) - Allows clients to opt out from receiving the user list when joining a channel. This is useful for clients with limited bandwith, to defer loading the user list to the time it is needed, or the connection is less busy; or to avoid redundancy with [WHOX](https://ircv3.net/specs/extensions/whox) [#527](https://github.com/ircv3/ircv3-specifications/pull/527)
* Apr 2024 [`message-redaction`](https://ircv3.net/specs/extensions/message-redaction)- Allows removing messages from the chat history, or to ask other clients to hide a message [#524](https://github.com/ircv3/ircv3-specifications/pull/524), [#538](https://github.com/ircv3/ircv3-specifications/pull/538)
* Jul 2024 [`account-extban`](https://ircv3.net/specs/extensions/account-extban) - Standardizes support most servers already had for banning accounts (rather than hostmasks), through a new ISUPPORT token [#464](https://github.com/ircv3/ircv3-specifications/pull/464)
* Sep 2024 [`metadata-2`](https://ircv3.net/specs/extensions/metadata) - Latest incarnation of a specification meant to support arbitrary public information on users. The previous version of this specification was deprecated in 2016 due to performance issues [#501](https://github.com/ircv3/ircv3-specifications/pull/501)

### Specs updated

* Feb 2023 [Standard Replies](https://ircv3.net/specs/extensions/standard-replies) - Added `standard-replies` capability, indicating clients support arbitrary `FAIL`/`WARN`/`NOTE` messages, even when not explicitly allowed by another capability [#506](https://github.com/ircv3/ircv3-specifications/pull/506)
* Feb 2023 [`chathistory`](https://ircv3.net/specs/extensions/chathistory) - Added `MSGREFTYPES` ISUPPORT token for servers to signal whether they support/prefer message ids or timestamps to refer to points in the history. This was done because in practice, most server implementations have a strong preference for one or the other. [#510](https://github.com/ircv3/ircv3-specifications/pull/510)
* Sep 2023 [Capability negotiation](https://ircv3.net/specs/extensions/capability-negotiation) - Clarified that servers may add trailing spaces at the end of capability lists [#530](https://github.com/ircv3/ircv3-specifications/pull/530)
* Sep 2023 [`away-notify`](https://ircv3.net/specs/extensions/away-notify) - Clarified that clients should not be sent notifications for their own changes in AWAY status [#531](https://github.com/ircv3/ircv3-specifications/pull/531)

### On the Roadmap

Highlights from our ongoing [roadmap](https://github.com/ircv3/ircv3-specifications/milestone/4) milestone

* ratify CHATHISTORY [#437](https://github.com/ircv3/ircv3-specifications/issues/437)
* ratify websocket [#548](https://github.com/ircv3/ircv3-specifications/pull/548), after resolving the issue of encoding [#551](https://github.com/ircv3/ircv3-specifications/pull/551)
* Message editing and deletion [#425](https://github.com/ircv3/ircv3-specifications/pull/425)

### Other

We now have an account on the Fediverse, follow us at [@ircv3@mastodon.social](https://mastodon.social/@ircv3).

We updated the [specifications page]({{ site.baseurl }}/irc/) to replace [`RFC1459`](https://tools.ietf.org/html/rfc1459), [`RFC2812`](https://tools.ietf.org/html/rfc2812) and [`RFC7194`](https://tools.ietf.org/html/rfc7194) with ["Modern IRC"](https://modern.ircdocs.horse/) as the base specification IRCv3 builds upon. The latter has matured enough in recent years that we are confident it is a strict improvement over the RFCs in terms of accuracy and completeness. [#469](https://github.com/ircv3/ircv3.github.io/pull/469)

Finally, we recommend you check out [Sable](https://github.com/Libera-Chat/sable), an interesting new IRCd developed by Libera.Chat, with built-in services and gossiping instead of a spanning-tree.
