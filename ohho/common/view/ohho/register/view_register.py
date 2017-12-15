from ohho.common.view.view_ohho_base import ViewOHHOBase
from ohho.common.logic.ohho.register.logic_register import LogicRegister
from ohho.common.view.common.parameters import Post
from Tools.ohho_log import OHHOLog


class RegisterHandler(ViewOHHOBase):
    def post(self):
        OHHOLog.print_log("start register")
        the_post = Post()
        OHHOLog.print_log("set the post")
        self.set_format(the_post.get_format(self))
        username = the_post.get_username(self)
        OHHOLog.print_log("get username")
        password = the_post.get_password(self)
        code = the_post.get_code(self)
        cellphone = the_post.get_cellphone_number(self)
        country_code = the_post.get_cellphone_country_code(self)
        if not country_code:
            country_code = "+86"
        identity_id = the_post.get_device_identity_id(self)
        mac_address = the_post.get_device_mac_address(self)
        imei = the_post.get_imei(self)
        base_url = the_post.get_base_url(self)
        register_dict = dict()

        OHHOLog.print_log("get all parameters")
        register_dict["username"] = username
        register_dict["password"] = password
        register_dict["code"] = code
        register_dict["identity_id"] = identity_id
        register_dict["mac_address"] = mac_address
        register_dict["imei"] = imei
        register_dict["cellphone"] = cellphone
        register_dict["country_code"] = country_code

        cellphone_dict = the_post.get_cellphone(self)
        instance = LogicRegister(register_dict, cellphone_dict)
        result = instance.register(base_url)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
