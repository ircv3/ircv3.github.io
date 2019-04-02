---
layout: page
title: Batch Types
meta-description: IRCv3 batch type support.
page-header: >
  IRCv3 Batch Types
---

### Client Support

{% for type in site.data.sw_clients %}
{% assign support_name = type.name %}
{% for support in site.data.doc_batch %}
{% include support_list.html %}
{% endfor %}
{% endfor %}

{% for type in site.data.sw_libraries %}
{% assign support_name = type.name %}
{% for support in site.data.doc_batch %}
{% include support_list.html %}
{% endfor %}
{% endfor %}

### Server Support

{% for type in site.data.sw_servers %}
{% assign hide_support_name = true %}
{% for support in site.data.doc_batch %}
{% include support_list.html %}
{% endfor %}
{% endfor %}
