from ohho.common.view.view_ohho_base import ViewOHHOBase
from Tools.decorator import authenticate
from ohho.common.logic.ohho.device.logic_add_device_setting import LogicAddDeviceSetting
from ohho.common.view.common.parameters import Post


class AddDeviceSettingHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        identity_id = the_post.get_device_identity_id(self)
        password = the_post.get_password(self)
        name = the_post.get_name(self)
        power = the_post.get_power(self)
        periods = the_post.get_periods(self)

        setting = LogicAddDeviceSetting()
        result = setting.add_device_setting(identity_id, password, name, power, periods)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
