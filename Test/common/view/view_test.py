import time
import tornado.ioloop
import tornado.web
import tornado.options
from tornado import gen

tornado.options.parse_command_line()


@gen.coroutine
def switch():
    yield


async def coro1():
    print("C1: Start")
    await switch()
    print("C1: Stop")


async def coro2():
    print("C2: Start")
    print("C2: a")
    print("C2: b")
    print("C2: c")
    print("C2: Stop")


class TestMainHandler(tornado.web.RequestHandler):
    async def get(self):
        # 测试命令行： curl -H "user_id:20" http://localhost:8878/rest/api/test/main/
        headers = self.request.headers
        if "user_id" in headers:
            self.write(self.request.headers["user_id"])
        else:
            self.write("no such key")
        # username = self.get_secure_cookie("username")
        # if not username:
        #     self.set_secure_cookie("username", "lileliang")
        # c1 = coro1()
        # c2 = coro2()
        # print(c1, c2)
        # await c1
        # try:
        #     c1.send(None)
        # except:
        #     pass
        # try:
        #     c2.send(None)
        # except:
        #     pass
        # if username:
        #     self.write(username)
        # else:
        #     self.write("no username")
        # self.finish()


class TestNoBlockingHnadler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        yield gen.sleep(10)
        self.write('No Blocking Request')


class TestBlockingHnadler(tornado.web.RequestHandler):
    def get(self):
        time.sleep(10)
        self.write('Blocking Request')
