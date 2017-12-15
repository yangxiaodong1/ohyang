import tornado.web
from tornado import gen
from Chat.common.view.message_buffer import global_message_buffer


class MessageUpdatesHandler(tornado.web.RequestHandler):
    async def post(self):
        cursor = self.get_argument("cursor", None)
        self.future = global_message_buffer.wait_for_messages(cursor=cursor)
        messages = await self.future
        if self.request.connection.stream.closed():
            return
        self.write(dict(message=messages))

    # @gen.coroutine
    # def post(self):
    #     cursor = self.get_argument("cursor", None)
    #     # Save the future returned by wait_for_messages so we can cancel
    #     # it in wait_for_messages
    #     self.future = global_message_buffer.wait_for_messages(cursor=cursor)
    #     messages = yield self.future
    #     if self.request.connection.stream.closed():
    #         return
    #     self.write(dict(messages=messages))

    def on_connection_close(self):
        global_message_buffer.cancel_wait(self.future)
