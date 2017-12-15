# coding: utf-8
import os
import json
import platform
import sys

if sys.version < '3':
    reload(sys)
    sys.setdefaultencoding('utf-8')

SIGN_NAME = "阿里云短信测试专用"
TEMPLATE_CODE = "SMS_85890021"
the_platform = platform.system()
if the_platform == "Windows":
    PYTHON2PATH = r"C:\Python27\python"
elif the_platform == "Linux":
    PYTHON2PATH = r"/bin/python"
current_path = os.path.dirname(os.path.abspath(__file__)) + "/"
NAME = current_path + "alidayu_send"


def execute_python2(phone_name,
                    params,
                    sign_name=SIGN_NAME,
                    template_code=TEMPLATE_CODE,
                    python2path=PYTHON2PATH,
                    name=NAME):
    cmd = python2path + " " + name + ".py " + phone_name + " " + sign_name + " " + template_code + " " + params
    print(cmd)
    command = os.popen(cmd, mode='r')
    # print(command.__dict__)
    try:
        result = command.readlines()
    except:
        result = list()
    # print("result", end=":")
    # print(result)
    if result:
        result_string = result[0][:-1]
        result_string_dict = json.loads(result_string)
        return result_string_dict
    else:
        return dict()


if __name__ == "__main__":
    phone_name = "13161916437"
    params = "{'code':'9990'}"
    content = execute_python2(phone_name, params)
    # result = content.readlines()
    # result_string = result[0][:-1]
    # result_string_dict = json.loads(result_string)
    print(content)
