from ohho.common.logic.ohho.user.logic_update_user_and_cellphone_relation import LogicUpdateUserAndCellphoneRelation
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


class UpdateUserAndCellphoneRelationHandler(ViewOHHOBase):
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        cellphone_number = the_post.get_cellphone_number(self)
        user_id = the_post.get_user_id(self)
        instance = LogicUpdateUserAndCellphoneRelation()
        result = instance.update_user_and_cellphone_relation(cellphone_number, user_id)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
