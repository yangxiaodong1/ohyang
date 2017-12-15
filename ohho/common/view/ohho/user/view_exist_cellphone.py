from Tools.decorator import authenticate
from ohho.common.logic.ohho.user.logic_exist_cellphone import LogicExistCellphone
from ohho.common.view.common.parameters import Post, Get
from ohho.common.view.view_ohho_base import ViewOHHOBase


class ExistCellphoneHandler(ViewOHHOBase):
    def post(self):
        params = Post()
        self.set_format(params.get_format(self))
        cellphone = params.get_cellphone_number(self)
        country_code = params.get_cellphone_country_code(self)

        instance = LogicExistCellphone()
        result = instance.exist(country_code, cellphone)
        return self.response(result)

    def get(self):
        params = Get()
        self.set_format(params.get_format(self))
        cellphone = params.get_cellphone_number(self)
        country_code = params.get_cellphone_country_code(self)

        instance = LogicExistCellphone()
        result = instance.exist(country_code, cellphone)
        return self.response(result)

