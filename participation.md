---
title: Participation
layout: page
---
The IRCv3 working group contains participants from the following organizations (and more):

<div class="flexy-list">
{% for participant in site.data.participants %}
<a class="participant" href="{{ participant.url }}">{{ participant.name }}</a>
{% endfor %}
</div>

<br/>

To participate, contribute to our specifications and extensions registry on [GitHub](http://github.com/ircv3/ircv3-specifications).

<br/>

You may also contact us on [irc.freenode.net in #ircv3](irc://irc.freenode.net/ircv3)
