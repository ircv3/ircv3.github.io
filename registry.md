---
title: IRCv3 Registry
layout: default
meta-description: IRCv3 Tags, Capabilities, Commands and Metadata Keys.
page-header: >
  IRCv3 Registry
---

This page lists the tags, capabilities, commands, batches and metadata keys that have been defined by the IRCv3 Working Group, are described by our specifications, or that we otherwise recommend using. Draft-status names are listed without the `draft/`, as this primarily catalogues reserved names.

<div class="irc-sw-list flexy-list" style="max-width: 60rem;">
{% for type in site.data.registry %}
<a href="#{{ type.name | slugify }}">{{ type.name }}</a>
{% endfor %}
{% for type in site.data.metadata_registry %}
<a href="#{{ type.name | slugify }}">{{ type.name }}</a>
{% endfor %}
{% for type in site.data.standard_replies_registry %}
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
          {% if site.data.irc_versions.proposed contains specname %}
            <a class="proposed" title="{{ site.data.irc_versions.proposed.specs[specname].name }}" href="{{ site.data.irc_versions.proposed.specs[specname].full-url }}">{{ site.data.irc_versions.proposed.specs[specname].name }}</a><sup> [PR]</sup>{% if forloop.last %}{% else %},{% endif %}
          {% elsif site.data.irc_versions.stable.specs[specname].deprecated %}
            <a class="deprecated" title="{{ site.data.irc_versions.stable.specs[specname].name }}" href="{{ site.baseurl }}{{ site.data.irc_versions.stable.specs[specname].link }}">{{ site.data.irc_versions.stable.specs[specname].name }}</a><sup> [deprecated]</sup>{% if forloop.last %}{% else %},{% endif %}
          {% elsif site.data.irc_versions.stable.specs[specname].draft %}
            <a class="draft" title="{{ site.data.irc_versions.stable.specs[specname].name }}" href="{{ site.baseurl }}{{ site.data.irc_versions.stable.specs[specname].link }}">{{ site.data.irc_versions.stable.specs[specname].name | replace: "draft/" }}</a><sup> [draft]</sup>{% if forloop.last %}{% else %},{% endif %}
          {% else %}
            <a title="{{ site.data.irc_versions.stable.specs[specname].name }}" href="{{ site.baseurl }}{{ site.data.irc_versions.stable.specs[specname].link }}">{{ site.data.irc_versions.stable.specs[specname].name }}</a>{% if forloop.last %}{% else %},{% endif %}
          {% endif %}
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

{% for type in site.data.metadata_registry %}
<h2 id="{{ type.name | slugify }}">{{ type.name }}</h2>
<table class="fullwidth">
  <thead>
    <tr>
      <th style="text-align: center">Key</th>
      <th>Format</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    {% for val in type.values %}
    <tr>
      <td style="min-width: 5rem; white-space: nowrap">
        <code>{{ val.key }}</code>
      </td>
      <td style="min-width: 10rem">
        {% if val.format-mono %}<code>{{ val.format }}</code>{% else %}{{ val.format | markdownify | replace:"<p>","" | replace:"</p>","" }}{% endif %}
        <br>
        {% if val.examples %}
        <code class="examples">{{ val.examples | newline_to_br }}</code>
        {% endif %}
      </td>
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

{% for type in site.data.standard_replies_registry %}
<h2 id="{{ type.name | slugify }}">{{ type.name }} <a href="{{ site.baseurl }}/specs/extensions/standard-replies.html">[spec]</a></h2>
<table class="fullwidth">
  <thead>
    <tr>
      <th style="text-align: center">Command</th>
      <th>Code</th>
      <th>Specs</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    {% assign last_cmd = nil %}
    {% for val in type.values %}
    <tr {% if last_cmd == val.command %}{% else %}{% assign last_cmd = val.command %}class="newblock"{% endif %}>
      <td style="min-width: 5rem; text-align: center" {% if val.command == "*" %}title="Returned generally, not from a specific command"{% elsif val.command %}title="Returned from the {{ val.command }} command"{% else %}title="May be returned generally or from a specific command"{% endif %}>
        <code>{{ val.command }}</code>
      </td>
      <td style="min-width: 10rem">
        <code>{{ val.code }}</code>
      </td>
      <td>
        {% for specname in val.specs %}
          {% if site.data.irc_versions.proposed contains specname %}
            <a class="proposed" title="{{ site.data.irc_versions.proposed.specs[specname].name }}" href="{{ site.data.irc_versions.proposed.specs[specname].full-url }}">{{ site.data.irc_versions.proposed.specs[specname].name }}</a><sup> [PR]</sup>{% if forloop.last %}{% else %},{% endif %}
          {% elsif site.data.irc_versions.stable.specs[specname].deprecated %}
            <a class="deprecated" title="{{ site.data.irc_versions.stable.specs[specname].name }}" href="{{ site.baseurl }}{{ site.data.irc_versions.stable.specs[specname].link }}">{{ site.data.irc_versions.stable.specs[specname].name }}</a><sup> [deprecated]</sup>{% if forloop.last %}{% else %},{% endif %}
          {% elsif site.data.irc_versions.stable.specs[specname].draft %}
            <a class="draft" title="{{ site.data.irc_versions.stable.specs[specname].name }}" href="{{ site.baseurl }}{{ site.data.irc_versions.stable.specs[specname].link }}">{{ site.data.irc_versions.stable.specs[specname].name | replace: "draft/" }}</a><sup> [draft]</sup>{% if forloop.last %}{% else %},{% endif %}
          {% else %}
            <a title="{{ site.data.irc_versions.stable.specs[specname].name }}" href="{{ site.baseurl }}{{ site.data.irc_versions.stable.specs[specname].link }}">{{ site.data.irc_versions.stable.specs[specname].name }}</a>{% if forloop.last %}{% else %},{% endif %}
          {% endif %}
        {% endfor %}
      </td>
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
