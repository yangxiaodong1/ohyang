from Test.common.db.db_device_information import DBDeviceInformation


class LogicDeviceInformation(object):
    @staticmethod
    def add(kwargs):
        result = dict()
        result["success"] = False
        if kwargs:
            obj = DBDeviceInformation.add(kwargs)
        else:
            obj = DBDeviceInformation.get_none()
        if obj:
            result["success"] = True
        return result
