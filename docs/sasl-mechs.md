---
layout: page
title: SASL Mechanisms
meta-description: SASL Mechanisms for the IRCv3 'sasl' capability.
---
IAL primarily uses the same mechanisms as SASL in other protocols. Most commonly:

* [PLAIN](https://tools.ietf.org/search/rfc4616) as defined by RFC 4616
* [EXTERNAL](https://tools.ietf.org/html/rfc4422#appendix-A) as defined by RFC 4422
* [SCRAM-SHA-256](https://tools.ietf.org/html/draft-hansen-scram-sha256-02)

### Client Support

{% for type in site.data.sw_clients %}
{% assign support_name = type.name %}
{% for support in site.data.doc_sasl %}
{% include support_list.html %}
{% endfor %}
{% endfor %}

### Services Support

{% for type in site.data.sw_services %}
{% assign hide_support_name = true %}
{% for support in site.data.doc_sasl %}
{% include support_list.html %}
{% endfor %}
{% endfor %}
