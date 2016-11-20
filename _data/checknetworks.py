#!/usr/bin/env python3
# Checks our network support file and notifies for added/removed specs.

# Written in 2016 by Daniel Oaks <daniel@danieloaks.net>
#
# To the extent possible under law, the author(s) have dedicated all copyright
# and related and neighboring rights to this software to the public domain
# worldwide. This software is distributed without any warranty.
#
# You should have received a copy of the CC0 Public Domain Dedication along
# with this software. If not, see
# <http://creativecommons.org/publicdomain/zero/1.0/>.

# to run this script:
#     pip3 install --update girc pyyaml docopt
#     cd _data
#     python3 checknetworks.py

"""checknetworks.py - tests IRCv3 network support file.
Usage:
    checknetworks.py run [<supportfile>]
    checknetworks.py --version
    checknetworks.py (-h | --help)
Options:
    <supportfile>  YAML network list [default: su_networks.yml]."""
from docopt import docopt
import girc
import yaml


def check_net(versions, info):
    print("Connecting to:", info['name'])
    hostname = info['net-address']['display']

    reactor = girc.Reactor()

    supported = {}

    # register events
    @reactor.handler('in', 'endofmotd')
    @reactor.handler('in', 'nomotd')
    def handle_endofmotd(event):
        # get caps
        supported['caps'] = []
        for name in event['server'].capabilities.available:
            supported['caps'].append(name)

        # get features
        supported['features'] = []
        for name in event['server'].features.available:
            supported['features'].append(name)

        event['server'].quit()

    # without TLS then with TLS
    server = reactor.create_server(info['name'] + ' noTLS')
    server.set_user_info('ircv3-tst', user='ircv3', real='IRCv3 tester')
    server.connect(hostname, 6667, ssl=False)

    reactor.run_forever()

    # generate cap lists
    all_caps = []
    for ver in versions:
        for spec in versions[ver]['specs']:
            all_caps.extend(versions[ver]['specs'][spec].get('caps', []))

    claimed_supported = []
    for ver in info['support']:
        for spec in info['support'][ver]:
            claimed_supported.extend(versions[ver]['specs'][spec].get('caps', []))

    claimed_unsupported = []
    for cap in all_caps:
        if cap not in claimed_supported:
            claimed_unsupported.append(cap)

    # and check them
    for cap in claimed_supported:
        if cap not in supported['caps']:
            print(' *!* - ', info['name'], 'claims to support', cap, 'but does not')
    for cap in claimed_unsupported:
        if cap in supported['caps']:
            print(' *!* + ', info['name'], 'now also supports', cap)

if __name__ == '__main__':
    arguments = docopt(__doc__, version=girc.__version__)

    if arguments['run']:
        print("NOTE: The output of this script can be incorrect due to nets only exposing certain caps when on/not on TLS, and other implementation and network-specific factors.")

        # open irc-versions file
        versions_string = open('irc_versions.yml', 'r').read()
        versions = yaml.safe_load(versions_string)

        # open support file
        supportfn = 'su_networks.yml'
        if arguments['<supportfile>'] is not None:
            supportfn = arguments['<supportfile>']
        support_string = open(supportfn, 'r').read()

        support = yaml.safe_load(support_string)

        # connect to each test network
        for nettype in support:
            for net in nettype['software']:
                check_net(versions, net)
