---
layout: page
title: Networks
meta-description: IRCv3 Network Support. This page lists the IRC networks compatible with and supporting IRCv3 features.
data-source-filename: su_networks.yml
---
We make a best effort to keep this list up to date.

Please help us keep this updated by <a href="https://github.com/ircv3/ircv3.github.io/blob/master/_data/{{page.data-source-filename}}">contributing a pull request</a>.

{% for type in site.data.su_networks %}
{% include software_list.html %}
{% endfor %}
