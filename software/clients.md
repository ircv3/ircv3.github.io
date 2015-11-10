---
layout: page
title: Clients
meta-description: IRCv3 Client Support. This page lists the IRC clients compatible with and supporting IRCv3 features.
---
This software is compliant natively; other software may be compliant with extensions.

{% for type in site.data.sw_clients %}
* [{{ type.name }}](#{{ type.name }})
{% endfor %}

{% for type in site.data.sw_clients %}
{% include software_list.html %}
{% endfor %}
