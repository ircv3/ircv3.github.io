---
layout: post
title: Spec round-up
---
Following our tradition of the annual update, here's a summary of everything that's been happening since Feb 2020. And it's quite a lot!

### Specs ratified

* Feb 2020 [setname](https://ircv3.net/specs/extensions/setname.html) - Allows users to change their realname without reconnecting
* May 2020 [Typing notifications](https://ircv3.net/specs/client-tags/typing.html) - Displays to others when you're typing
* Apr 2021 [UTF8ONLY isupport key](https://ircv3.net/specs/extensions/utf8-only.html) [#432](https://github.com/ircv3/ircv3-specifications/pull/432) - Indicates that server will only accept UTF8 encoded messages

### New drafts

* Apr 2020 [Multiline messages](https://ircv3.net/specs/extensions/multiline.html) [#398](https://github.com/ircv3/ircv3-specifications/pull/398) - Allows multiple lines per message
* Sep 2020 [Channel renaming](https://ircv3.net/specs/extensions/channel-rename.html) [#420](https://github.com/ircv3/ircv3-specifications/pull/420) - Enables channel renaming
* Nov 2020 [chathistory](https://ircv3.net/specs/extensions/chathistory.html) [#393](https://github.com/ircv3/ircv3-specifications/pull/393) - Allows fetching historical messages from a channel
* Apr 2021 [Bot mode](https://ircv3.net/specs/extensions/bot-mode.html) [#439](https://github.com/ircv3/ircv3-specifications/pull/439) - Indicates that a user is a bot via a mode and WHOIS numeric, and adds a tag to their messages
* Sep 2021 [WebSocket](https://ircv3.net/specs/extensions/websocket.html) [#342](https://github.com/ircv3/ircv3-specifications/pull/342) - Allows web clients to connect to IRC servers directly
* Nov 2021 [Client batches](https://ircv3.net/specs/extensions/client-batch.html) [#454](https://github.com/ircv3/ircv3-specifications/pull/454) - This was split off from multiline into its own framework for use by other specs
* Nov 2021 [Account registration](https://ircv3.net/specs/extensions/account-registration.html) [#435](https://github.com/ircv3/ircv3-specifications/pull/435) - Allows account registration without non-standard bot or services messaging
* Nov 2021 [Extended monitor](https://ircv3.net/specs/extensions/extended-monitor.html) [#466](https://github.com/ircv3/ircv3-specifications/pull/466) - Extends monitor to more commands and notifications

### Specs updated

* May 2020 [Message tags](https://ircv3.net/specs/extensions/message-tags.html) - CLIENTTAGDENY isupport token [#412](https://github.com/ircv3/ircv3-specifications/pull/412)
* Nov 2021 [WebIRC](https://ircv3.net/specs/extensions/webirc.html) - Client certificate fingerprint options [#463](https://github.com/ircv3/ircv3-specifications/pull/463)

### On the Roadmap

Highlights from our ongoing [roadmap](https://github.com/ircv3/ircv3-specifications/milestone/4) milestone

* ratify CHATHISTORY [#437](https://github.com/ircv3/ircv3-specifications/issues/437)
* userip-tag and userhost-tag [#418](https://github.com/ircv3/ircv3-specifications/issues/418)
* Add draft account-extban spec [#464](https://github.com/ircv3/ircv3-specifications/pull/464)
* Message editing and deletion [#425](https://github.com/ircv3/ircv3-specifications/pull/425)
* Display name client tag spec [#452](https://github.com/ircv3/ircv3-specifications/pull/452)