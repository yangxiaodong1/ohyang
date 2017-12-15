import tornado.web
from Tools.ohho_operation import OHHOOperation
from Tools.ohho_log import OHHOLog
from Test.common.logic.logic_phone_position import LogicPhonePosition


class PhonePositionHandler(tornado.web.RequestHandler):
    def post(self):
        # OHHOLog.print_log("start")
        # OHHOLog.print_log(self.request.body)
        # name = self.get_argument("name")
        # OHHOLog.print_log(name)
        name = self.get_body_argument("name")
        OHHOLog.print_log(name)
        environment = self.get_body_argument("environment")
        timestamp = self.get_body_argument("timestamp")
        longitude = self.get_body_argument("longitude")
        latitude = self.get_body_argument("latitude")
        input_distance = self.get_body_argument("input_distance", 0)
        accuracy = self.get_body_argument("accuracy", 0)
        kwargs = dict()
        if name and environment and timestamp and longitude and latitude:
            kwargs["name"] = name
            kwargs["environment"] = environment
            kwargs["timestamp"] = int(timestamp)
            kwargs["longitude"] = float(longitude)
            kwargs["latitude"] = float(latitude)
            kwargs["input_distance"] = float(input_distance)
            kwargs["accuracy"] = float(accuracy)
        OHHOLog.print_log(kwargs)
        result = LogicPhonePosition.add(kwargs)
        OHHOLog.print_log(result)
        self.set_status(status_code=201)
        # OHHOLog.print_log("end")
        self.write(OHHOOperation.dict2json(result))

    def get(self):
        name1 = self.get_argument("name1")
        name2 = self.get_argument("name2")
        result = LogicPhonePosition.get_phones_inforamtion(name1, name2)
        self.write(OHHOOperation.dict2json(result))
