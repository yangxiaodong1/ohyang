import random
import string
from time import *

from datetime import *
from Tools.ohho_random import OHHORandom
import json


class OhhoRandom(object):
    @staticmethod
    def get_cellphone(num):
        all_phone_nums = set()
        num_start = ['134', '135', '136', '137', '138', '139', '150', '151', '152', '158', '159', '157', '182', '187',
                     '188',
                     '147', '130', '131', '132', '155', '156', '185', '186', '133', '153', '180', '189']
        # for i in range(num):
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 8))
        res = start + end + '\n'
        all_phone_nums.add(res)

    @staticmethod
    def get_sex():
        sex_list = [1, 2, 3]
        sex = random.sample(sex_list, 1)
        return sex[0]

    @staticmethod
    def get_birthday():
        date1 = (2007, 1, 1, 0, 0, 0, -1, -1, -1)
        time1 = mktime(date1)
        date2 = (2017, 1, 1, 0, 0, 0, -1, -1, -1)
        time2 = mktime(date2)
        random_time = random.uniform(time1, time2)  # uniform返回随机实数 time1 <= time < time2
        random_time = date.fromtimestamp(random_time)
        return random_time

    @staticmethod
    def get_height():
        min_int = 100
        max_int = 300
        random_height = random.randint(min_int, max_int)
        return random_height

    @staticmethod
    def get_hometown():
        return 1

    @staticmethod
    def get_school():
        return 1

    @staticmethod
    def get_company():
        return 1

    @staticmethod
    def get_degree_id():
        return 1

    @staticmethod
    def get_favourite_live_city():
        city_list = ["北京", "上海", "广州", "深圳", "天津", "南京", "武汉", "沈阳", "西安", "成都", "重庆", "杭州", "青岛", "大连", "宁波", "济南", "哈尔滨", "长春", "厦门", "郑州",
                     "长沙", "兰州", "苏州", "无锡", "南昌", "贵阳", "南宁", "合肥", "太原", "石家庄", "呼和浩特", "佛山"]
        random_city = random.choice(city_list)
        return random_city

    @staticmethod
    def get_occupation_id():
        return 1

    @staticmethod
    def get_position_id():
        return 1

    @staticmethod
    def get_match_condition_id():
        return 1

    @staticmethod
    def get_cellphone_id():
        return 1

    @staticmethod
    def get_type():
        return 1

    @staticmethod
    def get_first():
        return 1

    @staticmethod
    def get_second():
        return 1

    @staticmethod
    def get_third():
        return 1

    # @staticmethod
    # def get_isbn():
    #     return 1
    #
    # @staticmethod
    # def get_name():
    #     return 1
    #
    # @staticmethod
    # def get_description():
    #     return 1
    #
    # @staticmethod
    # def get_index():
    #     return 1
    #
    # @staticmethod
    # def get_icon():
    #     return 1
    #
    # @staticmethod
    # def get_auther():
    #     return 1
    #
    # @staticmethod
    # def get_url():
    #     return 1
    @staticmethod
    def get_favourite_book():
        obj = dict()
        return obj

    @staticmethod
    def get_favourite_movie():
        obj = dict()
        return obj

    @staticmethod
    def get_favourite_music():
        obj = dict()
        return obj

    @staticmethod
    def get_favourite_sport():
        obj = dict()
        return obj

    @staticmethod
    def get_user_icon():
        obj = dict()
        return obj

    @staticmethod
    def get_user_impression():
        obj = dict()
        return obj

    @staticmethod
    def get_user_interest():
        a = {"music": [77, 78, 79, 80, 81, 82], "profession_id": [307], "food": [139, 140, 141, 142, 143],
             "work_domain_id": [345], "movie": [60, 61, 62, 63, 64], "smoke_id": [447],
             "sport": [225, 226, 227, 228, 229, 230], "book": [43, 44, 45, 46, 47], "drink_id": [450],
             "travel": [172, 173, 174, 175, 176]}
        b = {"work_domain_id": [346], "movie": [60, 61], "music": [77, 78], "sport": [225, 226], "food": [139, 140],
             "book": [43, 44], "travel": [172, 173]}
        c = {"work_domain_id": [346], "movie": [60, 61], "music": [77, 78], "sport": [225, 226], "food": [139, 140],
             "book": [43, 44], "travel": [172, 173]}
        d = {"music": [77, 78], "food": [139, 140], "movie": [60, 61], "smoke_id": [447], "sport": [225, 226],
             "book": [43, 44], "drink_id": [450], "travel": [172, 173]}
        e = {"movie": [61, 62, 63, 65, 66, 68, 69, 71, 72, 74], "smoke_id": [448],
             "music": [77, 79, 81, 88, 89, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100, 101, 102, 103, 104, 105, 107, 108,
                       109, 110, 111, 112, 113, 114, 115, 116, 117],
             "sport": [225, 226, 233, 234, 235, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 250, 251, 252, 255,
                       257, 258, 261],
             "food": [139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157,
                      158, 159], "book": [43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54],
             "travel": [172, 173, 175, 180, 181, 184, 185, 187, 188, 190, 194, 195, 196, 197, 198, 199, 200, 201, 202,
                        203]}

        temp_data = [a, b, c, d, e]
        random_data = random.sample(temp_data, 1)
        random_data = json.dumps(random_data[0])

        return random_data

    @staticmethod
    def get_user_match_interest():
        a1 = [77, 78, 79, 80, 81, 82, 307, 77, 78, 172, 173, 60, 61, 225, 226, 139, 140, 77, 79, 81, 88, 89, 90, 91, 92,
              93]
        a2 = random.randint(1, 10)
        interest_data = random.sample(a1, a2)
        return str(interest_data)

    @staticmethod
    def get_imei():
        random_imei = OHHORandom.get_nonce(15)
        return random_imei


if __name__ == '__main__':
    birthday = OhhoRandom.get_birthday()
    print(birthday)
    # aa = OhhoRandom.get_user_match_interest()
    # bb = OhhoRandom.get_height()
    # print(bb)
