import os
import json
from math import radians, atan, tan, acos, cos, sin
from Tools.ohho_log import OHHOLog


class OHHOOperation(object):
    @staticmethod
    def get_current_directory_name(the_file):
        dir_path = os.path.dirname(the_file)
        return dir_path.split("/")[-1]

    @staticmethod
    def dict2json(obj_dict):
        if obj_dict:
            return json.dumps(obj_dict)
        return ""

    @staticmethod
    def json2dict(obj_string):
        if obj_string:
            return json.loads(obj_string)
        return dict()

    @staticmethod
    def json2list(obj_string):
        if obj_string:
            return json.loads(obj_string)
        return list()

    @staticmethod
    def dict_add_dict(dict1, dict2):
        if dict1 and isinstance(dict1, dict):
            result = dict1
            if dict2 and isinstance(dict2, dict):
                result.update(dict2)
        elif dict2 and isinstance(dict2, dict):
            result = dict2
        else:
            result = dict()
        return result

    @staticmethod
    def list_minus_list(list1, list2):
        if list1:
            if list2:
                return list(set(list1) - set(list2))
        return list1

    @staticmethod
    def set_intersect_set(set1, set2):
        return set1 & set2

    @staticmethod
    def set_union_set(set1, set2):
        return set1 | set2

    @staticmethod
    def calc_distance(Lat_A, Lng_A, Lat_B, Lng_B):
        '输入两点的经纬度计算两者距离'
        try:
            ra = 6378.140  # 赤道半径 (km)
            rb = 6356.755  # 极半径 (km)
            flatten = (ra - rb) / ra  # 地球扁率
            rad_lat_A = radians(Lat_A)
            rad_lng_A = radians(Lng_A)
            rad_lat_B = radians(Lat_B)
            rad_lng_B = radians(Lng_B)
            pA = atan(rb / ra * tan(rad_lat_A))
            pB = atan(rb / ra * tan(rad_lat_B))
            xx = acos(sin(pA) * sin(pB) + cos(pA) * cos(pB) * cos(rad_lng_A - rad_lng_B))
            c1 = (sin(xx) - xx) * (sin(pA) + sin(pB)) ** 2 / cos(xx / 2) ** 2
            c2 = (sin(xx) + xx) * (sin(pA) - sin(pB)) ** 2 / sin(xx / 2) ** 2
            dr = flatten / 8 * (c1 - c2)
            distance = ra * (xx + dr)
            return distance
        except Exception as ex:
            OHHOLog.print_log(ex)
            return -1

    # python3默认使用的是str类型对字符串编码，默认使用bytes操作二进制数据流，两者不能混淆！！
    # Python3有两种表示字符序列的类型：bytes和str。前者的实例包含原始的8位值，后者的实例包含Unicode字符。
    # str(unicode)类型是基准！要将str类型转化为bytes类型，使用encode()内置函数；反过来，使用decode()函数。

    @staticmethod
    def to_str(bytes_or_str):
        if isinstance(bytes_or_str, bytes):
            return bytes_or_str.decode("utf8")
        else:
            return bytes_or_str

    @staticmethod
    def to_bytes(bytes_or_str):
        if isinstance(bytes_or_str, str):
            return bytes_or_str.encode("utf8")
        else:
            return bytes_or_str

            # @staticmethod
            # def unicode2utf8(content_string):
            #     if isinstance(content_string, str):
            #         return content_string.encode("utf-8")
            #     return content_string
            #
            # @staticmethod
            # def utf82unicode(content_byte):
            #     if isinstance(content_byte, bytes):
            #         return content_byte.decode("utf-8")
            #     return content_byte


if __name__ == "__main__":
    a = "abc"
    print(type(a))
    b = OHHOOperation.to_bytes(a)
    print(b)
    print(type(b))
    c = OHHOOperation.to_str(b)
    print(c)
    print(type(c))
