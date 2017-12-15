import tornado.web
from ohho.common.test.constant import INTERFACES_HTML


class TestInterfacesHandler(tornado.web.RequestHandler):
    def post(self):
        pass

    def get(self):
        self.render(INTERFACES_HTML)
