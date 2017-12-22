from ohho.common.db.im.db_ohho_im_temporary_message import DBOHHOIMTemporaryMessage
from ohho.common.logic.common.result import Result
from ohho.common.logic.common.im.netease.send_message import SendMessage
from Tools.ohho_log import OHHOLog
from Tools.ohho_operation import OHHOOperation
from Tools.ohho_datetime import OHHODatetime


class LogicMeetSendMessage(object):
    def __init__(self):
        self.message = DBOHHOIMTemporaryMessage()
        self.send_message = SendMessage()

    def send(self, user_id, friend_user_id, content, type):
        result = Result.result_success()

        data = dict()
        data["account_id"] = user_id
        data["another_account_id"] = friend_user_id
        data["message"] = content
        success = self.message.add(data)
        if success:
            OHHOLog.print_log("add message to database successfully!")
        else:
            OHHOLog.print_log("add message to database failed!")
        result["add2db"] = success
        message = dict()
        msg = dict()
        msg["content"] = content
        msg["user_id"] = user_id
        msg["type"] = type
        msg["current_timestamp"] = OHHODatetime.get_current_timestamp()
        message["msg"] = msg
        success = self.send_message.send_attach_message(user_id, friend_user_id, OHHOOperation.dict2json(message))
        OHHOLog.print_log(success)
        result["send2im"] = success
        return result
