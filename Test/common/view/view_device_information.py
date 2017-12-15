import tornado.web
from Tools.ohho_operation import OHHOOperation
from Tools.ohho_log import OHHOLog
from Test.common.logic.logic_device_information import LogicDeviceInformation


class DeviceInformationHandler(tornado.web.RequestHandler):
    def post(self):
        name = self.get_body_argument("name", None)
        phone_name = self.get_body_argument("phone_name", None)
        # OHHOLog.print_log(phone_name)
        # OHHOLog.print_log(type(phone_name))
        environment = self.get_body_argument("environment", None)
        # OHHOLog.print_log(environment)
        timestamp = self.get_body_argument("timestamp", None)
        rssi = self.get_body_argument("rssi", None)
        tx_power = self.get_body_argument("tx_power", None)
        compute_distance = self.get_body_argument("compute_distance", None)
        input_distance = self.get_body_argument("input_distance", None)
        kwargs = dict()
        if name is not None:
            kwargs["name"] = name

        if environment is not None:
            kwargs["environment"] = environment

        if timestamp is not None:
            kwargs["timestamp"] = timestamp

        if phone_name is not None:
            kwargs["phone_name"] = phone_name

        if rssi is not None:
            kwargs["rssi"] = rssi

        if tx_power is not None:
            kwargs["tx_power"] = tx_power

        if compute_distance is not None:
            kwargs["compute_distance"] = compute_distance

        if input_distance is not None:
            kwargs["input_distance"] = input_distance

        result = LogicDeviceInformation.add(kwargs)
        self.set_status(status_code=201)
        self.write(OHHOOperation.dict2json(result))

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
