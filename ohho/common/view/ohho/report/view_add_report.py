from Tools.decorator import authenticate
from Tools.ohho_operation import OHHOOperation
from ohho.common.logic.ohho.report.logic_add_report import LogicAddReport
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


class AddReportHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        reported_user_id = the_post.get_reported_user_id(self)
        report_type = the_post.get_type(self)
        content = the_post.get_content(self)
        instance = LogicAddReport()
        result = instance.add_report(user_id, reported_user_id, report_type, content)
        return self.response(result)

    def get(self):
        result = dict()
        self.set_status(status_code=200)
        self.write(OHHOOperation.dict2json(result))
