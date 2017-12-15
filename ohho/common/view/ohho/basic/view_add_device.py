from ohho.common.view.view_ohho_base import ViewOHHOBase
from ohho.common.logic.ohho.device.logic_add_device import LogicAddDevice
from ohho.common.view.common.parameters import Post


class AddDeviceHandler(ViewOHHOBase):
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        application_id = the_post.get_device_application_id(self)
        identity_id = the_post.get_device_identity_id(self)
        mac_address = the_post.get_device_mac_address(self)
        tx_power = the_post.get_device_tx_power(self)
        device = LogicAddDevice()
        result = device.add_device(application_id, identity_id, mac_address, tx_power)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
