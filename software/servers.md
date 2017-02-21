---
layout: page
title: Servers
meta-description: IRCv3 Server Support. This page lists the IRC servers compatible with and supporting IRCv3 features.
data-source-filename: sw_servers.yml
---
{% include software_intro.html %}

{% assign hide_support_name = true %}
{% for type in site.data.sw_servers %}
{% include software_list.html %}
{% endfor %}
