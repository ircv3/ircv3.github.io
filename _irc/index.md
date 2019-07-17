---
layout: page
title: IRCv3 Specifications
excerpt: IRCv3 Specifications
meta-description: Specifications that the IRCv3 Working Group maintains and distributes.
index: true
redirect_from:
    - /irc/3.1.html
    - /irc/3.2.html
    - /irc/3.3.html
page-header: >
  IRCv3 Specifications
---

IRCv3 specifications build on top of the core IRC protocol. The primary core
IRC protocol specifications are [`RFC1459`](http://tools.ietf.org/html/rfc1459),
[`RFC2812`](http://tools.ietf.org/html/rfc2812) and [`RFC7194`](https://tools.ietf.org/html/rfc7194).
To fully understand IRCv3, please read the core IRC protocol specifications
followed by the IRCv3 specifications.

**Note:** The core IRC protocol specifications have been widely acknowledged to
be old, out-of-date, and to not fully or accurately describe how the IRC client
protocol works today. One of our members has been working on updated core
protocol specifications [here](https://modern.ircdocs.horse/) which you may find
useful to consult. Look at core protocol specifications and the IRC ecosystem
itself for a complete picture of how the IRC protocol works today.
If you have any questions on the core IRC protocol, please feel free to ask us
[directly]({{site.baseurl}}/contact.html) or with an issue in our
[feedback](https://github.com/ircv3/ircv3-ideas) GitHub repository.

The IRCv3 specifications are released when they are stable and have been widely
tested. In the past the WG released specifications as versioned bundles
(IRCv3.1, IRCv3.2), but we no longer do this.

Errata updates may be submitted for our specifications. To do so, simply see
our [contribution](https://github.com/ircv3/ircv3-specifications/blob/master/CONTRIBUTING.md)
document.


---


## Capability Negotiation

Capability negotiation is a vital part of IRCv3. Capabilities let us implement
protocol changes in backwards-compatible ways, as well as convey various
information on joining a server.

CAPs are the primary way that IRCv3 features are enabled. As such, most
software implementing IRCv3 extensions will want to implement capability
negotiation.

The [Capability Negotiation spec]({{site.baseurl}}/specs/core/capability-negotiation.html)
conveys the basic listing and requesting of capabilities, and lays the
framework which most IRCv3 specs use. It also goes over the `302` extensions,
and [`cap-notify`]({{site.baseurl}}/specs/core/capability-negotiation.html#cap-notify)
– a feature to make clients aware when capabilities are removed from and added
to the server (for example, if the SASL authentication layer disconnects, the
associated capability may be disabled for a time).


## [Message Tags]({{site.baseurl}}/specs/extensions/message-tags.html)

Message tags extend the core framing used with IRC messages, and allow extended
data to be sent with messages.

Message tags are widely used in the IRCv3 specifications. As such, most
software implementing IRCv3 extensions will want to to implement the core
Message Tags specification.

The [Message Tags spec]({{site.baseurl}}/specs/extensions/message-tags.html)
covers the new message format, how tag data is formatted and escaped, and
how they are named. In addition, it extends the message length and lets
clients send tags directly between each other, allowing new features to be
developed and implemented independently from the IRC servers themselves
(similar to extensions based on CTCP).

**Note:** Message tags themselves are used as a foundation for other extensions
and do not themselves offer any user-facing features. Specific message tags are
defined in the various IRCv3 specifications.


---


## Account Tracking

IRCv3 extensions allow clients to much more easily know when other users are
logged into accounts. This allows for much greater integration between client
bots and the network's authentication system, as well as better general display
and authentication of client identities.

The [`account-notify` spec]({{site.baseurl}}/specs/extensions/account-notify-3.1.html)
defines a way for clients to be notified when other clients login to accounts.
This spec defines the `ACCOUNT` message to enable this, use of the `a` WHOX
token, as well as outlining the general restriction of account names not being
`*` (as this is used to indicate logging out of accounts).

The [`account-tag` spec]({{site.baseurl}}/specs/extensions/account-tag-3.2.html)
defines a way for clients to receive a message tag on messages specifying the
current account that other client is logged into (or that they aren't logged
into one at all). This is especially useful for letting bots make use of the
network's authentication and account mechanisms.

The [`extended-join` spec]({{site.baseurl}}/specs/extensions/extended-join-3.1.html)
defines a way to request that extra client information (including that client's
account) is sent when clients join a given channel. This allows better tracking
of accounts, particularly when used with `account-notify`.


## [Away Notifications]({{site.baseurl}}/specs/extensions/away-notify-3.1.html)

The `away-notify` extension provides a way for clients to instantly know when
other clients go away or come back. This improves responsiveness and the
display of channels for IRC clients that display this information.

The [`away-notify` spec]({{site.baseurl}}/specs/extensions/away-notify-3.1.html)
describes how to sign up for these notifications and the `AWAY` message to
enable this. 


## [Batches]({{site.baseurl}}/specs/extensions/batch-3.2.html)

The `batch` extension provides a way for servers to mark certain messages as
related. This can simplify the display of this information in clients as well
as allow better post-processing on them.

The [`batch` spec]({{site.baseurl}}/specs/extensions/batch-3.2.html) describes
the naming of new batch types, the semantics of batches and how clients should
process them.

**Note:** Batches themselves are used as a foundation for other extensions and
do not themselves offer any user-facing features.

Here are the standalone batch types the IRCv3 WG defines:

* [The `netsplit` and `netjoin` batch types]({{site.baseurl}}/specs/extensions/batch/netsplit-3.2.html) allow clients to collapse netsplits and netjoins more effectively.
* [The `chathistory` batch type]({{site.baseurl}}/specs/extensions/batch/chathistory-3.3.html) allows replaying message history.


## [Changing Usernames and Hostnames]({{site.baseurl}}/specs/extensions/chghost-3.2.html)

The `chghost` extension lets clients more easily see when other clients'
usernames and/or hostnames are changed. This replaces the clunky method of
sending a fake `QUIT`, and then one or more fake `JOIN` messages instead.

The [`chghost` spec]({{site.baseurl}}/specs/extensions/chghost-3.2.html)
describes the new `CHGHOST` message which this extension uses, and how clients
see these changes.


## Client-Only Tags

Client-only tags are message tags that are sent directly between clients with
no server involvement. They're special in IRCv3 as they only apply to clients,
and as such we detail them in their own section here.

Here are the client-only tags the IRCv3 WG defines:

* [The `reply` client-only tag]({{site.baseurl}}/specs/client-tags/reply.html) **[draft]** marks that a given message is intended as a reply to a specific sent message.
* [The `react` client-only tag]({{site.baseurl}}/specs/client-tags/react.html) **[draft]** sends a reaction to a specific sent message, allowing such functionality from other chat systems.
* [The `typing` client-only tag]({{site.baseurl}}/specs/client-tags/typing.html) **[draft]** lets users know when another user is typing a message in their channel or private message.


## [Echo Message]({{site.baseurl}}/specs/extensions/echo-message-3.2.html)

The `echo-message` extension lets clients confirm when messages are sent, and
see messages that other clients on their connection (say, via an IRC bouncer)
have sent. It does this by echoing messages back to clients after they are
sent, allowing for these extra features.

The [`echo-message` spec]({{site.baseurl}}/specs/extensions/echo-message-3.2.html)
describes which messages are echo'd, and how they are interpreted by clients.


## [Invite Notify]({{site.baseurl}}/specs/extensions/invite-notify-3.2.html)

The `invite-notify` extension allows privileged channel users to see when
someone is invited to their channel. This can help chanops better run their
channels and see better information about what's going on.

The [`invite-notify` spec]({{site.baseurl}}/specs/extensions/invite-notify-3.2.html)
describes the new `INVITE` reply which this extension uses, and how clients
interpret these notifications.


## [Labeled Responses]({{site.baseurl}}/specs/extensions/labeled-response.html)

The `labeled-response` extension allows clients to link returned numerics with
sent commands. This allows for much richer/accurate implementations of
`echo-message`, and lets clients generally corrolate sent and received messages.

Additionally, this should also assist bouncers with correctly directing
responses to the right connected client.

The **work-in-progress** [`labeled-response` spec]({{site.baseurl}}/specs/extensions/labeled-response.html)
covers the `draft/label` tag, and how clients should send and will receive
labels.


## [Message IDs]({{site.baseurl}}/specs/extensions/message-ids.html)

The `message-ids` extension allows servers to provide a network-unique
identifier on messages (including `PRIVMSG`/`NOTICE`). This allows clients to
build new features that refer to specific messages, with the knowledge that
these identifiers will be unique.

The [`message-ids` spec]({{site.baseurl}}/specs/extensions/message-ids.html)
covers the `msgid` tag, how servers should generate message IDs and how
clients should treat them.

**Note:** Message IDs themselves are used as a foundation for other extensions
and do not themselves offer any user-facing features. Specific IRCv3
extensions will note their use of (and dependency on) message IDs.


## [Monitor]({{site.baseurl}}/specs/core/monitor-3.2.html)

The `MONITOR` command acts as a standardized way for clients to be alerted when
other clients enter or exit the network. This is in opposition to `ISON`, which
does this through polling, and `WATCH`, which differs between vendor
implementations.

The [Monitor spec]({{site.baseurl}}/specs/core/monitor-3.2.html) details this
command, the relevant `RPL_ISUPPORT` token and the commands used with it.


## [Multiple Prefixes]({{site.baseurl}}/specs/extensions/multi-prefix-3.1.html)

The `multi-prefix` extension allows clients to see all the statuses
(i.e. voice, chanop) that other clients have in a channel rather than just the
highest. This improves data tracking for clients and bots, and allows clients
to display the privilege level of other clients more correctly.

The [`multi-prefix` spec]({{site.baseurl}}/specs/extensions/multi-prefix-3.1.html)
details the exact messages these changes apply to and how exactly it's used.


## SASL Authentication

SASL allows users to authenticate in a standardised way across different IRC
networks. This is in opposition to logging in with 'services' such as NickServ,
and provides a pre-registration way to authenticate. Because SASL allows
authentication before registration, it allows clients to join certain types of
restricted channels much more effectively.

The [v3.1 SASL spec]({{site.baseurl}}/specs/extensions/sasl-3.1.html) defines
the `AUTHENTICATE` command and `sasl` cap, which work together to allow clients
to authenticate to the network.

The [v3.2 SASL spec]({{site.baseurl}}/specs/extensions/sasl-3.2.html) defines
a way to advertise the authentication methods available to clients, allows for
clients to re-authenticate after services is lost and reconnects, and defines
what to do if the authentication layer is disconnected or reconnected.

IRC SASL authentication primarily uses the same mechanisms as SASL in other
protocols. Most commonly:

* [PLAIN](https://tools.ietf.org/search/rfc4616) as defined by RFC 4616
* [EXTERNAL](https://tools.ietf.org/html/rfc4422#appendix-A) as defined by RFC 4422
* [SCRAM-SHA-256](https://tools.ietf.org/html/rfc7677) as defined by RFC 7677

For further information on SASL mechanism support, see the
[SASL Mechanisms page]({{site.baseurl}}/docs/sasl-mechs.html).


## [Server Time]({{site.baseurl}}/specs/extensions/server-time-3.2.html)

The `server-time` extension allows clients to see the exact time that messages
were sent and received. This allows bouncers to replay information with more
accurate time tracking.

The [`server-time` spec]({{site.baseurl}}/specs/extensions/server-time-3.2.html)
describes the `time` tag, how to specify timestamps and how clients should
parse incoming timestamps.


## [Server Name Indication (SNI)]({{site.baseurl}}/specs/core/sni-3.3.html)

SNI makes it easier for servers to send the correct TLS certificate to
connecting clients.

The **work-in-progress** [SNI spec]({{site.baseurl}}/specs/core/sni-3.3.html) provides
guidelines for clients and servers, allowing them to better detect the TLS
certificate to send based on the server's hostname.


## [Setname]({{site.baseurl}}/specs/extensions/setname.html)

Setname allows clients to update their realname (gecos) after connecting to
the server. This is especially useful as some clients use the realname information
for avatars and an additional name field.

The **work-in-progress** [setname spec]({{site.baseurl}}/specs/extensions/setname.html)
describes how this is implemented, and how clients can update their names and see
updates from other users.


## [Strict Transport Security (STS)]({{site.baseurl}}/specs/extensions/sts.html)

STS allows clients to be automatically upgraded to use TLS encryption and
prevents downgrade attacks. STS is intended as a replacement for the `STARTTLS`
command with better security qualities.

The [`sts` spec]({{site.baseurl}}/specs/extensions/sts.html) describes the `sts`
capability, how it operates, and various implementation details for both clients
and servers.


## [Userhosts in NAMES]({{site.baseurl}}/specs/extensions/userhost-in-names-3.2.html)

The `userhost-in-names` extension allows clients to more easily see the
user/hostnames of other clients when joining channels. This allows clients to
better track info and automate client features more easily.

The [`userhost-in-names` spec]({{site.baseurl}}/specs/extensions/userhost-in-names-3.2.html)
describes how the `NAMES` message changes with this capability active, and how
clients should interpret the changes.


## [WebIRC]({{site.baseurl}}/specs/extensions/webirc.html)

The `WEBIRC` command is widely used to provide the real IP address of users
to the server when connecting through a gateway. This is common for current
web-based IRC clients.

The [`WEBIRC` spec]({{site.baseurl}}/specs/extensions/webirc.html)
describes how this command works, how to use it, and some best practices to
keep in mind while implementing this feature.


---


# Deprecated Extensions

These extensions have been explicitly **deprecated**. We no longer recommend
implementing them. Generally, these extensions have either been superseded,
or other major implementation issues have been discovered with them.


## [v3.2 Metadata]({{site.baseurl}}/specs/core/metadata-3.2.html)

The v3.2 `METADATA` command was found to have issues related to rate-limiting
and excessive notifications, which made it impossible for servers in widespread
use to implement. A new Metadata specification is being written to address
these issues and overhaul the notification system, so we do not recommend
implementing this spec.


## [STARTTLS]({{site.baseurl}}/specs/extensions/tls-3.1.html)

STARTTLS allows clients to upgrade their plaintext connections to use TLS
encryption. In alignment with [RFC8314](https://tools.ietf.org/html/rfc8314),
it is recommended that IRC networks use listeners designed for implicit TLS (such
as those that operate on port 6697) and clients instead implement STS support.

The [`tls` spec]({{site.baseurl}}/specs/extensions/tls-3.1.html) is still
available for reference. It describes how the `STARTTLS` command works,
as well as how connection registration is changed by the introduction of
this capability.


{% include anchors.html %}
