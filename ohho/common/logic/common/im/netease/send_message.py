from ohho.common.logic.common.im.netease.constant import *
from ohho.common.logic.common.im.netease.header import Header
from ohho.common.db.im.db_ohho_im_user import DBOHHOIMUser
from Tools.ohho_http import OHHOHttp
from Tools.ohho_log import OHHOLog
from Tools.ohho_operation import OHHOOperation


class SendMessage(object):
    @staticmethod
    def set_parameter(parameter_dict, name, value):
        if value:
            parameter_dict[name] = value
        return parameter_dict

    @staticmethod
    def send_message(from_, to, body, operation=0, type=0, anti_spam=False, anti_spam_custom=dict(),
                     option=dict(), push_content="", payload="", extension="", force_push_list=list(),
                     force_push_content="", force_push_all=False):
        url = URL_SEND_MESSAGE
        headers = Header.get_create_header()
        data = dict()
        data[PARAMETER_SEND_MESSAGE_FROM] = from_
        data[PARAMETER_SEND_MESSAGE_OPERATION] = operation
        data[PARAMETER_SEND_MESSAGE_TO] = to
        data[PARAMETER_SEND_MESSAGE_TYPE] = type
        data[PARAMETER_SEND_MESSAGE_BODY] = body
        data[PARAMETER_SEND_MESSAGE_ANTI_SPAM] = anti_spam
        data[PARAMETER_SEND_MESSAGE_FORCE_PUSH_ALL] = force_push_all
        data = SendMessage.set_parameter(data, PARAMETER_SEND_MESSAGE_ANTI_SPAM_CUSTOM, anti_spam_custom)
        data = SendMessage.set_parameter(data, PARAMETER_SEND_MESSAGE_OPTION, option)
        data = SendMessage.set_parameter(data, PARAMETER_SEND_MESSAGE_PUSH_CONTENT, push_content)
        data = SendMessage.set_parameter(data, PARAMETER_SEND_MESSAGE_PAYLOAD, payload)
        data = SendMessage.set_parameter(data, PARAMETER_SEND_MESSAGE_EXTENSION, extension)
        data = SendMessage.set_parameter(data, PARAMETER_SEND_MESSAGE_FORCE_PUSH_LIST, force_push_list)
        data = SendMessage.set_parameter(data, PARAMETER_SEND_MESSAGE_FORCE_PUSH_CONTENT, force_push_content)

        print(data)
        response = OHHOHttp.post(url, headers, data)
        return response

    @staticmethod
    def send_attach_message(from_, to, attach, message_type=0,
                            push_content="", payload="", sound="",
                            save=2, option=dict()):
        url = URL_SEND_SYSTEM_MESSAGE
        headers = Header.get_create_header()
        data = dict()
        data[PARAMETER_SEND_SYSTEM_MESSAGE_FROM] = from_
        data[PARAMETER_SEND_SYSTEM_MESSAGE_TO] = to
        data[PARAMETER_SEND_SYSTEM_MESSAGE_ATTACH] = attach
        # OHHOLog.print_log(attach)
        data[PARAMETER_SEND_SYSTEM_MESSAGE_MESSAGE_TYPE] = message_type
        data[PARAMETER_SEND_SYSTEM_MESSAGE_SAVE] = save
        data = SendMessage.set_parameter(data, PARAMETER_SEND_SYSTEM_MESSAGE_PUSH_CONTENT, push_content)
        data = SendMessage.set_parameter(data, PARAMETER_SEND_SYSTEM_MESSAGE_PAYLOAD, payload)
        data = SendMessage.set_parameter(data, PARAMETER_SEND_SYSTEM_MESSAGE_SOUND, sound)
        data = SendMessage.set_parameter(data, PARAMETER_SEND_SYSTEM_MESSAGE_OPTION, option)
        # OHHOLog.print_log("send attach message")
        response = OHHOHttp.post(url, headers, data)
        # OHHOLog.print_log(response)
        return response

    @staticmethod
    def update2db(response):
        instance = DBOHHOIMUser()
        response_dict = OHHOOperation.json2dict(response)
        code = response_dict[RESPONSE_NAME_CODE]
        if code == RESPONSE_CODE_SUCCESS:
            info = response_dict[RESPONSE_NAME_INFO]
            accid = info[RESPONSE_NAME_INFO_ACCID]
            query = instance.get_query()
            obj = instance.get_by_account(query, accid)
            obj = instance.first(obj)
            if obj:
                data = dict()
                data["token"] = info[RESPONSE_NAME_INFO_TOKEN]
                success = instance.update(obj, data)
                return success
            else:
                data = dict()
                data["token"] = info[RESPONSE_NAME_INFO_TOKEN]
                data["account_id"] = info[RESPONSE_NAME_INFO_ACCID]
                success = instance.add(data)
                return success
        return False


if __name__ == "__main__":
    # print("hello, world")
    from_ = 4
    to = 5
    body = {"msg": [{"name": 1}]}

    print(SendMessage.send_message(from_, to, OHHOOperation.dict2json(body)))
