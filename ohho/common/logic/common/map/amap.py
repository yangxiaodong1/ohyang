from Tools.ohho_http import OHHOHttp
from Tools.ohho_operation import OHHOOperation

KEY = "d20ad2fde19d12bca74b7d50bb113a94"


class AMAP(object):
    @staticmethod
    def get(longitude, latitude):
        url = "http://restapi.amap.com/v3/geocode/regeo?" \
              "location=" + str(longitude) + "," + str(latitude) + \
              "&key=" + KEY + "&radius=1000&extensions=all"
        return OHHOHttp.get(url)

    @staticmethod
    def get_pois(response):
        if isinstance(response, str):
            response = OHHOOperation.json2dict(response)
        return response["regeocode"]["pois"]

    @staticmethod
    def get_nearest_poi_name(response):
        pois = AMAP.get_pois(response)
        pois_dict = dict()
        for item in pois:
            pois_dict[item["name"]] = item["distance"]
        pois_dict_list = OHHOOperation.dict_sort_by_value(pois_dict, reverse=False)
        return pois_dict_list[0][0] if pois_dict_list else ""

    @staticmethod
    def get_nearest_poi_name_interface(longitude, latitude):
        response = AMAP.get(longitude, latitude)
        return AMAP.get_nearest_poi_name(response)


if __name__ == "__main__":
    longitude = 116.481488
    latitude = 39.990464
    result = AMAP.get(longitude, latitude)
    response = OHHOOperation.json2dict(result)
    pois = response["regeocode"]["pois"]
    pois_dict = dict()
    for item in pois:
        print(item)
        # print(AMAP.get_nearest_poi_name(result))
