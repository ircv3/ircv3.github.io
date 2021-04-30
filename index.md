---
layout: default
title: Welcome
meta-description: Welcome to the IRCv3 Working Group. We're a group of IRC client and server software authors working to improve the IRC protocol.
page-header: >
  Open, extensible, feature-rich chat,


  proven through years of use.
---
<div class="row frontpage pure-g">
  <div class="pure-u-1-3">
    <h2>Specifications</h2>
    <hr>
    <p>
      These are the specifications which make up modern IRC, and the extensions that the IRCv3 WG have defined.
    </p>
    <a class="button" href="{{ site.baseurl }}/irc/">
      View
    </a>
  </div>
  <div class="pure-u-1-3">
    <h2>Working Group</h2>
    <hr>
    <p>
      The IRCv3 Working Group is chartered to prototype, develop and test changes to the IRC client protocol.
    </p>
    <a class="button" href="{{ site.baseurl }}/wg.html">
      View
    </a>
  </div>
  <div class="pure-u-1-3">
    <h2>FAQs</h2>
    <hr>
    <p>
      These are questions about IRC and the IRCv3 Working Group that we get asked regularly, and our answers.
    </p>
    <a class="button" href="{{ site.baseurl }}/faq.html">
      View
    </a>
  </div>
</div>


## Introduction

If you’re just getting started with IRC development, the first thing to look at would be the IRC core specifications [`RFC1459`](https://tools.ietf.org/html/rfc1459) and [`RFC2812`](https://tools.ietf.org/html/rfc2812). One of our members has also been writing a new core protocol document [here](https://modern.ircdocs.horse), which you may find useful to consult. After that, our [specifications page]({{ site.baseurl }}/irc/) contains the extensions the IRCv3 Working Group has developed.

All of the IRCv3 extensions are backwards-compatible with older IRC clients, and older IRC servers. Our [roadmap](https://github.com/ircv3/ircv3-specifications/milestone/4) details the specifications we have in the pipeline, and our [GitHub repository](https://github.com/ircv3/ircv3-specifications) is where most of our specification work is done.

For any other questions, feel free to consult our [FAQ page]({{ site.baseurl }}/faq.html) which contains all sorts of info about us and what we do.

If you’re interested in talking with us, our discussion channel is [#ircv3 on Freenode](ircs://irc.freenode.net:6697/#ircv3) <sup>[[webchat]](https://kiwiirc.com/client/irc.freenode.net:+6697/#ircv3)</sup>.


## IRCv3 Features

- Standardised account login using SASL to speed up registration and authentication. <sup>[[3.1]]({{ site.baseurl }}/specs/extensions/sasl-3.1.html)</sup> <sup>[[3.2]]({{ site.baseurl }}/specs/extensions/sasl-3.2.html)</sup>
- Providing the account information of other clients for the development of more advanced client features. <sup>[[1]]({{ site.baseurl }}/specs/extensions/account-notify.html)</sup> <sup>[[2]]({{ site.baseurl }}/specs/extensions/account-tag.html)</sup> <sup>[[3]]({{ site.baseurl }}/specs/extensions/extended-join.html)</sup>
- Optional metadata able to be attached to each message for easier, standardised extension development. <sup>[[link]]({{ site.baseurl }}/specs/extensions/message-tags.html)</sup>
- Instant away notifications, to let users know when other users go away or come back more quickly. <sup>[[link]]({{ site.baseurl }}/specs/extensions/away-notify.html)</sup>
- Showing the actual time a message was received, improving history playback from IRC bouncers. <sup>[[link]]({{ site.baseurl }}/specs/extensions/server-time.html)</sup>
- Grouping related messages to simplify collapsing and display of those messages to users. <sup>[[link]]({{ site.baseurl }}/specs/extensions/batch.html)</sup>


## What We're Working On

- Standardised account registration and verification, allowing clients to provide better interfaces for end users. <sup>[[link]](https://github.com/ircv3/ircv3-specifications/pull/435)</sup>
- Giving clients a standardised way to recognise, access and view chat history (provided by bouncers or servers). <sup>[[link]]({{ site.baseurl }}/specs/batches/chathistory.html)</sup>
- Providing a mechanism to allow clients to automatically detect, move to, and keep using secure connections. <sup>[[link]]({{ site.baseurl }}/specs/extensions/sts.html)</sup>
- Allowing Unicode nicknames and channel names, improving the chat experience for international users. <sup>[[link]](https://github.com/ircv3/ircv3-specifications/pull/272)</sup>
- Client avatars for display in graphical clients.


## Participating Organizations

<div class="flexy-list">
  {% for participant in site.data.participants %}
  <a class="participant" href="{{ participant.url }}">{{ participant.name }}</a>
  {% endfor %}
</div>
