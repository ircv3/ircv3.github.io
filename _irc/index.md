---
layout: page
title: IRCv3 Specifications
excerpt: IRCv3 Specifications
index: true
---

{% for spec in site.irc %}
{% if spec.index != true %}

## {{spec.title}}

{{spec.content}}

{% endif %}
{% endfor %}
