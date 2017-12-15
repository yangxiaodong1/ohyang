from ohho.common.view.common.parameters import Post, Get
from ohho.common.test.redis.constant import *
from DB.redis.operation import RedisDB
from ohho.common.logic.common.constant import CODE
import tornado.web


class TestGetRedisHashHandler(tornado.web.RequestHandler):
    def post(self):
        the_post = Post()
        username = the_post.get_username(self)
        if username:
            result = RedisDB.hash_get(username, CODE)
        else:
            result = ""
        return self.render(TEST_REDIS_GET_HASH_HTML,
                           redis_url=TEST_REDIS_GET_HASH_URL,
                           home_url=TEST_HOME_URL,
                           username=username,
                           result=result
                           )

    def get(self):
        self.render(TEST_REDIS_GET_HASH_HTML,
                    redis_url=TEST_REDIS_GET_HASH_URL,
                    home_url=TEST_HOME_URL,
                    username="",
                    result="")
