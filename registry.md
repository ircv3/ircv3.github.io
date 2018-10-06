---
title: IRCv3 Registry
layout: default
meta-description: IRCv3 Tags, Capabilities, Commands and Metadata Keys.
page-header: >
  IRCv3 Registry
---

This page lists the tags, capabilities, commands, batches and metadata keys that have been defined by the IRCv3 Working Group, are described by our specifications, or that we otherwise recommend using.

<div class="irc-sw-list flexy-list">
{% for type in site.data.registry %}
<a href="#{{ type.name | slugify }}">{{ type.name }}</a>
{% endfor %}
</div>

<hr>

{% for type in site.data.registry %}
<h2 id="{{ type.name | slugify }}">{{ type.name }}</h2>
<table>
  <thead>
    <tr>
      {% if type.include_numeric %}<th style="text-align: center">Numeric</th>{% endif %}
      <th>Name</th>
      {% if type.include_specs %}<th>Specs</th>{% endif %}
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    {% for val in type.values %}
    <tr>
      {% if type.include_numeric %}<td style="min-width: 5rem; text-align: center">
        <code>{{ val.numeric }}</code>
      </td>{% endif %}
      <td style="min-width: 10rem"{% if type.nomono %}{% else %} class="mono"{% endif %}>{{ val.name }}</td>
      {% if type.include_specs %}<td style="min-width: 13rem">
        {% for specname in val.specs %}
          <a class="{% if site.data.specs[specname].deprecated %}deprecated{% endif %} {% if site.data.specs[specname].draft %}draft{% endif %}" title="{{ site.data.specs[specname].name }}" href="{{ site.baseurl }}/specs{{ site.data.specs[specname].url }}">{{ site.data.specs[specname].shortname }}</a>{% if site.data.specs[specname].deprecated %}<sup> [deprecated]</sup>{% endif %}{% if site.data.specs[specname].draft %}<sup> [draft]</sup>{% endif %}{% if forloop.last %}{% else %},{% endif %}
        {% endfor %}
      </td>{% endif %}
      <td>
        {{ val.description | markdownify | replace:"<p>","" | replace:"</p>","" }}
        {% assign i = 1 %}
        {% for link in val.links %}
          <sup><a href="{{ site.baseurl }}{{ link }}">({{i}})</a></sup>
          {% assign i = i | plus: 1 %}
        {% endfor %}
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>
{% endfor %}

{% include anchors.html %}
