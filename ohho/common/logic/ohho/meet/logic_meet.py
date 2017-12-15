from ohho.common.db.im.db_ohho_im_user_request_relation import DBOHHOIMUserRequestRelation
from ohho.common.logic.common.record.meet import Meet
from ohho.common.logic.common.result import Result
from ohho.common.logic.common.user import User
from ohho.common.logic.common.record.friend import Friend
from Tools.ohho_datetime import OHHODatetime
from settings import TEST


class LogicMeet(object):
    def __init__(self):
        self.user = User()
        self.meet = Meet()
        self.friend = Friend()

    def met(self, user_id, last_id, limit, base_url):
        met_list = self.meet.get_meet(user_id, last_id)
        blacks = self.friend.get_black_by_user(user_id)
        black_list = [b.friend_account_id for b in blacks] if blacks else list()
        data = list()
        count = 0
        for met in met_list:
            another_user_id = met.user_id if met.another_user_id == int(user_id) else met.another_user_id
            if another_user_id in black_list:
                continue
            temp = self.user.get_friend_information(user_id, another_user_id, met.apply_id, base_url)
            if temp:
                temp["last_id"] = met.id
                temp["apply_id"] = met.apply_id
                temp["created_at"] = OHHODatetime.clock2string(OHHODatetime.utc2beijing(met.created_at))

                data.append(temp)
                count += 1
            if limit and int(limit) > 0:
                if count >= int(limit):
                    break
        result = Result.result_success()
        result["data"] = data

        return result


        # if TEST:
        #     data = list()
        #     users = self.user.get_all()
        #     if self.user.user.is_empty(users):
        #         pass
        #     else:
        #         for user in users:
        #             if user.id == user_id:
        #                 continue
        #             else:
        #                 temp = self.user.get_user_basic_information(user.id)
        #                 if temp:
        #                     if self.friend.is_friend_or_black(user_id, user.id):
        #                         temp["is_friend_or_black"] = True
        #                     else:
        #                         temp["is_friend_or_black"] = False
        #                     data.append(temp)
        # else:


        #
        # relations = self.meet.get_meet(user_id, last_id)
        #
        # data = list()  # add user information by relations
        # count = 0
        # for relation in relations:
        #     apply = self.meet.apply.get_by_id(relation.apply_id)
        #     if apply:
        #         another_user_id = apply.one_user_id if apply.another_user_id == user_id else apply.another_user_id
        #         temp = self.user.get_friend_information(user_id, another_user_id, apply.id, base_url)
        #         if temp:
        #             # if self.friend.is_friend_or_black(user_id, another_user_id):
        #             #     temp["is_friend_or_black"] = True
        #             # else:
        #             #     temp["is_friend_or_black"] = False
        #             temp["last_id"] = relation.id
        #             data.append(temp)
        #             count += 1
        #
        #             if limit and int(limit) > 0:
        #                 if count >= int(limit):
        #                     break
        #
        # result = Result.result_success()
        # result["data"] = data
        #
        # return result
