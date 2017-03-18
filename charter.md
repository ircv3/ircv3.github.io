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


## Technical board

The direction of these specifications is led by the technical board. The board consists of a broad range of IRC software and specification authors that reflect the community at large. The board will seek to make all decisions by consensus.

Nominations for new members of the board will be considered once the following pre-requisites are met:

- Demonstrated support of the IRCv3 specifications
- Approval from the existing board
- Adherence to the [code of conduct]({{site.baseurl}}/conduct.html)

In general, candidates who meet any of the following criteria will be given more consideration

- Developers of widely used IRC software
- Administrators of widely used IRC networks
- People who have otherwise contributed materially to the specifications

We're seeking representation from as many members of the IRC community as possible. If you or your project would be a good candidate for representation, please contact the board. The current members of the board are:

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

The chair has ultimate responsibility for moving discussions forward and will make decisions in cases where consensus isn't possible, including returning proposals to the drawing board where necessary.

## Project resources & Contribution

The main project resources are:

- The [ircv3/ircv3-specifications](https://github.com/ircv3/ircv3-specifications) Github repository and issue tracker.  This is the official repository containing the latest version of the specifications.  Changes may be submitted by pull request and suggestions may be made by opening an issue.
- The [#ircv3](ircs://irc.freenode.net:6697/#ircv3) channel at [irc.freenode.net](ircs://irc.freenode.net:6697/#ircv3).  This is the main discussion space for the working group.

Contributions are welcome from anyone in the IRC community; including users, developers, operators, administrators. Feel free to start a discussion on IRC or on the issue tracker if you'd like to contribute.
 
Failure to follow our [code of conduct]({{site.baseurl}}/conduct.html) when participating may result in immediate removal from the project resources.
