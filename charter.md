---
title: Working group charter
layout: default
meta-description: The IRCv3 working group is chartered to prototype, develop and specify further extensions to the IRC client protocol.
page-header: >
  IRCv3 Working Group Charter
---

The IRCv3 working group is chartered to prototype, develop, test and specify further extensions to
the IRC client protocol. It does not define any other aspect of an IRC network, such as IRC services,
or the server-to-server protocol, although the changes it develops may require cooperation from vendors
in both areas.

These extensions are published on this website through backwards-compatible [specifications]({{site.baseurl}}/irc/).


## IRCv3 Contributors

The direction of these specifications is led by our contributors and the WG Chair. Our contributors consist of a broad range of IRC software and specification authors that reflects the IRC development community at large. We seek to make all decisions by consensus.

To be listed on this page, contributors must:

- Demonstrate support of the IRCv3 specifications
- Have the approval of the current contributors
- Adhere to our [code of conduct]({{site.baseurl}}/conduct.html)

We're seeking representation from as many members of the IRC community as possible. If you or your project would be a good candidate for representation, please contact us!

Here's some of our current contributors:

<table>
    <thead>
        <tr>
            <th>IRC nick</th>
            <th>Github</th>
            <th>Project</th>
            <th></th>
        </tr>
    </thead>
    <tbody>
        {% for member in site.data.tc %}
        <tr>
            <td>{{ member.nick }}</td>
            <td><a href="https://github.com/{{ member.github }}">{{ member.github }}</a></td>
            <td>
               {% for project in member.projects %}
                  {{ project | markdownify | replace: "<p>", "" | replace: "</p>", "" }}
                  {% if forloop.last %}{% else %}/{% endif %}
               {% endfor %}
            </td>
            <td>
               {% if member.chair %}Chair{% endif %}
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>


## Governance

The WG Chair is someone the IRCv3 contributors have designated as the Leader For Now of IRCv3. They're able to move discussions forward and make decisions in cases where consensus between contributors isn't possible. They can also return proposals to the drawing board where necessary.

In extraordinary circumstances, the IRCv3 contributors may decide to depose the WG Chair and replace them with someone else (as we've done [in the past](https://github.com/ircv3/ircv3-specifications/issues/233)). In addition, the Chair may appoint someone else to replace them as Chair.

Ownership of the resources of the IRCv3 WG (including the GitHub org, domains, channel, and moderators email list) are spread across several contributors, to prevent the situation where someone can unilaterally control the WG without support from the contributors.


## Project resources & Contribution

The main project resources are:

- The [ircv3/ircv3-specifications](https://github.com/ircv3/ircv3-specifications) Github repository and issue tracker.  This is the official repository containing the latest version of the specifications.  Changes may be submitted by pull request and suggestions may be made by opening an issue.
- The [#ircv3](ircs://irc.libera.chat:6697/#ircv3) channel at [irc.libera.chat](ircs://irc.libera.chat:6697/#ircv3).  This is the main discussion space for the working group.

Contributions are welcome from anyone in the IRC community; including users, developers, operators, administrators. Feel free to start a discussion on IRC or on the issue tracker if you'd like to contribute.

Failure to follow our [code of conduct]({{site.baseurl}}/conduct.html) when participating may result in immediate removal from the project resources.
