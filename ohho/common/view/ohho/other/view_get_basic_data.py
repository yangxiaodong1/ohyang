from ohho.common.view.view_ohho_base import ViewOHHOBase
from Tools.decorator import authenticate
from ohho.common.logic.ohho.base.logic_get_basic_data import LogicGetBasicData
from ohho.common.view.common.parameters import Post, Get
from Tools.ohho_log import OHHOLog


class GetBasicDataHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        instance = LogicGetBasicData()
        result = instance.get()
        return self.response(result)

    def get(self):
        the_post = Get()
        self.set_format(the_post.get_format(self))
        instance = LogicGetBasicData()
        result = instance.get()
        OHHOLog.print_log(result)
        return self.response(result)
