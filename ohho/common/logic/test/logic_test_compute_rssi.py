from ohho.common.db.ohho.user.db_ohho_user import DBOHHOUser
from ohho.common.logic.common.result import Result
from ohho.common.db.test.db_test_rssi import DBTestRssi
from ohho.common.db.test.db_test_rssi_distance import DBTestRssiDistance
from Tools.ohho_log import OHHOLog


class LogicTestComputeRssi(object):
    def __init__(self):
        self.rssi = DBTestRssi()
        self.rssi_distance = DBTestRssiDistance()

    def get_less_than_two_second_sample(self, timestamp, type, phone_list=list()):
        """获取最近两秒，n1, n2 各个的所有样本对象"""
        rssi_query = self.rssi.get_query()
        rssi_query = self.rssi.between_timestamp_two_second(rssi_query, self.rssi.model.timestamp, timestamp)
        rssi_query = self.rssi.get_by_type(rssi_query, type)
        if phone_list:
            rssi_query = self.rssi.get_by_phone(rssi_query, phone_list)
        return rssi_query

    def get_less_than_one_second_sample(self, timestamp, type):
        """获取最近一秒，n1, n2 各个的所有样本对象"""
        rssi_query = self.rssi.get_query()
        rssi_query = self.rssi.between_timestamp_one_second(rssi_query, self.rssi.model.timestamp, timestamp)
        rssi_query = self.rssi.get_by_type(rssi_query, type)
        rssi_query = self.rssi.order_by_id_desc(rssi_query)
        return rssi_query

    def get_sample_list(self, timestamp, type=1):
        """获取两秒内的样本rssi的值"""
        sample_list = list()
        rssi_query = self.get_less_than_two_second_sample(timestamp, type)
        if rssi_query:
            sample_list = [rssi.rssi for rssi in rssi_query]
        return sample_list

    def get_rssi_max_min_avg(self, timestamp, type=1):
        """获取rssi最大值最小值平均值"""
        sample_list = self.get_sample_list(timestamp, type)
        list_length = len(sample_list)
        if list_length:
            d_max = int(max(sample_list))
            d_min = int(min(sample_list))
            d_sum = int(sum(sample_list))
            d_avg = d_sum / list_length
            return d_max, d_min, abs(d_avg)
        else:
            return None, None, None

    def get_middle_value(self, data_list):
        data_list = list(set(data_list))
        data_list = sorted(data_list)
        data_length = len(data_list)
        if data_length and data_length % 2 == 1:
            return True, data_list[data_length // 2], 0
        elif data_length:
            return False, data_list[data_length / 2 - 1], data_list[data_length / 2]
        else:
            return False, 0, 0

    def private_convert_rssi2distance(self, data):
        data = abs(data)
        subtrahend = 38.643
        # subtrahend = 34
        # subtrahend = 44.2900
        # subtrahend = 68.77
        # subtrahend = 50
        # divisor = 16.90558
        divisor = 20
        # divisor = 46
        # divisor = 30.1
        # subtrahend = 45 # 45 - 49
        # divisor = 32.5 # 32.5 - 45

        power = (data - subtrahend) / divisor
        print(power)
        from math import e
        # distance = pow(e, power)
        distance = pow(10, power)
        return distance

    def convert_rssi2distance(self, timestamp, type=1):
        """获取距离值"""
        data_list = self.get_sample_list(timestamp)
        is_middle, middle1, middle2 = self.get_middle_value(data_list)
        if is_middle:
            return self.private_convert_rssi2distance(middle1), 0
        elif middle1 and middle2:
            return self.private_convert_rssi2distance(middle1), self.private_convert_rssi2distance(middle2)
        else:
            return 0, 0
            # rssi_max, rssi_min, rssi_avg = self.get_rssi_max_min_avg(timestamp, type)
            # # OHHOLog.print_log("rssi")
            # # OHHOLog.print_log(rssi_max)
            # # OHHOLog.print_log(rssi_avg)
            # # OHHOLog.print_log(rssi_min)
            # if rssi_max is not None and rssi_min is not None and rssi_avg is not None:
            #     d_max = self.private_convert_rssi2distance(rssi_min)
            #     d_min = self.private_convert_rssi2distance(rssi_max)
            #     d_avg = self.private_convert_rssi2distance(rssi_avg)

            # OHHOLog.print_log("distance")
            # OHHOLog.print_log(d_max)
            # OHHOLog.print_log(d_avg)
            # OHHOLog.print_log(d_min)

            #     return d_max, d_min, d_avg
            # else:
            # return None, None, None

    def approach_reality(self, timestamp, type=1, before_data=None):
        """获取rssi值"""
        middle1, middle2 = self.convert_rssi2distance(timestamp, type)
        if middle1:
            if not middle2:
                return middle1
            else:
                if before_data:
                    if (abs(before_data - middle1) > abs(before_data - middle2)):
                        return middle2
                    else:
                        return middle1
                else:
                    return middle1
        else:
            return 0

            # distance_max, distance_min, distance_avg = self.convert_rssi2distance(timestamp, type)
            # if distance_max is not None and distance_min is not None and distance_avg is not None:
            #     distance = (distance_max + distance_min + 4 * distance_avg) / 6
            #
            #     OHHOLog.print_log("distance")
            #     OHHOLog.print_log(distance_max)
            #     OHHOLog.print_log(distance_avg)
            #     OHHOLog.print_log(distance_min)
            #     OHHOLog.print_log(distance)
            #     return distance
            # else:
            #     return None

    def get_last_three_rssi(self, timestamp, type=1):
        samples = self.get_less_than_one_second_sample(timestamp, type)
        samples = self.rssi.order_by_id_desc(samples)
        rssi_list = list()
        if samples:
            three_samples = samples[:3]
            rssi_list = [s.rssi for s in three_samples]
        return rssi_list

    def is_near_or_far(self, timestamp, type=1):
        """获得3绝对值"""
        last_three_rssi = self.get_last_three_rssi(timestamp, type)
        length = len(last_three_rssi)
        if length > 1:
            if length % 2 == 1:
                last_three_rssi = last_three_rssi[:-1]
            front = sum(last_three_rssi[:(length // 2)])
            back = sum(last_three_rssi[(length // 2):])

            minus = abs(front - back)
            return False, False
            if minus <= 2:
                return False, False
            else:
                if front > back:
                    return False, True
                else:
                    return True, False
        else:
            return False, False


            # if length < 3:
            #     OHHOLog.print_log("too short")
            #     return False, False
            # last_three_rssi_abs = [abs(rssi) for rssi in last_three_rssi]
            # max_value = max(last_three_rssi_abs)
            # min_value = min(last_three_rssi_abs)
            # if max_value == last_three_rssi_abs[2]:
            #     OHHOLog.print_log("near")
            #     return True, False
            # elif min_value == last_three_rssi_abs[2]:
            #     OHHOLog.print_log("far")
            #     return False, True
            # else:
            #     OHHOLog.print_log("source")
            #     return False, False

    def get_d1(self, timestamp, type=1):
        """获取最终的距离"""
        d_rssi = self.approach_reality(timestamp, type)
        if d_rssi is not None:
            is_near, is_far = self.is_near_or_far(timestamp, type)
            d1 = d_rssi
            if is_near:
                d1 -= 1
            elif is_far:
                d1 += 1
            return d1
        else:
            return None

    def add(self, timestamp, phone, distance):
        data = dict()
        if timestamp is None:
            return Result.result_failed("timestamp is None!")
        timestamp = float(timestamp)
        data["timestamp"] = timestamp

        if distance is None:
            return Result.result_failed("distance is None!")
        distance = float(distance)
        data["app_distance"] = distance

        server_distance = self.get_d1(timestamp)
        if server_distance is not None:
            data["server_distance"] = server_distance
        data["phone"] = phone

        success = self.rssi_distance.add(data)
        if success:
            return Result.result_success()
        else:
            return Result.result_failed()


if __name__ == "__main__":
    data = -51
    instance = LogicTestComputeRssi()
    print(instance.private_convert_rssi2distance(data))
