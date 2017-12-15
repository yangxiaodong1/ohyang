from Tools.decorator import authenticate, execute_time
from Tools.ohho_log import OHHOLog
from ohho.common.logic.ohho.map.logic_upload_map_position import LogicUploadMapPosition
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


class UploadMapPositionHandler(ViewOHHOBase):
    # @execute_time
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        map_information = the_post.get_all_map_information(self)
        user_id = the_post.get_user_id(self)
        apply_id = the_post.get_apply_id(self)
        timestamp = the_post.get_timestamp(self)
        base_url = the_post.get_base_url(self)
        instance = LogicUploadMapPosition()
        result = instance.upload_map_position(user_id, map_information, apply_id, base_url, timestamp)
        # OHHOLog.print_log(result)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
