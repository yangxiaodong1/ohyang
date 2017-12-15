from ohho.common.view.common.parameters import Post, Get
from ohho.common.test.redis.constant import *
from ohho.common.db.test.db_test_timestamp import DBTestTimestamp
# from ohho.common.db.ohho.relation.db_ohho_user_and_device_imei import DBOHHOUserAndDeviceIMEI
# from DB.redis.operation import RedisDB
# from ohho.common.logic.common.constant import CODE
from Tools.ohho_operation import OHHOOperation
import tornado.web


class TestAddTimestampHandler(tornado.web.RequestHandler):
    def post(self):
        the_post = Post()
        name = the_post.get_name(self)
        # timestamp = self.get_body_argument("timestamp", None)
        data = dict()
        # if timestamp:
        #     data["timestamp"] = timestamp
        data["name"] = name
        print(data)
        db = DBTestTimestamp()
        db.add(data)
        result = {"success": True}

        return self.write(OHHOOperation.dict2json(result))

    def get(self):
        # instance = DBOHHOUserAndDeviceIMEI()
        # query = instance.get_query()
        # query = instance.get_by_user_id(query, None)
        # query = instance.get_by_device_id(query, None)
        # data = [imei.imei for imei in query]
        #
        # return self.write(",".join(data))

        self.render(TEST_ADD_TIMESTAMP_HTML,
                    redis_url=TEST_REDIS_SET_HASH_URL,
                    home_url=TEST_HOME_URL,
                    username="",
                    result="")
