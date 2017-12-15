import tornado.web
from ohho.common.test.redis.constant import TEST_REDIS_GET_HASH_URL
from ohho.common.test.redis.constant import TEST_REDIS_SET_HASH_URL
from ohho.common.test.constant import HOME_APP_INTERFACES_HTML

class TestHomeAppInterfacesHandler(tornado.web.RequestHandler):
    def post(self):
        pass

    def get(self):
        self.render(HOME_APP_INTERFACES_HTML)
