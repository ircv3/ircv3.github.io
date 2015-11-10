---
layout: page
title: Libraries
meta-description: IRCv3 Library Support. This page lists the IRC libraries compatible with and supporting IRCv3 features.
---
This software is compliant natively; other software may be compliant with extensions.

{% for type in site.data.sw_libraries %}
{% include software_list.html %}
{% endfor %}
