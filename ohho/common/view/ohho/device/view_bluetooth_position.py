from Tools.decorator import authenticate
from ohho.common.logic.ohho.device.logic_bluetooth_position import LogicBluetoothPosition
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


# no use
class BluetoothPositionHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        apply_id = the_post.get_apply_id(self)
        identity_id = the_post.get_device_identity_id(self)
        rssi = the_post.get_device_rssi(self)
        distance = the_post.get_device_distance(self)
        base_url = the_post.get_base_url(self)

        instance = LogicBluetoothPosition()
        result = instance.bluetooth_position(user_id, identity_id, rssi, distance, apply_id, base_url)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
