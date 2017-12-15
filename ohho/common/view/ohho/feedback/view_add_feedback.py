from ohho.common.view.view_ohho_base import ViewOHHOBase
from Tools.decorator import authenticate
from ohho.common.logic.ohho.feedback.logic_add_feedback import LogicAddFeedback
from ohho.common.view.common.parameters import Post


class AddFeedbackHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        feedback_type = the_post.get_type(self)
        content = the_post.get_content(self)
        feedback = LogicAddFeedback()
        result = feedback.add_feedback(user_id, feedback_type, content)

        return self.response(result)
        # self.set_status(status_code=201)
        # self.write(OHHOOperation.dict2json(result))

    def get(self):
        pass
        # result = dict()
        # self.set_status(status_code=200)
        # self.write(OHHOOperation.dict2json(result))
