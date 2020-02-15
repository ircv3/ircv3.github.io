---
layout: post
title: Labels, Message IDs and History
---
There's been a bunch of newly-submitted proposals recently, looking at everything from history retrieval with bouncers to message reactions. Let's go over the holiday changes.

The `labeled-response` draft [<sup>[link]</sup>](https://ircv3.net/specs/extensions/labeled-response.html) was added. This draft links sent commands to returned numerics/messages much more effectively for clients, allowing more complete implementations of `echo-message`.

The `message-ids` draft [<sup>[link]</sup>](https://ircv3.net/specs/extensions/message-ids.html) was added. This draft provides a network-unique identifier on messages, which allows many new and exciting features to be built! This includes the `reply`, `reaction`, and `chathistory` proposals below.

The `sts` draft is getting an upgrade with the `preload` key [<sup>[link]</sup>](https://github.com/ircv3/ircv3-specifications/pull/295), which should allow IRC networks to specify whether they want their STS policy added into preload lists shipped with clients. In addition to what STS already provides, this contributes towards helping make clients more secure.

The new message tags specification is also getting an update [<sup>[link]</sup>](https://github.com/ircv3/ircv3-specifications/pull/287). Currently being looked at is exactly how to specify client-only tags, and increasing the current minimum-bound of 512 bytes for tag space.

In terms of proposals, a [`reaction` PR](https://github.com/ircv3/ircv3-specifications/pull/289) has been submitted, which allows clients to add their 'reactions' to specific messages. This feature is already widely-implemented in other messaging protocols, and puts IRC on a more equal footing against them.

As well, a [`chathistory` PR](https://github.com/ircv3/ircv3-specifications/pull/292) has been submitted, which allows clients to query servers/bouncers for chat history. This feature has been desired in bouncers for a while, and should also make it possible for certain clients to implement infinite-scroll style history retrieval.

A [`reply` PR](https://github.com/ircv3/ircv3-specifications/pull/288) has also been submitted. It allows clients to note that a message is intended as a reply to another sent message. In addition to allowing features such as the `reaction` tag above, it also brings up the possibility of a more thread-like view of conversations.
