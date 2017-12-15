from ohho.common.view.common.parameters import Post, Get
from ohho.common.test.redis.constant import *
# from DB.redis.operation import RedisDB
# from ohho.common.logic.common.constant import CODE
from ohho.common.logic.common.code import Code
import tornado.web


class TestSetRedisHashHandler(tornado.web.RequestHandler):
    def post(self):
        the_post = Post()
        username = the_post.get_username(self)
        the_code = Code.create_code()
        Code.save_code(username, the_code)
        return self.render(TEST_REDIS_SET_HASH_HTML,
                           redis_url=TEST_REDIS_SET_HASH_URL,
                           home_url=TEST_HOME_URL,
                           username=username,
                           result=the_code
                           )

    def get(self):
        self.render(TEST_REDIS_SET_HASH_HTML,
                    redis_url=TEST_REDIS_SET_HASH_URL,
                    home_url=TEST_HOME_URL,
                    username="",
                    result="")
