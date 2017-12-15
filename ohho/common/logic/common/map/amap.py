from Tools.ohho_http import OHHOHttp

KEY = "d20ad2fde19d12bca74b7d50bb113a94"


class AMAP(object):
    @staticmethod
    def get(longitude, latitude):
        url = "http://restapi.amap.com/v3/geocode/regeo?" \
              "location=" + str(longitude) + "," + str(latitude) + \
              "&key=" + KEY + "&radius=1000&extensions=all"
        return OHHOHttp.get(url)


if __name__ == "__main__":
    longitude = 116.481488
    latitude = 39.990464
    result = AMAP.get(longitude, latitude)
    import json

    result_dict = json.loads(result)
    print(result_dict)
    regeo_code = result_dict["regeocode"]
    print(regeo_code)
    pois = regeo_code["pois"]
    print(pois)
    poi = pois[0]
    for key, value in poi.items():
        print(key, end=":")
        print(value)

