---
layout: post
title: Spec round-up
---
Following our tradition of the annual update, here's a summary of everything that's been happening since Feb 2020.

### Specs ratified

* Feb 2020 [setname](https://ircv3.net/specs/extensions/setname) - Allows users to change their realname without reconnecting
* May 2020 [Typing notifications](https://ircv3.net/specs/client-tags/typing) - Displays to others when you're typing
* Apr 2021 [UTF8ONLY isupport key](https://ircv3.net/specs/extensions/utf8-only) - Indicates that server will only accept UTF8 encoded messages [#432](https://github.com/ircv3/ircv3-specifications/pull/432)

### New drafts

* Apr 2020 [Multiline messages](https://ircv3.net/specs/extensions/multiline) - Allows multiple lines per message [#398](https://github.com/ircv3/ircv3-specifications/pull/398)
* Sep 2020 [Channel renaming](https://ircv3.net/specs/extensions/channel-rename) - Enables channel renaming [#420](https://github.com/ircv3/ircv3-specifications/pull/420)
* Nov 2020 [chathistory](https://ircv3.net/specs/extensions/chathistory) - Allows fetching historical messages from a channel [#393](https://github.com/ircv3/ircv3-specifications/pull/393)
* Apr 2021 [Bot mode](https://ircv3.net/specs/extensions/bot-mode) - Indicates that a user is a bot via a mode and WHOIS numeric, and adds a tag to their messages [#439](https://github.com/ircv3/ircv3-specifications/pull/439)
* Sep 2021 [WebSocket](https://ircv3.net/specs/extensions/websocket) - Allows web clients to connect to IRC servers directly [#342](https://github.com/ircv3/ircv3-specifications/pull/342)
* Nov 2021 [Client batches](https://ircv3.net/specs/extensions/client-batch) - This was split off from multiline into its own framework for use by other specs [#454](https://github.com/ircv3/ircv3-specifications/pull/454)
* Nov 2021 [Account registration](https://ircv3.net/specs/extensions/account-registration) - Allows account registration without non-standard bot or services messaging [#435](https://github.com/ircv3/ircv3-specifications/pull/435)
* Nov 2021 [Extended monitor](https://ircv3.net/specs/extensions/extended-monitor) - Extends monitor to more commands and notifications [#466](https://github.com/ircv3/ircv3-specifications/pull/466)

### Specs updated

* May 2020 [Message tags](https://ircv3.net/specs/extensions/message-tags) - CLIENTTAGDENY isupport token [#412](https://github.com/ircv3/ircv3-specifications/pull/412)
* Nov 2021 [WebIRC](https://ircv3.net/specs/extensions/webirc) - Client certificate fingerprint options [#463](https://github.com/ircv3/ircv3-specifications/pull/463)

### On the Roadmap

Highlights from our ongoing [roadmap](https://github.com/ircv3/ircv3-specifications/milestone/4) milestone

* ratify CHATHISTORY [#437](https://github.com/ircv3/ircv3-specifications/issues/437)
* userip-tag and userhost-tag [#418](https://github.com/ircv3/ircv3-specifications/issues/418)
* Add draft account-extban spec [#464](https://github.com/ircv3/ircv3-specifications/pull/464)
* Message editing and deletion [#425](https://github.com/ircv3/ircv3-specifications/pull/425)
* Display name client tag spec [#452](https://github.com/ircv3/ircv3-specifications/pull/452)

### Other

We've tidied up the spec structure; making URLs, titles, etc more consistent [#441](https://github.com/ircv3/ircv3-specifications/pull/441). And we've also made a lot of clarifications, improvements and typo fixes to specs that don't materially affect compatibility, too many to list here.

In Aug 2021, The [charter](https://ircv3.net/charter) page had an update to better reflect our loose governance structure, deprecating the concept of the "technical board" and clarifying what it means to be listed as a "contributor" [#399](https://github.com/ircv3/ircv3.github.io/pull/399)

Finally, do check the support tables to see how adoption of our specs is coming along, there've been a lot of busy implementations over the past year.