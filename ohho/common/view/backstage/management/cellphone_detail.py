from tornado.web import authenticated

from ohho.common.logic.common.cellphone import Cellphone
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.view.backstage.constant import *
from ohho.common.view.common.parameters import Get, Post
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate

class BackstageCellphoneDetailHandler(BaseHandler):
    @backstage_authenticate
    def post(self):
        pass
        the_post = Post()
        cellphone_key = the_post.get_cellphone_key(self)
        detail_url = MANAGEMENT_CELLPHONE_DETAIL_URL + "?cellphone_key=" + str(cellphone_key)
        submit = self.get_body_argument("submit", "")
        cancel = self.get_body_argument("cancel", "")
        delete = self.get_body_argument("delete", "")
        instance = Cellphone(cellphone_key)
        if cancel:
            return self.redirect(MANAGEMENT_CELLPHONE_LIST_URL)
        if delete:
            cellphone = instance.get()
            if cellphone:
                success = instance.delete(cellphone)
                if success:
                    return self.redirect(MANAGEMENT_CELLPHONE_LIST_URL)
                else:
                    return self.redirect(detail_url)

        if submit:
            cellphone = instance.get()
            data = dict()
            data["operation"] = the_post.get_cellphone_operation(self)
            data["operation_version"] = the_post.get_cellphone_operation_version(self)
            data["manufacturer"] = the_post.get_cellphone_manufacturer(self)
            data["platform_type"] = the_post.get_cellphone_platform_type(self)
            success = instance.update(cellphone, data)
            if success:
                return self.redirect(MANAGEMENT_CELLPHONE_LIST_URL)
            else:
                return self.redirect(detail_url)
        return self.redirect(detail_url)

    @permission
    @backstage_authenticate
    def get(self):
        the_get = Get()
        cellphone_key = the_get.get_cellphone_key(self)
        instance = Cellphone(cellphone_key)
        cellphone = instance.get()
        # from Tools.ohho_operation import OHHOOperation
        # import chardet
        # m = cellphone.manufacturer
        # the_byte = OHHOOperation.to_bytes(m)
        # print(the_byte)
        # print(chardet.detect(the_byte))
        # print(m)
        return self.render("backstage/management/cellphone_detail.html", cellphone=cellphone)
