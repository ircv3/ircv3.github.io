---
layout: page
title: Libraries
meta-description: IRCv3 Library Support. This page lists the IRC libraries compatible with and supporting IRCv3 features.
data-source-filename: sw_libraries.yml
page-header: >
  IRCv3 Library Support
---
{% include software_intro.html %}

{% assign hide_support_name = true %}
{% for type in site.data.sw_libraries %}
{% include software_list.html %}
{% endfor %}
