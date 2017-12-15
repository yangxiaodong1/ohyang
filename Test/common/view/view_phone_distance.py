import tornado.web
from Tools.ohho_operation import OHHOOperation
from Tools.decorator import statistic
from Tools.ohho_log import OHHOLog
from Test.common.logic.logic_phone_distance import LogicPhoneDistance


class PhoneDistanceHandler(tornado.web.RequestHandler):
    @statistic
    def get(self):
        print(self.__class__.__name__)
        self.set_header("Content-Type", "application/json; charset=utf-8")
        name1 = self.get_argument("name1")
        name2 = self.get_argument("name2")
        result = LogicPhoneDistance.add_by_names(name1, name2)
        OHHOLog.print_log(result)
        self.write(OHHOOperation.dict2json(result))

    def post(self):
        name1 = self.get_body_argument("name1")
        name2 = self.get_body_argument("name2")
        result = LogicPhoneDistance.add_by_names(name1, name2)
        self.set_status(status_code=201)
        self.write(OHHOOperation.dict2json(result))
