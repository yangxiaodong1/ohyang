import os
import tornado.ioloop
import tornado.web
from tornado.httpserver import HTTPServer
from tornado.netutil import bind_sockets
from handlers.handlers import handlers

from settings import IPV4_ONLY
from settings import PORT
from settings import DEBUG
from settings import XSRF_COOKIES
from settings import AUTO_RELOAD
from settings import TEMPLATE_PATH
from settings import STATIC_PATH
from settings import COOKIE_SECRET
from settings import LOG_PATH
from settings import IS_LOG2TERMINAL
from settings import LOG_FILE_MAX_SIZE
from settings import LOG_FILE_NUMBER_BACKUPS
from settings import LOGIN_URL
from Tools.ohho_platform import OHHOPlatform
from Tools.ohho_log import OHHOLog

from tornado.options import define, options, parse_command_line

define("port", default=PORT, help="run on the given port", type=int)
define("debug", default=DEBUG, help="run in debug mode")
define("log_file_prefix", default=LOG_PATH, help="write log to file")
# define("log_to_stderr", default=IS_LOG2TERMINAL, help="write log to terminal")
define("log_file_max_size", default=LOG_FILE_MAX_SIZE, help="log file max size")
define("log_file_num_backups", default=LOG_FILE_NUMBER_BACKUPS, help="log file number backups")
parse_command_line()


def get_app():
    app = tornado.web.Application(
        handlers,
        cookie_secret=COOKIE_SECRET,
        template_path=TEMPLATE_PATH,
        static_path=STATIC_PATH,
        xsrf_cookies=XSRF_COOKIES,
        autoreload=AUTO_RELOAD,
        debug=DEBUG,
        login_url=LOGIN_URL,
    )
    return app


if __name__ == "__main__":
    if IPV4_ONLY:
        import socket

        sockets = bind_sockets(options.port, family=socket.AF_INET)
    else:
        sockets = bind_sockets(options.port)
    if not DEBUG:
        import tornado.process

        tornado.process.fork_processes(0)  # 0 表示按CPU数目创建相应数据的子进程

    SSL = True

    import ssl

    ssl_ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)

    if OHHOPlatform.is_windows():
        cert_file = os.path.join(os.path.abspath("."), "ca/server-cert.pem")
        key_file = os.path.join(os.path.abspath("."), "ca/server-key.pem")
    elif OHHOPlatform.is_linux():
        cert_file = os.path.join(os.path.abspath("."), "ca/linux-server-cert.pem")
        key_file = os.path.join(os.path.abspath("."), "ca/linux-server-key.pem")
    else:
        cert_file = ""
        key_file = ""

    try:
        result = ssl_ctx.load_cert_chain(cert_file, key_file)
        OHHOLog.print_log(result)
    except Exception as ex:
        OHHOLog.print_log(ex)
    OHHOLog.print_log("test end")

    app = get_app()
    server = HTTPServer(app, xheaders=True)
    server.add_sockets(sockets)
    # server = HTTPServer(app)

    server1 = HTTPServer(app, ssl_options=ssl_ctx)
    server1.listen(18888)

    tornado.ioloop.IOLoop.current().start()
