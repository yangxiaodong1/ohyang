from ohho.common.view.common.parameters import Get, Post
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.logic.common.device import Device
from tornado.web import authenticated
from ohho.common.view.backstage.constant import *
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate


class BackstageDeviceBatchAddHandler(BaseHandler):
    @backstage_authenticate
    def post(self):
        image_file = self.request.files.get("hardware")
        if image_file:
            body = image_file[0]["body"]
            body = body.decode("utf-8")
            instance = Device()
            temp = False
            for index, i in enumerate(body.split("\r\n")):
                if i and index:
                    data = dict()
                    list_i = i.split(",")
                    if not list_i[2]:
                        list_i[2] = 20
                    if not list_i[3]:
                        list_i[3] = "0000000000"
                    try:
                        print(list_i)
                        data["identity_id"] = str(list_i[0])
                        data["mac_address"] = str(list_i[1])
                        data["tx_power"] = int(list_i[2])
                        data["application_id"] = str(list_i[3])
                        instance.set_identity(list_i[0])
                        query = instance.get_by_identity()
                        if not query and str(list_i[0]):
                            success = instance.add(data)
                            if success:
                                temp = True
                            else:
                                temp = True
                    except Exception as e:
                        return self.render(MANAGEMENT_DEVICE_BATCH_ADD_HTML,
                                           msg="tx_power为int类型请检查"
                                           )
            if temp:
                return self.redirect(MANAGEMENT_DEVICE_LIST_URL)

        return self.render(MANAGEMENT_DEVICE_BATCH_ADD_HTML,
                           msg="上传文件失败"
                           )

    @permission
    @backstage_authenticate
    def get(self):
        return self.render(MANAGEMENT_DEVICE_BATCH_ADD_HTML,
                           msg=""
                           )
