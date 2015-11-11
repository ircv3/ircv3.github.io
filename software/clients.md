---
layout: page
title: Clients
meta-description: IRCv3 Client Support. This page lists the IRC clients compatible with and supporting IRCv3 features.
---
This software is compliant natively; other software may be compliant with extensions.

<div class="irc-sw-list flexy-list">
{% for type in site.data.sw_clients %}
<a href="#{{ type.name | slugify }}">{{ type.name }}</a>
{% endfor %}
</div>

{% for type in site.data.sw_clients %}
{% include software_list.html %}
{% endfor %}
