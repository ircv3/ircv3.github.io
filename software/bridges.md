---
layout: page
title: Bridges
meta-description: IRCv3 Bridges Support. This page lists gateways to and from other protocols, which are compatible with and supporting IRCv3 features.
data-source-filename: sw_bridges.yml
page-header: >
  IRCv3 Bridges Support
---
{% include software_intro.html %}

"N/A" indicates the bridged platform(s) does not support an equivalent of a given specification.

{% for type in site.data.sw_bridges %}
{% include software_list.html %}
{% endfor %}

