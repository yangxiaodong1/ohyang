from ohho.common.view.common.parameters import Get
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.logic.common.device import Device
from tornado.web import authenticated
from math import ceil
from ohho.common.view.common.pagination import Pagination
from ohho.common.view.backstage.constant import *
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate

class BackstageDeviceListHandler(BaseHandler):
    def post(self):
        pass

    @permission
    @backstage_authenticate
    def get(self):
        the_get = Get()
        identity_id = the_get.get_device_identity_id(self)
        if identity_id is None:
            identity_id = ""
        mac_address = the_get.get_device_mac_address(self)
        if mac_address is None:
            mac_address = ""
        page = the_get.get_page(self)
        data_count_per_page = the_get.get_data_count_per_page(self)
        page_count_per_page = the_get.get_page_count_per_page(self)
        offset = (page - 1) * data_count_per_page
        limit = data_count_per_page

        instance = Device()
        query = instance.get_all_device()

        if identity_id:
            instance.set_identity(identity_id)
            query = instance.find_by_identity(query)

        if mac_address:
            instance.set_mac_address(mac_address)
            query = instance.find_by_mac_address(query)

        devices, count = instance.get_some_devices(query, offset, limit)
        total_page = int(ceil(count / data_count_per_page))
        pagination = Pagination(total_page, page, data_count_per_page, page_count_per_page)
        page_list, previous, next = pagination.get_page_list_of_this_page()

        # return self.render("backstage/management/device_list.html",
        return self.render(MANAGEMENT_DEVICE_LIST_HTML,
                           devices=devices,
                           pages=page_list,
                           previous=previous,
                           next=next,
                           page=page,
                           identity_id=identity_id,
                           mac_address=mac_address,
                           detail_url=MANAGEMENT_DEVICE_DETAIL_URL,
                           delete_url=MANAGEMENT_DEVICE_DELETE_URL,
                           )
