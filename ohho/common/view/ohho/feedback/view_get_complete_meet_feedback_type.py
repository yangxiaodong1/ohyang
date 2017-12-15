from ohho.common.view.view_ohho_base import ViewOHHOBase
from Tools.decorator import authenticate
from ohho.common.db.ohho.base.db_ohho_interest import DBOHHOInterest
from ohho.common.view.common.parameters import Get


class GetCompleteMeetFeedbackTypeHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        pass
        # the_post = Post()
        # self.set_format(the_post.get_format(self))
        # user_id = the_post.get_user_id(self)
        # feedback_type = the_post.get_type(self)
        # content = the_post.get_content(self)
        # feedback = LogicAddFeedback()
        # result = feedback.add_feedback(user_id, feedback_type, content)
        #
        # return self.response(result)
        # self.set_status(status_code=201)
        # self.write(OHHOOperation.dict2json(result))

    def get(self):
        result = dict()
        the_get = Get()
        self.set_format(the_get.get_format(self))
        interest = DBOHHOInterest()

        result["type"] = interest.get_complete_meet_feedback_type()
        return self.response(result)

        # result = dict()
        # self.set_status(status_code=200)
        # self.write(OHHOOperation.dict2json(result))
