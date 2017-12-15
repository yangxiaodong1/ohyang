from ohho.common.view.common.parameters import Get, Post
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.logic.common.cellphone import Cellphone
from tornado.web import authenticated
from ohho.common.view.backstage.constant import *
from Tools.decorator import backstage_authenticate
from math import ceil
from ohho.common.view.common.pagination import Pagination
from Tools.decorator import permission


class BackstageCellphoneAddHandler(BaseHandler):
    @backstage_authenticate
    def post(self):
        the_post = Post()
        cellphone_dict = the_post.get_cellphone(self)
        cellphone = Cellphone()
        cellphone.add_cellphone(cellphone_dict)
        return self.redirect(MANAGEMENT_CELLPHONE_LIST_URL)


    @permission
    @backstage_authenticate
    def get(self):
        return self.render(MANAGEMENT_CELLPHONE_ADD_HTML)
        # return self.render("backstage/management/cellphone_add.html")
