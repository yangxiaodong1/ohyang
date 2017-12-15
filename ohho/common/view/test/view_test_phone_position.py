from ohho.common.view.view_ohho_base import ViewOHHOBase
from Tools.ohho_operation import OHHOOperation
from Tools.ohho_log import OHHOLog
from ohho.common.view.common.parameters import Post, Get
from ohho.common.logic.common.result import Result
from ohho.common.logic.test.logic_test_add_phone_position import LogicTestAddPhonePosition


class TestPhonePositionHandler(ViewOHHOBase):
    def post(self):
        the_request = Post()
        self.set_format(the_request.get_format(self))
        instance = LogicTestAddPhonePosition()
        position_dict = the_request.get_map_information(self)
        position_dict["name"] = the_request.get_name(self)
        position_dict["environment"] = self.get_body_argument("environment")
        position_dict["timestamp"] = self.get_body_argument("timestamp")
        position_dict["input_distance"] = self.get_body_argument("input_distance")
        position_dict["aoi"] = self.get_body_argument("aoi")
        position_dict["position_time"] = self.get_body_argument("position_time")
        result = Result.result_failed()
        success = instance.add(position_dict)
        if success:
            result = Result.result_success()
        return self.response(result)

        # OHHOLog.print_log("start")
        # OHHOLog.print_log(self.request.body)
        # name = self.get_argument("name")
        # OHHOLog.print_log(name)
        # name = self.get_body_argument("name")
        # OHHOLog.print_log(name)
        # environment = self.get_body_argument("environment")
        # timestamp = self.get_body_argument("timestamp")
        # longitude = self.get_body_argument("longitude")
        # latitude = self.get_body_argument("latitude")
        # input_distance = self.get_body_argument("input_distance", 0)
        # accuracy = self.get_body_argument("accuracy", 0)
        # kwargs = dict()
        # if name and environment and timestamp and longitude and latitude:
        #     kwargs["name"] = name
        #     kwargs["environment"] = environment
        #     kwargs["timestamp"] = int(timestamp)
        #     kwargs["longitude"] = float(longitude)
        #     kwargs["latitude"] = float(latitude)
        #     kwargs["input_distance"] = float(input_distance)
        #     kwargs["accuracy"] = float(accuracy)
        # OHHOLog.print_log(kwargs)

        # result = LogicPhonePosition.add(kwargs)
        # OHHOLog.print_log(result)
        # self.set_status(status_code=201)
        # OHHOLog.print_log("end")
        # self.write(OHHOOperation.dict2json(result))

    def get(self):
        the_request = Get()
        self.set_format(the_request.get_format(self))
        instance = LogicTestAddPhonePosition()
        position_dict = the_request.get_map_information(self)
        position_dict["name"] = the_request.get_name(self)
        position_dict["environment"] = self.get_argument("environment")
        position_dict["timestamp"] = self.get_argument("timestamp")
        position_dict["input_distance"] = self.get_argument("input_distance")
        position_dict["aoi"] = self.get_argument("aoi")
        position_dict["position_time"] = self.get_argument("position_time")
        result = Result.result_failed()
        success = instance.add(position_dict)
        if success:
            result = Result.result_success()
        return self.response(result)
        # name1 = self.get_argument("name1")
        # name2 = self.get_argument("name2")
        # result = LogicPhonePosition.get_phones_inforamtion(name1, name2)
        # self.write(OHHOOperation.dict2json(result))
