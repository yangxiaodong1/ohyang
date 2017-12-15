import tornado.web
from Tools.ohho_operation import OHHOOperation
from ohho.common.view.common.parameters import Post, Get
from ohho.common.logic.test.logic_test_get_user_by_device import LogicTestGetUserByDevice
from Tools.decorator import authenticate


class GetUserByDeviceHandler(tornado.web.RequestHandler):
    @authenticate
    def post(self):
        the_get = Post()
        device_identities = the_get.get_device_identities(self)
        identity_list = device_identities.split(",")
        result = LogicTestGetUserByDevice.get(identity_list)
        return self.write(OHHOOperation.dict2json(result))


    def get(self):
        return self.write("This is a %s method, %s is not supported" % ("get", "post"))
        # the_get = Get()
        # device_identities = the_get.get_device_identities(self)
        # identity_list = device_identities.split(",")
        # result = LogicTestGetUserByDevice.get(identity_list)
        # self.write(OHHOOperation.dict2json(result))
