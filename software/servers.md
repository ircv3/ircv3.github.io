---
layout: page
title: Servers
meta-description: IRCv3 Server Support. This page lists the IRC servers compatible with and supporting IRCv3 features.
data-source-filename: sw_servers.yml
page-header: >
  IRCv3 Server Support
---
{% include software_intro.html %}

{% for type in site.data.sw_servers %}
{% include software_list.html %}
{% endfor %}
