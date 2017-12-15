from ohho.common.logic.ohho.user.logic_rebind_cellphone import LogicRebindCellphone
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


class RebindCellphoneHandler(ViewOHHOBase):
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        country_code = the_post.get_cellphone_country_code(self)
        cellphone_key = the_post.get_cellphone_key(self)
        cellphone_number = the_post.get_cellphone_number(self)
        cellphone_dict = the_post.get_cellphone(self)
        code = the_post.get_code(self)
        base_url = the_post.get_base_url(self)

        instance = LogicRebindCellphone()
        result = instance.rebind_cellphone(cellphone_key, cellphone_number, code, base_url, cellphone_dict,
                                           country_code)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
