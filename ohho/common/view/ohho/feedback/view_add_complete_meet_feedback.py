from ohho.common.view.view_ohho_base import ViewOHHOBase
from Tools.decorator import authenticate
from ohho.common.logic.ohho.feedback.logic_add_complete_meet_feedback import LogicAddCompleteMeetFeedback
from ohho.common.view.common.parameters import Post


class AddCompleteMeetFeedbackHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        friend_user_id = the_post.get_friend_id(self)
        apply_id = the_post.get_apply_id(self)
        score = the_post.get_score(self)
        impression = the_post.get_impression(self)
        content = the_post.get_content(self)
        category = the_post.get_category(self)
        feedback = LogicAddCompleteMeetFeedback()
        result = feedback.add_feedback(user_id, friend_user_id, apply_id, score, impression, content, category)

        return self.response(result)
        # self.set_status(status_code=201)
        # self.write(OHHOOperation.dict2json(result))

    def get(self):
        pass
        # result = dict()
        # self.set_status(status_code=200)
        # self.write(OHHOOperation.dict2json(result))
