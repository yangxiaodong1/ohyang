from Tools.decorator import authenticate
from ohho.common.logic.ohho.device.logic_find_device_position import LogicFindDevicePosition
from ohho.common.view.common.parameters import Get
from ohho.common.view.view_ohho_base import ViewOHHOBase

# no use
class FindDevicePositionHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        self.write("This is a %s method, %s is not supported" % ("get", "post"))

    @authenticate
    def get(self):
        the_get = Get()
        self.set_format(the_get.get_format(self))
        identity_id = the_get.get_device_identity_id(self)
        instance = LogicFindDevicePosition()
        result = instance.find_device_position(identity_id)
        return self.response(result)
