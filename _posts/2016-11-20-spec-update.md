---
layout: post
title: Specification Update
---
We've got a lot done recently! Let's go through all of the latest changes.

First off, the message intents draft was replaced with `message-tags`[<sup>[spec]</sup>](https://ircv3.net/specs/core/message-tags-3.3.html). The new draft `message-tags` cap and semantics are more useful than intents, allowing features to be implemented by clients themselves (similar to CTCP) and also codifying some of the existing meta around clients/servers parsing all well-formed tags.

If you've missed it, the Strict Transport Security (STS) draft [<sup>[link]</sup>](https://ircv3.net/specs/extensions/sts.html) is also on the site, and some [testnets](https://ircv3.net/support/networks.html) have support for it as `draft/sts`. The aim of STS is to allow clients to automatically upgrade their plaintext connections to TLS and to subsequently prevent downgrade attacks.

On a related note, the SNI draft [<sup>[link]</sup>](https://ircv3.net/specs/core/sni-3.3.html) is also now on the site, and should help servers present the right certificate to connecting clients.

It was clarified that all message tag / capability / batch names must be handled as opaque identifiers [<sup>[pr]</sup>](https://github.com/ircv3/ircv3-specifications/pull/274/files). This was already assumed by most, but is a useful clarification to make for implementors.

Draft capability names now use the `draft/` prefix to denote their status, and to improve transition if specs change before being merged in proper [<sup>[pr]</sup>](https://github.com/ircv3/ircv3-specifications/pull/277).

IRCv3.2 Metadata has been **deprecated** [<sup>[pr]</sup>](https://github.com/ircv3/ircv3-specifications/pull/279). The new version of [Metadata](https://github.com/ircv3/ircv3-specifications/pull/250) will extend the rate-limiting and notification capabilities of this spec, letting it be implemented in a much more efficient way by the larger IRC servers.

And for proposals, an [`rfc7700` casemapping PR](https://github.com/ircv3/ircv3-specifications/pull/272) has been submitted, which would allow nicknames and channel names to contain Unicode characters. As well, an [extended message length PR](https://github.com/ircv3/ircv3-specifications/pull/281) has been submitted, which would allow servers to accept and send larger IRC messages.
