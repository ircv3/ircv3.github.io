---
layout: post
title: 2022 Spec round-up
---
Following our tradition of the annual update, here's a summary of everything that's been happening since Nov 2021.

### Specs ratified

* Feb 2022 [WHOX](https://ircv3.net/specs/extensions/whox) - Allows clients to request additional information on other clients.
* Apr 2022 [Bot mode](https://ircv3.net/specs/extensions/bot-mode) - Allows identifying clients presenting themselves as bot to other clients
* Oct 2022 [Extended monitor](https://ircv3.net/specs/extensions/extended-monitor) - Extends monitor to more commands and notifications

### New drafts

* Jun 2022 [channel-context client tag](https://ircv3.net/specs/client-tags/channel-context) - Allows sending private messages to clients, while displaying them in the same buffer as a channel
* Jun 2022 [Read marker](https://ircv3.net/specs/extensions/read-marker) - Allows several clients of the same user connected to a server or bouncer to tell each other about which messages have been read in each buffer (channel or query)

### Specs updated

* Nov 2021 [Account registration](https://ircv3.net/specs/extensions/account-registration) - Added `ACCOUNT_REQUIRED` fail code [#481](https://github.com/ircv3/ircv3-specifications/pull/481)
* Oct 2022 [account-tag](https://ircv3.net/specs/extensions/account-tag) - Relaxed requirement that the tag be set on all messages [#505](https://github.com/ircv3/ircv3-specifications/pull/505)

### On the Roadmap

Highlights from our ongoing [roadmap](https://github.com/ircv3/ircv3-specifications/milestone/4) milestone

* ratify CHATHISTORY [#437](https://github.com/ircv3/ircv3-specifications/issues/437)
* userip-tag and userhost-tag [#418](https://github.com/ircv3/ircv3-specifications/issues/418)
* Add draft account-extban spec [#464](https://github.com/ircv3/ircv3-specifications/pull/464)
* Message editing and deletion [#425](https://github.com/ircv3/ircv3-specifications/pull/425)
* Display name client tag spec [#452](https://github.com/ircv3/ircv3-specifications/pull/452)

### Other

We have reorganized the main [specifications page]({{ site.baseurl }}/irc/) to group related specs together in a more logical manner given the recent additions.

Finally, do check the support tables to see how adoption of our specs is coming along, there've been a bunch of busy implementations over the past year; especially [Goguma](https://sr.ht/~emersion/goguma/), a new Android client spearheading many draft specifications.
