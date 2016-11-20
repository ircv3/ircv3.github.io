---
layout: post
title: Specification Update
---
We've got a lot done recently! Let's go through all of the latest changes.

First off, the 3.3 draft message intents was replaced with `message-tags`[<sup>[spec]</sup>](http://ircv3.net/specs/core/message-tags-3.3.html), which looks pretty likely to go in as-is [<sup>[pr]</sup>](https://github.com/ircv3/ircv3-specifications/pull/271).

The new draft `message-tags` cap and semantics are more useful than intents, allow more features to be implemented by clients themselves (similar to CTCP) and codify some of the existing meta around clients/servers parsing all well-formed tags.

It was clarified that all message tag / capability / batch names must be handled as opaque identifiers [<sup>[pr]</sup>](https://github.com/ircv3/ircv3-specifications/pull/274/files). This was already assumed by most, but is a useful clarification to make for implementors.

Draft capability names now use the `draft/` prefix to denote their status, and to improve transition if specs change before being merged in proper [<sup>[pr]</sup>](https://github.com/ircv3/ircv3-specifications/pull/277).

IRCv3.2 Metadata has been **deprecated** [<sup>[pr]</sup>](https://github.com/ircv3/ircv3-specifications/pull/279). [IRCv3.3 Metadata](https://github.com/ircv3/ircv3-specifications/pull/250) will extend the rate-limiting and notification capabilities of this spec, letting it be implemented in a much more efficient way by the larger IRC servers.

And for proposals, an [`rfc7700` casemapping PR](https://github.com/ircv3/ircv3-specifications/pull/272) has been submitted, which would allow nicknames and channel names to contain Unicode characters. As well a [extended message length PR](https://github.com/ircv3/ircv3-specifications/pull/281) has been submitted, which would allow servers to accept and send larger IRC messages.
