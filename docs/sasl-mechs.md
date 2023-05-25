---
layout: page
title: SASL Mechanisms
meta-description: SASL Mechanisms for the IRCv3 'sasl' capability.
page-header: >
  IRCv3 SASL Mechanisms
---
IRC SASL authentication primarily uses the same mechanisms as SASL in other protocols. Most commonly:

* [PLAIN](https://tools.ietf.org/search/rfc4616) as defined by RFC 4616
* [EXTERNAL](https://tools.ietf.org/html/rfc4422#appendix-A) as defined by RFC 4422
* [SCRAM-SHA-256](https://tools.ietf.org/html/rfc7677) as defined by RFC 7677

{% for type in site.data.sw_clients %}
### {{ type.name }}
{% for support in site.data.doc_sasl %}
{% include support_list.html %}
{% endfor %}
{% endfor %}

{% for type in site.data.sw_libraries %}
### {{ type.name }}
{% for support in site.data.doc_sasl %}
{% include support_list.html %}
{% endfor %}
{% endfor %}

{% for type in site.data.sw_services %}
### {{ type.name }}
{% for support in site.data.doc_sasl %}
{% include support_list.html %}
{% endfor %}
{% endfor %}
