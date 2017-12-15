from ohho.common.view.view_ohho_base import ViewOHHOBase
from Tools.decorator import authenticate
from ohho.common.logic.ohho.feedback.logic_add_cancel_meet_feedback import LogicAddCancelMeetFeedback
from ohho.common.logic.ohho.meet.logic_cancel_meet import LogicCancelMeet
from ohho.common.logic.common.user import User
from ohho.common.logic.common.constant import *
from ohho.common.view.common.parameters import Post


class AddCancelMeetFeedbackHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        user = User()
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        friend_user_id = the_post.get_friend_id(self)
        apply_id = the_post.get_apply_id(self)
        category = the_post.get_category(self)
        reason = the_post.get_reason(self)
        content = the_post.get_content(self)
        base_url = the_post.get_base_url(self)

        cancel_meet = LogicCancelMeet()
        cancel_meet.cancel_meet(user_id, friend_user_id, apply_id, base_url)

        feedback = LogicAddCancelMeetFeedback()
        result = feedback.add_feedback(user_id, friend_user_id, apply_id, reason, content, category)

        information = user.get_cancel_meet_user_information(user_id, apply_id, base_url)
        information["message"] = content
        user.push_user_information(friend_user_id, PUSH_STATE_TYPE_CANCEL_MEET, information)

        return self.response(result)
        # self.set_status(status_code=201)
        # self.write(OHHOOperation.dict2json(result))

    def get(self):
        pass
        # result = dict()
        # self.set_status(status_code=200)
        # self.write(OHHOOperation.dict2json(result))
