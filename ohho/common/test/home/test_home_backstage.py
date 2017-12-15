import tornado.web
from ohho.common.test.redis.constant import TEST_REDIS_GET_HASH_URL
from ohho.common.test.redis.constant import TEST_REDIS_SET_HASH_URL
from ohho.common.test.constant import HOME_BACKSTAGE_HTML


class TestHomeBackstageHandler(tornado.web.RequestHandler):
    def post(self):
        pass

    @tornado.web.asynchronous
    def get(self):
        self.render(HOME_BACKSTAGE_HTML,
                    redis_url=TEST_REDIS_GET_HASH_URL,
                    set_redis_url=TEST_REDIS_SET_HASH_URL,
                    )
