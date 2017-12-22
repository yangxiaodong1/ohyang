from Chat.common.view.main_handler import MainHandler
from Chat.common.view.message_new_handler import MessageNewHandler
from Chat.common.view.message_update_handler import MessageUpdatesHandler
# from Test.common.view.view_phone_position import PhonePositionHandler
from Test.common.view.view_phone_distance import PhoneDistanceHandler
from Test.common.view.view_device_information import DeviceInformationHandler
from Test.common.view.view_test import TestBlockingHnadler, TestMainHandler, TestNoBlockingHnadler
from IM.netease.common.view.view_test import TestNetEaseHandler
from ohho.tests import *

handlers = [
    (r"/", MainHandler),
    (r"/a/message/new", MessageNewHandler),
    (r"/a/message/updates", MessageUpdatesHandler),
    # (r"/rest/api/positions/", PhonePositionHandler),
    (r"/rest/api/positions/", TestPhonePositionHandler),
    (r"/rest/api/distances/", PhoneDistanceHandler),
    (r"/rest/api/devices/", DeviceInformationHandler),
    (r"/rest/api/test/main/", TestMainHandler),
    (r"/rest/api/test/block/", TestBlockingHnadler),
    (r"/rest/api/test/noblock/", TestNoBlockingHnadler),
    (r"/rest/api/test/netease/", TestNetEaseHandler),

    # test rssi
    (r"/rest/api/test/rssi/add/", TestAddRssiHandler),
    (r"/rest/api/test/rssi/compute/", TestComputeRssiHandler),
    # test interest point
    (r"/rest/api/test/interest/point/add/", TestAddInterestPointHandler),

    # test map
    (r"/rest/api/test/map/add/", TestAddMapInformationHandler),

    # delete apply
    (r"/rest/api/test/delete/apply/", DeleteApplyHandler),

    # show push user information
    (r"/rest/api/test/show/user/information/", TestShowUserBasicInformation),

    # test add new user
    (r"/rest/api/test/add/new/user/", TestAddNewUserHandler),
    # (r"/rest/api/test/map/information/add/", TestAddMapInformationHandler),

    # test met
    (r"/rest/api/test/met/", TestMetHandler),

]
