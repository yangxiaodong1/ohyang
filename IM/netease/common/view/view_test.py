from tornado.web import RequestHandler

from IM.netease.common.logic.logic_header import LogicHeader


class TestNetEaseHandler(RequestHandler):
    def get(self):
        self.write(LogicHeader.get_check_sum())
