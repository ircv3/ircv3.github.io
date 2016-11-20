---
layout: page
title: IRCv3 Specifications
excerpt: IRCv3 Specifications
index: true
---

Right now the IRCv3 specification is distributed as a series of extension
specifications to IRC protocol version 2.7, also known as
[RFC1459](http://tools.ietf.org/html/rfc1459). To understand the basis of the
IRC version 3 protocol, please read RFC1459 followed by the extension
specifications.

IRCv3 is based on a set of specifications; initially these specifications were
released as a versioned distribution but now specifications are released when
they're ready and errata corrections are amended when needed.

This is the current stable version of the IRC protocol.  Errata updates may be
submitted for the specifications.

## Base Extensions

Base extensions are specifications written that are considered essential to the
protocol. They should be supported by all IRC clients as they are either the
foundation of further specifications or are a very widely used feature.

### Capability Negotiation

Currently there's two specifications for capability negotiation. The first one
is considered the 3.1 version of the protocol, whereas the second is considered
the 3.2 version of the protocol.

[Version 3.1]({{site.baseurl}}/specs/core/capability-negotiation-3.1.html)
offers a simple way to request what capabilities the server supports. Using the
`CAP` command offers an interface to listing extensions the server supports as
well as requesting usage of that extension.

[Version 3.2](http://ircv3.net/specs/core/capability-negotiation-3.2.html) has
some additional features including the ability to store values in any listed
capabilities, replying with multiple lines of capabilities, and two subcommands
`NEW` and `DEL`, which state that a server has added support for and removed
support for an extension respectively.

### [Message Tags](http://ircv3.net/specs/core/message-tags-3.2.html)

Message tags are a way to send metadata about a command, typically used with a
user-to-user interaction. For example, when joining, a tag could specify the
[account name](http://ircv3.net/specs/extensions/account-tag-3.2.html)) of a
user. Tags are formatted as `key[=value]` pairs, where the value is optional.

**Note:** A [new extension](http://ircv3.net/specs/core/message-tags-3.3.html)
is currently being drafted. The new extension specification will offer support
for tags sent from the client to the server, and for servers to send tags sent
from clients, to other clients, regardless of whether or not they requested
support for the tag.

**Note:** This extension is meant to be a foundation on other extensions and
does not offer anything "user-facing".

### [Monitor](http://ircv3.net/specs/core/monitor-3.2.html)

The `MONITOR` command acts as a standardized low-bandwidth solution for the
`ISON` and `WATCH` commands. It acts as an interface to add and remove users
from a monitoring list and can also be used to check the status of the list of
monitored users.

### [Multi Prefix]({{site.baseurl}}/specs/extensions/multi-prefix-3.1.html)

The `multi-prefix` capability manipulates the values that `NAMES` and `WHO`
returns. The nick, which is preceded by zero or one prefixes indicating status
(voice, op, etc.) can now optionally be preceded by unlimited prefixes ordered
from highest rank to lowest.

### [SASL]({{site.baseurl}}/specs/extensions/sasl-3.1.html)

The SASL capability offers an `AUTHENTICATE` command which initially acts as a
way to specify a mechanism. Afterwards, the SASL mechanism authenticates the
user. The specification also documents multiple numerics used for specifying
successes and errors during the authentication transaction.

**Note:** [The 3.2 version](http://ircv3.net/specs/extensions/sasl-3.2.html)
advertises with the value set to a list of comma delimited supported
mechanisms. However, clients must attempt to use the 3.1 version of the
protocol if the 3.2 version is not supported. Clients can determine whether a
server supports version 3.1 or 3.2 by checking if the capability is advertised
with a value.

## Optional Extensions

Optional extensions should also be implemented but are not essential components
of IRCv3. IRCv3 will work fine without the below extensions but the extensions
help improve the user experience.

### [Account Notify]({{site.baseurl}}/specs/extensions/account-notify-3.1.html)

The `account-notify` extension (along with the `extended-join` extension and
the `WHOX` command) allow for the ability to constantly monitor the account a
user is logged into. `account-notify` in particular offers an `ACCOUNT` command
for the server to send to the client when a user either logs into an account or
logs out of their current account.

### [Account Tag](http://ircv3.net/specs/extensions/account-tag-3.2.html)

The `account-tag` extension adds a tag to the `PRIVMSG` command that is used to
identify the account the user is logged into at the current time. This covers a
use case where a user is talking with another user and both users do not share
a channel, which - when paired with the above mentioned extensions - offers a
way to view the account of a user no matter what.

The tag is sent with any commands sent from a user that interact with another
user, including `PRIVMSG`, `MODE`, and other commands.

### [Away Notify]({{site.baseurl}}/specs/extensions/away-notify-3.1.html)

This extension adds the `AWAY` command which is sent to clients that share a
channel with a user, when the user marks themselves as either away or not away.

### [Batch](http://ircv3.net/specs/extensions/batch-3.2.html)

This extension adds a new tag (`batch`) along with a new command (`BATCH`). The
`BATCH` command specifies the beginning or the end of a "batch" of messages,
while the `batch` tag specifies which "batch" of messages the current message
belongs to. Messages not in a batch will not contain the tag.

**Note:** This extension is meant to be a foundation on other extensions and
does not offer anything "user-facing".

### [Cap Notify](http://ircv3.net/specs/extensions/cap-notify-3.2.html)

The `cap-notify` extension is a "proxy" capability that can be requested to
allow usage of the `CAP` subcommands `ADD` and `DEL` (see above). The commands
can be used when a server adds or removes support for a capability.

### [chghost](http://ircv3.net/specs/extensions/chghost-3.2.html)

This extension adds a `CHGHOST` command whose arguments list the new user and
host for the user, or the old user or host if none changed (looks like
`ryan!awesome@ny1.hashbang.sh CHGHOST awesome to1.hashbang.sh`). This is useful
for servers that support the ability to change their hostname or ident.

### [Echo Message](http://ircv3.net/specs/extensions/echo-message-3.2.html)

The `echo-message` extension sends the message that the user sent to a channel
back to the user who sent it. This can be useful for confirming a message was
sent or to include information cut off of a previous message.

### [Extended Join]({{site.baseurl}}/specs/extensions/extended-join-3.1.html)

The `extended-join` capability modifies the `JOIN` command to include two more
parameters. The first is the account name (`*` if the user is not signed in)
and the trailing parameter contains the user's GECOS information, also known
as the `realname`.

### [Invite Notify](http://ircv3.net/specs/extensions/invite-notify-3.2.html)

This specification standardizes the `INVITE` command and adds a server-sent
`INVITE` command that notifies a user that they were invited to a channel. The
command specifies a target - the nick of the user invited to the channel - and
the channel the user has been invited to.

### [Server Time](http://ircv3.net/specs/extensions/server-time-3.2.html)

The `server-time` extension specifies the time that the message was received by
the server. This can be useful to list the time was received when replaying
logs from a bouncer.

### [STARTTLS](http://ircv3.net/specs/extensions/tls-3.1.html)

This extension adds a `STARTTLS` command that, when replied to by the server,
will start a TLS handshake between the client and the server. This will encrypt
the user's connection and make it safer to send passwords and other information
when the client is registering. It's also recommended to configure the client
to automatically connect with TLS when this capability is advertised.

### [Userhost In Names](http://ircv3.net/specs/extensions/userhost-in-names-3.2.html)

The `userhost-in-names` capability modifies the `NAMES` replies to include the
full hostmask (`nick!user@host`) of the users listed. This is useful to gain
information about the user without having to query the channel.

### [STS](http://ircv3.net/specs/core/sts-3.3.html)

Strict Transport Security, based off the web version HSTS, allows for clients
to automatically configure TLS and other encryption features based off of the
capability list. The `sts` capability will list a duration for the policy to
last as well as a network port. Clients should also allow users to specify the
TLS information themselves to avoid "Man In The Middle" bootstrap attacks.

### [SNI](http://ircv3.net/specs/core/sni-3.3.html)

Server Name Indication is a transparent extension that is used when clients
connect to a server using TLS 1.1+. Server name indication helps the server
identify which certificate should be used when connecting, to help avoid
errors.

## Deprecated Extensions

### [Metadata](http://ircv3.net/specs/core/metadata-3.2.html)

The metadata command, which initially allowed users to make information about
themselves more accessible, has encountered a barrier with rate limiting and
spam detection. The extension has been deprecated and a better solution will
eventually be replacing the extension.
