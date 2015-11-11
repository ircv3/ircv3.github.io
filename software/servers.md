---
layout: page
title: Servers
meta-description: IRCv3 Server Support. This page lists the IRC servers compatible with and supporting IRCv3 features.
---
This software is compliant natively; other software may be compliant with extensions.

{% for type in site.data.sw_servers %}
{% include software_list.html %}
{% endfor %}
