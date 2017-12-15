import tornado.web
from Tools.ohho_operation import OHHOOperation
from ohho.common.logic.common.result import Result
from ohho.common.db.test.db_test_device import DBTestDevice


class DeleteTestHandler(tornado.web.RequestHandler):
    def post(self):
        pass
        # name = self.get_body_argument("user_name", None)
        # result = dict()
        # result["user_name"] = name
        #
        # self.write(OHHOOperation.dict2json(result))
        # self.write("This is a %s method, %s is not supported" % ("get", "post"))

    def get(self):
        apply = DBTestDevice()
        apply.delete_all()
        result = Result.result_success()
        return self.write(OHHOOperation.dict2json(result))
        # self.write({"name": "get"})
        # the_get = Get()
        # device_identities = the_get.get_device_identities(self)
        # identity_list = device_identities.split(",")
        # result = LogicTestGetUserByDevice.get(identity_list)
        # self.write(OHHOOperation.dict2json(result))
