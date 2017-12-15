import logging

from sleekxmpp import ClientXMPP
from sleekxmpp.exceptions import IqError, IqTimeout


class EchoBot(ClientXMPP):
    def __init__(self, jid, password, friend_jid):
        ClientXMPP.__init__(self, jid, password)
        self.friend_id = friend_jid
        self.add_event_handler("session_start", self.session_start)
        self.add_event_handler("message", self.message)

        # If you wanted more functionality, here's how to register plugins:
        # self.register_plugin('xep_0030') # Service Discovery
        # self.register_plugin('xep_0199') # XMPP Ping

        # Here's how to access plugins once you've registered them:
        # self['xep_0030'].add_feature('echo_demo')

        # If you are working with an OpenFire server, you will
        # need to use a different SSL version:
        # import ssl
        # self.ssl_version = ssl.PROTOCOL_SSLv3

    def session_start(self, event):
        self.send_presence()
        self.get_roster()
        self._start_thread("chat_send", self.chat_send)

        # Most get_*/set_* methods from plugins use Iq stanzas, which
        # can generate IqError and IqTimeout exceptions
        #
        # try:
        #     self.get_roster()
        # except IqError as err:
        #     logging.error('There was an error getting the roster')
        #     logging.error(err.iq['error']['condition'])
        #     self.disconnect()
        # except IqTimeout:
        #     logging.error('Server is taking too long to respond')
        #     self.disconnect()

    def message(self, msg):
        if msg['type'] in ('chat', 'normal'):
            print("from %(from)s: %(body)s\n" % (msg))
            # self.send_message(self.friend_id, line)
            # msg.reply("Thanks for sending\n%(body)s" % msg).send()

    def chat_send(self):
        while True:
            line = input("please input:\n")
            self.send_message(self.friend_id, line)


if __name__ == '__main__':
    # Ideally use optparse or argparse to get JID,
    # password, and log level.

    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)-8s %(message)s')

    user = input("your user:\n")
    password = input("your password:\n")
    friend = input("your friend:\n")

    xmpp = EchoBot(user, password, friend)
    if xmpp.connect():
        print("connecting")
        xmpp.process(block=True)
        print("Done")
    else:
        print("Unable to connect")
