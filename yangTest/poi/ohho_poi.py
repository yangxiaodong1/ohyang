from Tools.ohho_http import OHHOHttp
URL = "http://restapi.amap.com/v3/geocode/regeo"
# http: // restapi.amap.com / v3 / geocode / regeo?output = xml & location = 116.310003, 39.991957 & key = < 用户的key > & radius = 1000 & extensions = all

KEY = "039603ec0caccd709e889667a28905b1"


class OHHOPoi(object):
    @staticmethod
    def get_poi_by_longitude_and_latitude(longitude, latitude, poitype="", radius="1000", extensions="base", batch="false", roadlevel="0",output="JSON"):
        location = longitude + "," + latitude
        url = URL + "?key=" + KEY + "&location=" + location + "&radius=" + radius + "&extensions=" + extensions

        data = OHHOHttp.get(url)
        return data


if __name__ == '__main__':
    longitude = "116.481488"
    latitude = "39.990464"
    radius = "1000"
    extensions = "all"
    data = OHHOPoi.get_poi_by_longitude_and_latitude(longitude, latitude, radius, extensions)
    print(data)


