import os

DBMysql = [
    # {
    #     "user": "root",
    #     "password": "111111",
    #     "host": "localhost",
    #     # "host": "192.168.253.253",
    #     "db": "ohho"
    # },
    # {
    #     "user": "root",
    #     "password": "111111",
    #     "host": "localhost",
    #     "db": "test001"
    # },
    {
        "user": "test",
        "password": "123456",
        "host": "192.168.253.16",
        # "host": "192.168.253.253",
        "db": "ohho"
    },

]

DBMongo = {
    "user": "",
    "password": "",
    "host": "localhost",
    "db": "ohho"
}

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__)) + "/"
LOG_PATH = CURRENT_PATH + "logs/ohho.log"
IS_LOG2TERMINAL = True
LOG_FILE_MAX_SIZE = 1024 * 10000
LOG_FILE_NUMBER_BACKUPS = 3
LOGIN_URL = "/backstage/login/"

IPV4_ONLY = False
# PORT = 8878
# PORT = 1346
PORT = 1345
DEBUG = True
COOKIE_SECRET = "QMlAIhXKQBSrLm9NNzpN6LoygSDhh0BCp6Rxz3GvEyc="
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "ohho/templates")
STATIC_PATH = os.path.join(os.path.dirname(__file__), "static")
XSRF_COOKIES = False
AUTO_RELOAD = True

TEST = True
DEFAULT_IM_USER_ID = 4

if __name__ == "__main__":
    import base64
    import uuid

    cookie_secret = base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
    print(cookie_secret)
    print(len(cookie_secret))

    print(CURRENT_PATH)
    print(LOG_PATH)
    print(TEMPLATE_PATH)
