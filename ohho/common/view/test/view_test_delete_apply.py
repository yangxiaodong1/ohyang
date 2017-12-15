import tornado.web
from Tools.ohho_operation import OHHOOperation
from ohho.common.logic.common.result import Result
from ohho.common.db.record.db_ohho_record_match_apply import DBOHHORecordMatchApply
from ohho.common.db.record.db_ohho_record_match_agree import DBOHHORecordMatchAgree
from ohho.common.db.record.db_ohho_record_match_refuse import DBOHHORecordMatchRefuse
from ohho.common.db.record.db_ohho_record_match_duplex_agree import DBOHHORecordMatchDuplexAgree

from ohho.common.db.record.db_ohho_record_match_meeting import DBOHHORecordMatchMeeting
from ohho.common.db.record.db_ohho_record_match_meet import DBOHHORecordMatchMeet
from ohho.common.db.record.db_ohho_record_match_meet_end import DBOHHORecordMatchMeetEnd
from ohho.common.db.record.db_ohho_record_match_met import DBOHHORecordMatchMet

from ohho.common.db.record.db_ohho_record_friend_apply import DBOHHORecordFriendApply
from ohho.common.db.record.db_ohho_record_friend_agree import DBOHHORecordFriendAgree
from ohho.common.db.record.db_ohho_record_friend_refuse import DBOHHORecordFriendRefuse

from ohho.common.db.im.db_ohho_im_user_relation import DBOHHOIMUserRelation

from ohho.common.db.record.db_ohho_record_exclude import DBOHHORecordExclude


class DeleteApplyHandler(tornado.web.RequestHandler):
    def post(self):
        pass
        # name = self.get_body_argument("user_name", None)
        # result = dict()
        # result["user_name"] = name
        #
        # self.write(OHHOOperation.dict2json(result))
        # self.write("This is a %s method, %s is not supported" % ("get", "post"))

    def get(self):
        apply = DBOHHORecordMatchApply()
        apply.delete_all()
        agree = DBOHHORecordMatchApply()
        agree.delete_all()
        refuse = DBOHHORecordMatchApply()
        refuse.delete_all()
        exclude = DBOHHORecordMatchApply()
        exclude.delete_all()
        duplex_agree = DBOHHORecordMatchDuplexAgree()
        duplex_agree.delete_all()

        meeting = DBOHHORecordMatchMeeting()
        meet = DBOHHORecordMatchMeet()
        meet_end = DBOHHORecordMatchMeetEnd()
        met = DBOHHORecordMatchMet()
        meeting.delete_all()
        meet.delete_all()
        meet_end.delete_all()
        met.delete_all()

        friend_apply = DBOHHORecordFriendApply()
        friend_agree = DBOHHORecordFriendAgree()
        friend_refuse = DBOHHORecordFriendRefuse()

        friend_apply.delete_all()
        friend_agree.delete_all()
        friend_refuse.delete_all()

        relation = DBOHHOIMUserRelation()
        relation.delete_all()

        # 使上面的语句生效
        apply.commit()

        result = Result.result_success()
        return self.write(OHHOOperation.dict2json(result))
        # self.write({"name": "get"})
        # the_get = Get()
        # device_identities = the_get.get_device_identities(self)
        # identity_list = device_identities.split(",")
        # result = LogicTestGetUserByDevice.get(identity_list)
        # self.write(OHHOOperation.dict2json(result))
