---
layout: post
title: New Design, Reactions, and WEBIRC
---
Happy New Year! It's been a while since we've updated, so there's a heap of changes to go through.

First off, in WG news, we've introduced a new site design and a new logo for IRCv3, thanks primarily to [dan-](https://github.com/danieloaks/) and [jwheare](https://github.com/jwheare)! Here's our new logo, in a variety of formats:

<img style="max-width: 100%; width: 55rem; margin: 0 auto; display: block" alt="IRCv3 Logos" src="http://ircv3.net/img/logo-versions.svg">

On the spec side, we've added the new `message-tags` draft [<link>[link]</sup>](https://ircv3.net/specs/core/message-tags-3.3.html) which introduces the `TAGMSG` message, allowing clients to pass metadata to each other freely. This spec also increases the size limit on tags from `512` to `4607` bytes, letting clients have more room to pass each other data.

The `reply` client tag draft [<sup>[link]</sup>](https://ircv3.net/specs/client-tags/reply.html) has been added, which allows clients to specify that a message is in reply to another specific message. This allows for things like the new client tag below!

The `react` client tag draft [<sup>[link]</sup>](https://ircv3.net/specs/client-tags/react.html) allows clients to send a 'reaction' to another message. This is similar to how users in other chat systems can reply to specific messages with emoji and other characters.

The `preload` key was added to STS [<sup>[link]</sup>](https://ircv3.net/specs/extensions/sts.html#the-preload-key), which allows servers to advertise that clients can include it in bundled STS preload lists. We've also ratified STS, so it's fine to implement and use in production!

Finally, we've also added a draft specifying the widespread `WEBIRC` command [<sup>[link]</sup>](https://ircv3.net/specs/extensions/webirc.html). This command is used by web-based IRC clients to pass through the real IP address of a connecting user, and having a concrete specification should help this command stay standard in the future – as well as allowing us to extend it in a backwards-compatible way.
