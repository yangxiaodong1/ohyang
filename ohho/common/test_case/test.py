import tornado.ioloop
from tornado.testing import AsyncTestCase
import tornado


class TestFunc1(AsyncTestCase):
    def get_new_ioloop(self):
        return tornado.ioloop.IOLoop.instance()

    @tornado.testing.gen_test
    def run(self):
        print("OK")
