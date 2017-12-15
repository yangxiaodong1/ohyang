import tornado.web
from Tools.ohho_operation import OHHOOperation
from ohho.common.view.common.parameters import Post, Get
from ohho.common.logic.common.result import Result
from ohho.common.db.test.db_test_device import DBTestDevice
from Tools.decorator import authenticate


class TestUpdateDeviceInformationHandler(tornado.web.RequestHandler):
    def post(self):
        the_post = Post()
        name = the_post.get_name(self)
        user_id = the_post.get_user_id(self)
        rssi = the_post.get_device_rssi(self)
        identity_id = the_post.get_device_identity_id(self)
        data = dict()
        data["name"] = name
        data["user_id"] = user_id
        data["rssi"] = rssi
        data["identity_id"] = identity_id
        db = DBTestDevice()
        if user_id:
            db.add(data)
        result = Result.result_success()
        self.write(OHHOOperation.dict2json(result))
        # self.write("This is a %s method, %s is not supported" % ("get", "post"))

    def get(self):
        self.write({"name": "get"})
        # the_get = Get()
        # device_identities = the_get.get_device_identities(self)
        # identity_list = device_identities.split(",")
        # result = LogicTestGetUserByDevice.get(identity_list)
        # self.write(OHHOOperation.dict2json(result))
