# -*- coding: utf-8 -*-
from sys import argv
from aliyunsdkdysmsapi.request.v20170525 import SendSmsRequest
from aliyunsdkdysmsapi.request.v20170525 import QuerySendDetailsRequest
from aliyunsdkcore.client import AcsClient
import uuid

"""
短信产品-发送短信接口
Created on 2017-06-12
"""
REGION = "cn-hangzhou"  # 暂时不支持多region
# ACCESS_KEY_ID/ACCESS_KEY_SECRET 根据实际申请的账号信息进行替换
ACCESS_KEY_ID = "LTAI4pdh6hpKLfzx"
ACCESS_KEY_SECRET = "1j18Lqs3c9hxESEtmEYwSB0HAdIz3e"
acs_client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, REGION)


# 请参考本文档步骤2
def send_sms(business_id, phone_number, sign_name, template_code, template_param=None):
    smsRequest = SendSmsRequest.SendSmsRequest()
    # 申请的短信模板编码,必填
    smsRequest.set_TemplateCode(template_code)
    # 短信模板变量参数,友情提示:如果JSON中需要带换行符,请参照标准的JSON协议对换行符的要求,比如短信内容中包含\r\n的情况在JSON中需要表示成\\r\\n,否则会导致JSON在服务端解析失败
    if template_param is not None:
        smsRequest.set_TemplateParam(template_param)
    # 设置业务请求流水号，必填。
    smsRequest.set_OutId(business_id)
    # 短信签名
    smsRequest.set_SignName(sign_name);
    # 短信发送的号码，必填。支持以逗号分隔的形式进行批量调用，批量上限为1000个手机号码,批量调用相对于单条调用及时性稍有延迟,验证码类型的短信推荐使用单条调用的方式
    smsRequest.set_PhoneNumbers(phone_number)
    # 发送请求
    smsResponse = acs_client.do_action_with_exception(smsRequest)
    print(smsResponse)
    return smsResponse


import chardet

__business_id = uuid.uuid1()
# print("business_id")
# print(__business_id)
# phone_number = "13161916437"
# sign_name = "阿里云短信测试专用"
# template_code = "SMS_85890021"
# params = "{'code':'1234'}"
# print(argv[1] == phone_number)
# # print(argv[2].decode("GB2312") == sign_name.encode("utf8"))
#
# print(chardet.detect(argv[2]))
# test21 = argv[2].decode("GB2312")
# print(chardet.detect(sign_name))
# test22 = sign_name.decode("utf8")
#
# print(test21 == test22)
#
# print(argv[3] == template_code)
#
# print(argv[4] == params)
#
# print(chardet.detect(argv[4]))
# print(argv[4])
# print(chardet.detect(params))
# print(params)

phone_number = argv[1]
encoding_dict = chardet.detect(argv[2])
sign_name = argv[2].decode(encoding_dict["encoding"]).encode("utf8")
template_code = argv[3]
params = argv[4]

# send_sms(__business_id, argv[1], argv[2], argv[3], argv[4])
send_sms(__business_id, phone_number, sign_name, template_code, params)
