from ohho.common.db.ohho.im.db_ohho_im_user import DBOHHOIMUser
from ohho.common.db.ohho.user.db_ohho_user_configuration import DBOHHOUserConfiguration
from ohho.common.logic.common.cellphone import Cellphone
from ohho.common.logic.common.code import Code
from ohho.common.logic.common.device import Device
from ohho.common.logic.common.im.netease.create import Create
from ohho.common.logic.common.im.netease.refresh_token import RefreshToken
from ohho.common.logic.common.im.netease.user import User as IMUser
from ohho.common.logic.common.result import Result
from ohho.common.logic.common.user import User
from ohho.common.logic.common.imei import IMEI
from ohho.common.logic.ohho.detail_constant import *
from Tools.ohho_log import OHHOLog
from Tools.ohho_uuid import OHHOUUID


class LogicRegister(object):
    def __init__(self, register_dict, cellphone_dict):
        self.register_dict = register_dict
        self.cellphone_dict = cellphone_dict
        self.im_user = DBOHHOIMUser()
        self.configuration = DBOHHOUserConfiguration()
        self.user = User(register_dict.get("username", None))
        self.device = Device()
        self.cellphone = Cellphone()
        self.imei = IMEI()

    def add_new_user(self, password, cellphone, country_code="+86"):
        username = OHHOUUID.get_uuid1_string()
        self.user.set_username(username)
        self.user.add_user(password, cellphone, country_code)
        user = self.user.get_by_username(username)
        if user:
            result = Result.result_success()
            result["user_id"] = user.id
        else:
            result = Result.result_failed()
            result["user_id"] = 0
        return result

    def update_user(self, instance, user_dict):
        return self.user.update_user(instance, user_dict)

    def add_cellphone(self, cellphone_dict):
        OHHOLog.print_log("add cellphone")
        result = self.cellphone.add_cellphone(cellphone_dict)
        OHHOLog.print_log(result)
        cellphone_id = result.get("cellphone_id", 0)
        return result, cellphone_id

    def check_code(self, username, code):
        OHHOLog.print_log("check code")
        result = Code.check_code(username, code)
        OHHOLog.print_log(result)
        return result

    def add_user(self, username, password):
        OHHOLog.print_log("add user")
        self.user.set_username(username)
        result = self.user.add_user(password)
        OHHOLog.print_log(result)
        return result

    def add_token(self):
        OHHOLog.print_log("login")
        result = self.user.add_token()
        OHHOLog.print_log(result)
        return result

    def add_user_extension(self, username):
        OHHOLog.print_log("add user extension")
        user = self.user.get_user()
        if user:
            result = self.user.add_user_extension(user.id, {"nickname": username})
        else:
            result = Result.result_failed("user does not exist!")
        OHHOLog.print_log(result)
        return result

    def add_match_condition(self):
        OHHOLog.print_log("add user extension")
        user = self.user.get_user()
        if user:
            result = self.user.add_new_condition(user.id)
        else:
            result = Result.result_failed("user %s does not exist!" % (self.user.get_username()))
        OHHOLog.print_log(result)
        return result

    def bind_device(self, identity_id, mac_address):
        OHHOLog.print_log("bind device")
        user = self.user.get_user()
        if user:
            self.device.set_identity(identity_id)
            self.device.set_mac_address(mac_address)
            result = self.device.bind_device(user.id)
        else:
            result = Result.result_failed("user %s does not exist!" % (self.user.get_username()))
        OHHOLog.print_log(result)
        return result

    def update_imei(self, identity_id, imei):
        try:
            if imei:
                self.device.set_identity(identity_id)
                device = self.device.get_by_identity()
                user = self.user.get_user()
                if device and user:
                    relation = self.imei.get_by_device(device.id)
                    if relation:
                        return Result.result_success("device %s has a imei before!" % (identity_id))
                    else:
                        imei_instance = self.imei.get_by_imei(imei)
                        if imei_instance:
                            return self.imei.update(imei_instance, user.id, device.id)
                        else:
                            return Result.result_failed("there is no such imei [%s]" % (imei))
                else:
                    return Result.result_failed(
                        "no such device [%s] or no such user [%s]" % (identity_id, self.user.get_username()))
            else:
                return Result.result_failed("parameter imei is illegal (empty)!")
        except Exception as ex:
            OHHOLog.print_log(ex)
            return Result.result_failed(ex)

    def add_user_and_cellphone_relation(self, cellphone_id):
        user = self.user.get_user()
        if user and cellphone_id:
            return self.cellphone.bind_cellphone(cellphone_id, user.id)
        else:
            return Result.result_failed(
                "user %s or cellphone %d does not exist!" % (self.user.get_username(), int(cellphone_id)))

    def register(self, base_url):
        """
        # - 验证码检查
        # - 添加用户（添加IM）
        # - 绑定硬件设备
        # - 添加手机信息
        # - 绑定手机设备
        :param register_dict:
        :return:
        """
        # 参数
        register_dict = self.register_dict
        cellphone_dict = self.cellphone_dict

        username = register_dict.get("username", "")
        password = register_dict.get("password", "")
        code = register_dict.get("code", "")
        identity_id = register_dict.get("identity_id", "")
        mac_address = register_dict.get("mac_address", "")
        imei = register_dict.get("imei", "")
        cellphone = register_dict.get("cellphone", "")
        if not cellphone:
            cellphone = username
        country_code = register_dict.get("country_code", "+86")

        add_user_result = dict()
        add_token_result = dict()

        # 添加手机信息
        add_cellphone_result, cellphone_id = self.add_cellphone(cellphone_dict)

        try:
            if username and password and code:
                # 验证码检查
                the_cellphone = country_code + cellphone
                is_code_correct = self.check_code(the_cellphone, code)
                if is_code_correct:

                    if not cellphone or not country_code:
                        OHHOLog.print_log("country code and cellphone number are needed!")
                        return Result.result_failed("country code and cellphone number are needed!")
                    else:
                        country_code_object = self.user.country_code.get_by_country_code(country_code)
                        if country_code_object and self.user.get_by_country_code_and_cellphone(country_code_object.id,
                                                                                               cellphone):
                            OHHOLog.print_log("cellphone number has been used!")
                            return Result.result_exist("cellphone number has been used!")

                    # 添加用户
                    # add_user_result = self.add_user(username, password)
                    add_user_result = self.add_new_user(password, cellphone, country_code)

                    if Result.does_user_exist(add_user_result):
                        return Result.result_exist()

                    if Result.is_user_added(add_user_result):
                        # 登录用户
                        add_token_result = self.add_token()

                        # 添加用户扩展
                        self.add_user_extension(cellphone)

                        # 添加配对条件
                        self.add_match_condition()

                        # 添加IM
                        self.add_im()

                        # 添加用户配置
                        self.add_configuration()

                        # 绑定设备
                        self.bind_device(identity_id, mac_address)

                        # 更新 imei
                        self.update_imei(identity_id, imei)

                        # 添加用户与手机的关系
                        self.add_user_and_cellphone_relation(cellphone_id)
                else:
                    OHHOLog.print_log("verification code is invalid!")
            else:
                OHHOLog.print_log("parameters are invalid!")
        except Exception as ex:
            OHHOLog.print_log(ex)

        if Result.is_user_added(add_user_result):

            if Result.is_success(add_token_result):
                result = Result.result_success()
            else:
                result = Result.result(CODE_LOGIN_FAILED, USER_NOT_LOGIN)
        else:
            result = Result.result_failed()

        user = self.user.get_user()

        if user and Result.is_success(result):
            result["data"] = self.user.get_user_information(user.id, base_url)

        return result

    def add_im(self):
        try:
            user = self.user.get_user()
            if user:
                user_id = user.id
                query = self.im_user.get_query()
                im_user = self.im_user.get_by_account(query, user_id)
                im_user = self.im_user.first(im_user)
                if im_user:
                    if not self.im_user.is_valid(im_user, True):
                        success = self.im_user.restore(im_user)
                        if success:
                            return Result.result_success(IM_USER_EXIST)
                        else:
                            return Result.result_failed(IM_USER_EXIST)
                    else:
                        return Result.result_success(IM_USER_EXIST)
                else:
                    success = RefreshToken.create_or_update(user_id)
                    if not success:
                        OHHOLog.print_log("refresh im failed!")
                        success = Create.add(user_id)
                        if success:
                            OHHOLog.print_log("create im successfully!")
                            return Result.result_success()
                        else:
                            OHHOLog.print_log("create im failed!")
                            success = RefreshToken.create_or_update(user_id)
                            if success:
                                OHHOLog.print_log("refresh im successfully at last!")
                                return Result.result_success()
                            else:
                                OHHOLog.print_log("refresh im failed at last!")
                                return Result.result_failed()
                    else:
                        OHHOLog.print_log("refresh im successfully at last!")
                        return Result.result_success()
            else:
                OHHOLog.print_log("user %s does not exist!" % (self.user.get_username()))
                return Result.result_failed()
        except Exception as ex:
            OHHOLog.print_log(ex)
            return Result.result_failed(ex)

    def add_configuration(self):
        user = self.user.get_user()
        if user:
            user_id = user.id
            configuration = self.configuration.get_by_user(user_id)
            data = dict()
            data["user_id"] = user_id
            data["is_match"] = 0
            data["is_online"] = 1
            if not configuration:
                return self.configuration.add(data)
            else:
                return self.configuration.update(configuration, data)
        else:
            return False

    def unregister(self, user_id):
        user = self.user.get_by_id(user_id)
        if user:
            data = dict()
            data["cellphone"] = ""
            data["last_cellphone"] = user.cellphone
            data["state"] = 0
            OHHOLog.print_log(data)
            success = self.user.update_user(user, data)

            imei_query = self.imei.get_query()
            imei_query = self.imei.get_by_user(imei_query, user_id)
            self.imei.delete_some(imei_query)

            token_instance = self.user.token.get(user_id)
            if token_instance:
                self.user.token.delete(token_instance)

            relation_query = self.user.user_and_device_relation.get_query()
            relation_query = self.user.user_and_device_relation.get_by_user(relation_query, user_id)
            self.user.user_and_device_relation.delete_some(relation_query)

            if success:
                IMUser.block(user_id)
                return Result.result_success()
            else:
                return Result.result_failed()
        else:
            return Result.result_failed("user %d does not exist!" % (int(user_id)))


if __name__ == "__main__":
    pass
