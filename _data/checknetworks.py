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
# <https://creativecommons.org/publicdomain/zero/1.0/>.

# to run this script:
#     pip3 install --upgrade girc pyyaml docopt
#     cd _data
#     python3 checknetworks.py run su_networks.yml

"""checknetworks.py - tests IRCv3 network support file.
Usage:
    checknetworks.py run [<supportfile>]
    checknetworks.py --version
    checknetworks.py (-h | --help)
Options:
    <supportfile>  YAML network list [default: su_networks.yml]."""
from docopt import docopt
import yaml
import os
import ssl
import socket
import traceback
from datetime import datetime
from girc.ircreactor.envelope import RFC1459Message
from girc.ircreactor.events import EventManager

# settings
nick = 'ircv3-tst'
username = 'ircv3'
realname = 'IRCv3 cap/isupport Tester'


class IRCv3Connection:
    """Connects to an IRC server at the given address."""
    def __init__(self, hostname, nick, username, realname, ipv6=False, debug=False, exit_early=False):
        self.debug = debug
        self.exit_early = exit_early
        self._data = b''

        if ipv6:
            family = socket.AF_INET6
        else:
            family = socket.AF_INET

        self.sock = socket.socket(family, socket.SOCK_STREAM)
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        self.sock = context.wrap_socket(self.sock, server_hostname=hostname)
        self.sock.connect((hostname, 6697))

        # identify
        self.send('CAP LS 302')
        self.send('NICK {}'.format(nick))
        self.send('USER {} 0 * :{}'.format(username, realname))
        if exit_early:
            self.send('QUIT')
        self.send('CAP END')

        # events setup
        self._events = EventManager()
        self._events.register('irc message 005', self.on_005)
        self._events.register('irc message cap', self.on_cap)
        self._events.register('irc message ping', self.on_ping)
        self._events.register('irc message 376', self.on_connected)
        self._events.register('irc message 422', self.on_connected)

        # basic data
        self.caps = {}
        self.isupport = {}

    def loop(self):
        """Start connection loop."""
        try:
            while True:
                line = self.recv()
                if line.strip() == '':
                    continue
                m = RFC1459Message.from_message(line)
                if m.verb == 'ERROR':
                    break
        except:
            trace = traceback.format_exc()
            print(trace)

    def recv(self, bytes=4096):
        """Receive any info from the IRC server."""
        # recv existing lines before receiving new ones
        if b'\n' not in self._data:
            self._data += self.sock.recv(bytes)
        if b'\n' in self._data:
            raw_bytes, self._data = self._data.split(b'\n', maxsplit=1)
            line = raw_bytes.decode('utf-8', 'ignore').strip('\r\n')
            if line.strip() == '':
                return ''
            if self.debug:
                print('{} <-  {}'.format(datetime.today().strftime('%H:%M:%S'), line))
            m = RFC1459Message.from_message(line)
            self._events.dispatch('irc message {}'.format(m.verb.lower()), m)
            return line
        return ''

    def send(self, line):
        """Send the given line to the IRC server."""
        self.send_raw('{}\r\n'.format(line))

    def send_raw(self, line):
        """Send the given line to the IRC server."""
        if self.debug:
            print('{} -> {}'.format(datetime.today().strftime('%H:%M:%S'), line.strip('\r\n')))
        self.sock.send(line.encode('utf-8', 'ignore'))

    def on_ping(self, msg):
        self.send('PONG :{}'.format(msg.params[-1]))

    def on_cap(self, msg):
        if msg.params[1].upper() != 'LS':
            return
        for cap in msg.params[-1].split():
            value = ''
            if '=' in cap:
                cap, value = cap.split('=', maxsplit=1)
            self.caps[cap] = value

    def on_005(self, msg):
        for name in msg.params[1:-1]:
            value = ''
            if '=' in name:
                name, value = name.split('=', maxsplit=1)
            self.isupport[name] = value

    def on_connected(self, msg):
        self.send('QUIT')


def check_net(versions, info):
    print("Connecting to:", info['name'])
    hostname = info['net-address']['display']
    exit_early = info['net-address'].get('exit-early', False)

    supported = {}

    irc = IRCv3Connection(hostname, nick, username, realname, debug=False, exit_early=exit_early)
    irc.loop()

    supported['isupport'] = irc.isupport.keys()
    supported['caps'] = irc.caps.keys()

    # generate cap and isupport lists
    all_caps = []
    all_isupport = []
    for ver in versions:
        for spec in versions[ver]['specs']:
            all_caps.extend(versions[ver]['specs'][spec].get('caps', []))
            all_isupport.extend(versions[ver]['specs'][spec].get('isupport', []))

    claimed_supported_caps = []
    claimed_supported_isupport = []
    for suptype in ['support', 'partial']:
        if suptype not in info:
            continue
        for ver in info[suptype]:
            for spec in info[suptype][ver]:
                claimed_supported_caps.extend(versions[ver]['specs'][spec].get('caps', []))
                claimed_supported_isupport.extend(versions[ver]['specs'][spec].get('isupport', []))

    claimed_unsupported_caps = []
    claimed_unsupported_isupport = []
    for cap in all_caps:
        if cap not in claimed_supported_caps:
            claimed_unsupported_caps.append(cap)
    for key in all_isupport:
        if key not in claimed_supported_isupport:
            claimed_unsupported_isupport.append(key)

    # and check them
    for cap in claimed_supported_caps:
        if cap not in supported['caps']:
            print(' *!* - ', info['name'], 'claims to advertise cap', cap, 'but does not')
    for cap in claimed_unsupported_caps:
        if cap in supported['caps']:
            print(' *!* + ', info['name'], 'now also sadvertise cap', cap)
    if exit_early:
        # we didn't get to see isupport tokens, skip checking those
        return

    for token in claimed_supported_isupport:
        if token not in supported['isupport']:
            print(' *!* - ', info['name'], 'claims to advertise isupport token', token, 'but does not')
    for token in claimed_unsupported_isupport:
        if token in supported['isupport']:
            print(' *!* + ', info['name'], 'now also sadvertise isupport token', token)

if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.1')

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
