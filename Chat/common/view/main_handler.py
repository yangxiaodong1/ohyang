import tornado.web
from Chat.common.view.message_buffer import global_message_buffer


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", messages=global_message_buffer.cache)
