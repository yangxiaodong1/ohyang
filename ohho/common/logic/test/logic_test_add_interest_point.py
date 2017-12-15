from Tools.ohho_operation import OHHOOperation
from ohho.common.db.test.db_test_interest_point import DBTestInterestPoint
from ohho.common.logic.common.result import Result
from Tools.ohho_log import OHHOLog
from Tools.ohho_datetime import OHHODatetime


class LogicTestAddInterestPoint(object):
    def __init__(self):
        self.interest = DBTestInterestPoint()

    def add(self, data):
        data_list = self.parse_parameters(data)
        if data_list:
            success = self.bulk_add(data_list)
            if success:
                return Result.result_success()
            else:
                return Result.result_failed("failed!")
        else:
            return Result.result_failed("no data")

    def bulk_add(self, dict_list):
        return self.interest.bulk_add(dict_list)

    def parse_parameters(self, data):
        """
        数据结构
        {
            "list": [
                {
                    "adCode": "110105",
                    "adName": "朝阳区",
                    "businessArea": "酒仙桥",
                    "cityCode": "010",
                    "distance": 32,
                    "img1": "http://store.is.autonavi.com/showpic/1c14d394cf5036a4418c92ec8d1bcbe7",
                    "img2": "http://store.is.autonavi.com/showpic/21122e8fcbca2e979b9089068b3a1c8e",
                    "img3": "http://store.is.autonavi.com/showpic/ce8c7fe35460bc58c4b37f59ff2b0812",
                    "poiId": "B0FFHVITFC",
                    "provinceCode": "110000",
                    "provinceName": "北京市",
                    "snippet": "酒仙桥路18号颐堤港LG层LG-12",
                    "tel": "010-64318399",
                    "title": "美希亚弁当(颐堤港)",
                    "typeCode": "050202",
                    "typeDes": "餐饮服务;外国餐厅;日本料理"
                },
                {
                    "adCode": "110105",
                    "adName": "朝阳区",
                    "businessArea": "酒仙桥",
                    "cityCode": "010",
                    "distance": 34,
                    "poiId": "B0FFI2DTOL",
                    "provinceCode": "110000",
                    "provinceName": "北京市",
                    "snippet": "颐堤港2层L273",
                    "tel": "",
                    "title": "弗萨塔可",
                    "typeCode": "050100",
                    "typeDes": "餐饮服务;中餐厅;中餐厅"
                }
            ],
            "name": "颐提港",
           "longitude": 116.490807
            "latitude": 39.97005
        }
        :param rssi_parameters:
        :return:
        """
        data_dict = OHHOOperation.json2dict(data)
        data = list()
        if data_dict:
            name = data_dict["name"]
            longitude = data_dict["longitude"]
            latitude = data_dict["latitude"]
            phone = data_dict["phone"]
            the_list = data_dict["list"]
            for d in the_list:
                temp = d
                temp["name"] = name
                temp["longitude"] = longitude
                temp["latitude"] = latitude
                temp["phone"] = phone
                temp["timestamp"] = OHHODatetime.get_current_timestamp()

                data.append(temp)

        return data
