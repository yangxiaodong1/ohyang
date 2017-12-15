from ohho.common.db.ohho.meet.db_ohho_temp_meet_address import DBOHHOTempMeetAddress
from ohho.common.logic.common.result import Result


class LogicWhereMeet(object):
    def __init__(self):
        self.meet_address = DBOHHOTempMeetAddress()

    def where_meet(self, user_id, apply_id, address_dict):
        apply_query = self.meet_address.get_by_apply(apply_id)
        if apply_query:
            result = Result.result_success()
            result["data"] = self.meet_address.get_information(apply_query)
        else:
            data = address_dict
            data["user_id"] = user_id
            data["apply_id"] = apply_id
            self.meet_address.add(data)
            apply_query = self.meet_address.get_by_apply(apply_id)
            if apply_query:
                result = Result.result_success()
                result["data"] = self.meet_address.get_information(apply_query)
            else:
                result = Result.result_failed()
                result["data"] = dict()
        return result
