import tornado.web
from ohho.common.test.redis.constant import TEST_REDIS_GET_HASH_URL
from ohho.common.test.redis.constant import TEST_REDIS_SET_HASH_URL
from ohho.common.test.constant import HOME_APP_HTML

class TestHomeAppHandler(tornado.web.RequestHandler):
    def post(self):
        pass

    @tornado.web.asynchronous
    def get(self):
        self.render(HOME_APP_HTML,
                    redis_url=TEST_REDIS_GET_HASH_URL,
                    set_redis_url=TEST_REDIS_SET_HASH_URL,
                    )
