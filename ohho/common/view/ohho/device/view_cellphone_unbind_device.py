from ohho.common.logic.ohho.device.logic_cellphone_unbind_device import LogicCellphoneUnbindDevice
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


class CellphoneUnbindDeviceHandler(ViewOHHOBase):
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        country_code = the_post.get_cellphone_country_code(self)
        cellphone_number = the_post.get_cellphone_number(self)
        code = the_post.get_code(self)
        identity_id = the_post.get_device_identity_id(self)
        mac_address = the_post.get_device_mac_address(self)
        unbind_device = LogicCellphoneUnbindDevice()
        result = unbind_device.unbind_device(cellphone_number, code, identity_id, mac_address, country_code)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
