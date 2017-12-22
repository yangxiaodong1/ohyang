from ohho.common.db.ohho.map.db_ohho_map_information import DBOHHOMapInformation
from Tools.ohho_operation import OHHOOperation
from Tools.ohho_datetime import OHHODatetime


class Map(object):
    def __init__(self):
        self.map = DBOHHOMapInformation()

    def get_degree(self, origin_latitude, origin_longitude, destination_latitude, destination_longitude):
        return OHHOOperation.get_degree(origin_latitude,
                                        origin_longitude,
                                        destination_latitude,
                                        destination_longitude)

    def get_near_map(self, user_id, delta_time=5 * 1000):
        timestamp = OHHODatetime.get_current_timestamp()
        timestamp = timestamp - delta_time
        query = self.map.filter_by_user(user_id)
        query = self.map.get_great_than_equal_timestamp(query, timestamp)
        query = self.map.order_by_id_desc(query)
        return query

    def get_the_greatest_map(self, query, timestamp):
        query = self.map.get_less_than_timestamp(query, timestamp)
        query = self.map.order_by_id_desc(query)
        return self.map.first(query)

    def get_the_least_map(self, query, timestamp):
        query = self.map.get_great_than_equal_timestamp(query, timestamp)
        query = self.map.order_by_id_asc(query)
        return self.map.first(query)

    def get_nearest_map(self, query, timestamp):
        greatest = self.get_the_greatest_map(query, timestamp)
        least = self.get_the_least_map(query, timestamp)
        if greatest and least:
            great_diff = abs(timestamp - greatest.timestamp)
            least_diff = abs(least.timestamp - timestamp)
            result = greatest if great_diff < least_diff else least
        else:
            result = greatest if greatest else least
        return result

    def get_orientation(self, angle):
        angle = angle % 360
        if angle == 0:
            return "north"
        elif 0 < angle < 90:
            return "northwest"
        elif angle == 90:
            return "west"
        elif 90 < angle < 180:
            return "southwest"
        elif angle == 180:
            return "south"
        elif 180 < angle < 270:
            return "southeast"
        elif angle == 270:
            return "east"
        elif 270 < angle < 360:
            return "northeast"

    def max_orientation(self, orientation_list):
        orientation_dict = dict()
        if orientation_list:
            for o in orientation_list:
                if orientation_dict.get(o, None) is None:
                    orientation_dict[o] = 1
                else:
                    orientation_dict[o] += 1

            orientation_dict_list = OHHOOperation.dict_sort_by_value(orientation_dict)
            if orientation_dict_list and len(orientation_dict_list) >= 2:
                if orientation_dict_list[0][1] == orientation_dict_list[1][1]:
                    orientation_dict = dict()
                    for o in orientation_list:
                        if len(o) < 6:
                            if orientation_dict.get(o, None) is None:
                                orientation_dict[o] = 1
                            else:
                                orientation_dict[o] += 1
                        else:
                            first = o[:5]
                            second = o[5:]
                            if orientation_dict.get(first, None) is None:
                                orientation_dict[first] = 1
                            else:
                                orientation_dict[first] += 1
                            if orientation_dict.get(second, None) is None:
                                orientation_dict[second] = 1
                            else:
                                orientation_dict[second] += 1
                    orientation_dict_list = OHHOOperation.dict_sort_by_value(orientation_dict)
                    if orientation_dict_list and len(orientation_dict_list) >= 2:
                        if orientation_dict_list[0][1] == orientation_dict_list[1][1]:
                            orientation_first = orientation_dict_list[0][0]
                            orientation_second = orientation_dict_list[1][0]
                            for o in orientation_list:
                                if orientation_first in o:
                                    return orientation_first
                                elif orientation_second in o:
                                    return orientation_second
                        else:
                            return orientation_dict_list[0][0]
                    else:
                        return None
                else:
                    return orientation_dict_list[0][0]
        else:
            return None

    def to_chinese(self, orientation):
        if orientation == "east":
            return "东"
        elif orientation == "west":
            return "西"
        elif orientation == "north":
            return "北"
        elif orientation == "south":
            return "南"
        elif orientation == "northeast":
            return "东北"
        elif orientation == "northwest":
            return "西北"
        elif orientation == "southeast":
            return "东南"
        elif orientation == "southwest":
            return "西南"
        else:
            return ""

    def main(self, user_id, friend_user_id):
        user_maps = self.get_near_map(user_id)
        friend_maps = self.get_near_map(friend_user_id)
        orientation_list = list()
        if user_maps:
            for m in user_maps:
                fm = self.get_nearest_map(friend_maps, m.timestamp)
                if fm:
                    degree = self.get_degree(m.latitude, m.longitude, fm.latitude, fm.longitude)
                    orientation_list.append(self.get_orientation(degree))
        return self.to_chinese(self.max_orientation(orientation_list))
