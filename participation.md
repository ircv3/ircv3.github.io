---
title: Participation
layout: page
meta-description: The IRCv3 working group contains participants from many organizations involved with IRC software development.
page-header: >
  IRCv3 Working Group Participation
---
The IRCv3 working group contains participants from the following organizations (and more):

<div class="flexy-list">
{% for participant in site.data.participants %}
<a class="participant" href="{{ participant.url }}">{{ participant.name }}</a>
{% endfor %}
</div>

<br/>

The following organizations observe the working group and/or implement IRCv3 specifications:

<div class="flexy-list">
{% for participant in site.data.consumers %}
<a class="participant" href="{{ participant.url }}">{{ participant.name }}</a>
{% endfor %}
</div>

<br/>

To participate, contribute to our specifications and extensions registry on [GitHub](https://github.com/ircv3/ircv3-specifications).

<br/>

You may also contact us on [irc.libera.chat in #ircv3](ircs://irc.libera.chat/ircv3)
