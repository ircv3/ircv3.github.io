---
title: IRCv3 Registry
layout: default
meta-description: IRCv3 Tags, Capabilities, Commands and Metadata Keys.
page-header: >
  IRCv3 Registry
---

This page lists the tags, capabilities, commands and metadata keys that have been defined by the IRCv3 Working Group, or are otherwise described by our specifications.

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
      <th>Name</th>
      <th>Specs</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    {% for val in type.values %}
    <tr>
      <td style="min-width: 10rem"{% if type.nomono %}{% else %} class="mono"{% endif %}>{{ val.name }}</td>
      <td style="min-width: 13rem">
        {% for specname in val.specs %}
          <a class="{% if site.data.specs[specname].deprecated %}deprecated{% endif %} {% if site.data.specs[specname].draft %}draft{% endif %}" title="{{ site.data.specs[specname].name }}" href="{{ site.baseurl }}/specs{{ site.data.specs[specname].url }}">{{ site.data.specs[specname].shortname }}</a>{% if site.data.specs[specname].deprecated %}<sup> [deprecated]</sup>{% endif %}{% if site.data.specs[specname].draft %}<sup> [draft]</sup>{% endif %}{% if forloop.last %}{% else %},{% endif %}
        {% endfor %}
      </td>
      <td>{{ val.description | markdownify | replace:"<p>","" | replace:"</p>","" }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
{% endfor %}

{% include anchors.html %}
