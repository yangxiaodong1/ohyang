from ohho.common.db.ohho.device.db_ohho_device import DBOHHODevice
from ohho.common.db.ohho.map.db_ohho_map_information import DBOHHOMapInformation
from ohho.common.db.ohho.relation.db_ohho_user_and_device_relation import DBOHHOUserAndDeviceRelation
from ohho.common.db.ohho.device.db_ohho_device_sensor import DBOHHODeviceSensor

from Tools.ohho_datetime import OHHODatetime

from ohho.common.logic.common.constant import FIND_DEVICE_TIMESTAMP_DELTA
from ohho.common.logic.common.result import Result

MEET_DISTANCE = 5
TIMESTAMP_DELTA = 5 * 60


class LogicFindDevicePosition(object):
    def __init__(self):
        self.sensor = DBOHHODeviceSensor()
        self.device = DBOHHODevice()
        self.relation = DBOHHOUserAndDeviceRelation()
        self.map = DBOHHOMapInformation()

    def find_device_position(self, identity_id):
        result = dict()
        data = list()
        circle = dict()
        circle["longitude"] = -1
        circle["latitude"] = -1
        circle["radius"] = -1
        self.device.set_identity(identity_id)
        device = self.device.get_by_identity()
        if device:
            relation = self.relation.get_by_device(device.id)
            if relation:
                query = self.map.get_by_user(relation.user_id)
                query = self.map.order_by_id_desc(query)
                first = self.map.first(query)
                if first:
                    current_timestamp = OHHODatetime.get_current_timestamp()
                    if current_timestamp < first.timestamp + FIND_DEVICE_TIMESTAMP_DELTA:
                        circle["longitude"] = first.longitude
                        circle["latitude"] = first.latitude
                        sensor_query = self.sensor.get_query()
                        sensor_query = self.sensor.get_by_device(sensor_query, device.id)
                        sensor_query = self.sensor.get_by_user(sensor_query, relation.user_id)
                        sensor_query = self.sensor.order_by_id_desc(sensor_query)
                        first = self.sensor.first(sensor_query)
                        if first:
                            if current_timestamp < first.timestamp + FIND_DEVICE_TIMESTAMP_DELTA:
                                result = Result.result_success()
                                circle["radius"] = first.distance
                            else:
                                result = Result.result_failed("device sensor is outdated!")
                        else:
                            result = Result.result_failed("no device sensor!")
                    else:
                        result = Result.result_failed("map position is outdated!")
                else:
                    result = Result.result_failed("no map position!")
            else:
                result = Result.result_failed("no user binds the device!")
        else:
            result = Result.result_failed("no such device!")
        data.append(circle)
        result["data"] = data

        return result
