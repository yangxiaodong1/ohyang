from ohho.common.db.ohho.record.db_ohho_record_friend_apply import DBOHHORecordFriendApply
from ohho.common.db.ohho.record.db_ohho_record_friend_agree import DBOHHORecordFriendAgree
from ohho.common.db.ohho.record.db_ohho_record_friend_refuse import DBOHHORecordFriendRefuse
from ohho.common.db.ohho.im.db_ohho_im_user_relation import DBOHHOIMUserRelation

from ohho.common.logic.common.result import Result
from ohho.common.db.im.constant import *
from Tools.ohho_log import OHHOLog


class Friend(object):
    def __init__(self):
        self.apply = DBOHHORecordFriendApply()
        self.agree = DBOHHORecordFriendAgree()
        self.refuse = DBOHHORecordFriendRefuse()
        self.friend = DBOHHOIMUserRelation()

    def get_valid_by_account(self, user_id):
        query = self.friend.get_query()
        query = self.friend.get_valid(query, True)
        return self.friend.get_by_account(query, user_id)

    def is_valid_apply(self, instance):
        if instance:
            is_not_timeout = self.apply.is_valid_instance(instance)
            the_friend = self.friend.get_by_apply(instance.id)
            if the_friend:
                return False
            elif is_not_timeout:
                return True
            else:
                return False
        return False

    def has_valid_apply(self, user_id, friend_user_id):
        """
        获取最新的有效申请
        如果没有被拒绝，则有效；否则无效。
        :param user_id:
        :param friend_user_id:
        :return:
        """
        apply = self.get_apply_by_user_and_friend(user_id, friend_user_id)
        is_valid_apply = self.apply.is_valid_instance(apply)
        if is_valid_apply:
            nearest_refuse = self.refuse.get_nearest_refuse(apply.id)
            if nearest_refuse:
                return False
            else:
                return True
        return False

    def is_friend(self, user_id, friend_user_id):
        friend = self.get_friend_by_user_and_friend(user_id, friend_user_id)
        if friend:
            return True
        return False

    def remove_friend(self, instance):
        return self.friend.delete(instance)

    def is_black(self, user_id, friend_user_id):
        instance = self.get_friend_by_user_and_friend(user_id, friend_user_id)
        if self.is_friend_valid(instance):
            return self.friend.is_black(instance)
        return False

    def is_friend_or_black(self, user_id, friend_user_id):
        # 你是我的朋友
        friend = self.get_friend_by_user_and_friend(user_id, friend_user_id)
        # 我在你的黑名单中
        black = self.get_black_by_user_and_friend(friend_user_id, user_id)
        # 你在我的黑名单中
        black_reverse = self.get_black_by_user_and_friend(user_id, friend_user_id)
        if friend or black or black_reverse:
            return True
        return False

    def get_friend_by_user(self, user_id):
        query = self.friend.get_query()
        query = self.friend.get_valid(query, True)
        query = self.friend.get_friends(query)
        # query = self.friend.get_by_apply_id_is_not_none(query)
        return self.friend.get_by_account(query, user_id)

    def get_black_by_user(self, user_id):
        query = self.friend.get_query()
        query = self.friend.get_valid(query, True)
        query = self.friend.get_blacks(query)
        return self.friend.get_by_account(query, user_id)

    def get_black_by_user_and_friend(self, user_id, friend_user_id):
        query = self.get_black_by_user(user_id)
        query = self.friend.get_by_friend(query, friend_user_id)
        query = self.friend.order_by_id_asc(query)
        return self.friend.first(query)

    def get_friend_by_friend(self, friend_id):
        query = self.friend.get_query()
        return self.friend.get_by_friend(query, friend_id)

    def get_friend_by_user_and_friend(self, user_id, friend_user_id):
        query = self.get_friend_by_user(user_id)
        query = self.friend.get_by_friend(query, friend_user_id)
        query = self.friend.get_by_apply_id_is_not_none(query)
        query = self.friend.order_by_id_asc(query)
        OHHOLog.print_log(self.friend.get_count(query))
        return self.friend.first(query)

    def is_friend_valid(self, friend):
        if friend:
            return friend.state
        else:
            return False

    def get_apply_by_user(self, user_id):
        query = self.apply.get_query()
        return self.apply.get_by_one_user(query, user_id)

    def get_apply_by_friend(self, friend_user_id):
        query = self.apply.get_query()
        return self.apply.get_by_another_user(query, friend_user_id)

    def get_apply_by_user_and_friend(self, user_id, friend_user_id):
        query = self.get_apply_by_user(user_id)
        query = self.apply.get_by_another_user(query, friend_user_id)
        query = self.apply.order_by_id_desc(query)
        return self.apply.first(query)

    def add_apply(self, user_id, friend_user_id):
        data = dict()
        data["one_user_id"] = user_id
        data["another_user_id"] = friend_user_id
        return self.apply.add(data)

    def add_agree(self, apply_id):
        data = dict()
        data["apply_id"] = apply_id
        return self.agree.add(data)

    def black2friend(self, instance):
        return self.friend.update_to_friend(instance)

    def add_friend(self, user_id, friend_user_id, apply_id):
        friend = self.get_friend_by_user_and_friend(user_id, friend_user_id)
        if friend:
            success1 = True
        else:
            data = dict()
            data["account_id"] = user_id
            data["friend_account_id"] = friend_user_id
            data["apply_id"] = apply_id
            success1 = self.friend.add(data)

        friend = self.get_friend_by_user_and_friend(friend_user_id, user_id)
        if friend:
            success2 = True
        else:
            data = dict()
            data["account_id"] = friend_user_id
            data["friend_account_id"] = user_id
            data["apply_id"] = apply_id
            success2 = self.friend.add(data)

        if success1 and success2:
            return Result.result_success()
        else:
            return Result.result_failed()

    def add_black(self, instance):
        return self.friend.update_to_black(instance)

    def get_blacks(self, user_id):
        query = self.get_black_by_user(user_id)
        query = self.friend.get_blacks(query)
        return query

    def add_refuse(self, apply_id, user_id):
        data = dict()
        data["apply_id"] = apply_id
        data["user_id"] = user_id
        return self.refuse.add(data)

    def get_friend(self, user_id, last_id):
        friends = self.friend.get_query()
        friends = self.friend.get_valid(friends, True)
        friends = self.friend.get_by_user(friends, user_id)
        friends = self.friend.get_friends(friends)
        friends = self.friend.order_by_id_desc(friends)
        last_id = int(last_id)
        # applies = self.get_apply_by_user(user_id)
        # applies_reverse = self.get_apply_by_friend(user_id)
        # apply_ids = [apply.id for apply in applies]
        # apply_reverse_ids = [apply.id for apply in applies_reverse]
        # apply_id_list = apply_ids + apply_reverse_ids
        # friend = self.friend.find_by_apply(apply_id_list)
        if last_id > 0:
            friends = self.friend.get_less_than_id(friends, last_id)
        return friends
