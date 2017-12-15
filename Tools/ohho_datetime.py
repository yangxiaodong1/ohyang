import time
import datetime

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
DATE_FORMAT = "%Y-%m-%d"


class OHHODatetime(object):
    @staticmethod
    def get_year(dt):
        return dt.year

    @staticmethod
    def get_current_timestamp():
        return int(time.time() * 1000)

    @staticmethod
    def get_current_timestamp_second():
        return int(time.time())

    @staticmethod
    def get_now():
        return datetime.datetime.now()

    @staticmethod
    def get_today_start():
        now_date_string = OHHODatetime.get_now_date_string()
        today_start_string = now_date_string + " 00:00:00"
        return OHHODatetime.string2clock(today_start_string)

    @staticmethod
    def get_date(dt):
        return dt.date()

    @staticmethod
    def get_now_string():
        now = OHHODatetime.get_now()
        return OHHODatetime.clock2string(now)

    @staticmethod
    def get_now_date_string():
        now = OHHODatetime.get_now()
        return OHHODatetime.clock2string(now, DATE_FORMAT)

    @staticmethod
    def get_utc_now():
        return datetime.datetime.utcnow()

    @staticmethod
    def get_some_time_after(dt, days, hours, minutes, seconds):
        time_delta = datetime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
        return dt + time_delta

    @staticmethod
    def get_some_hour_after(dt, hours):
        return OHHODatetime.get_some_time_after(dt, 0, hours, 0, 0)

    @staticmethod
    def beijing2utc(dt):
        negative_eight = datetime.timedelta(hours=-8)
        return dt + negative_eight

    @staticmethod
    def utc2beijing(dt):
        positive_eight = datetime.timedelta(hours=8)
        return dt + positive_eight

    @staticmethod
    def clock2string(dt, format=DATETIME_FORMAT):
        return dt.strftime(format)

    @staticmethod
    def date2string(dt):
        return OHHODatetime.clock2string(dt, DATE_FORMAT)

    @staticmethod
    def string2clock(dt_string):
        return datetime.datetime.strptime(dt_string, DATETIME_FORMAT)

    @staticmethod
    def string2date(dt_string):
        return datetime.datetime.strptime(dt_string, DATE_FORMAT)

    @staticmethod
    def utc2beijing(dt):
        return dt + datetime.timedelta(hours=8)

    @staticmethod
    def several_hours_before_from_now(hours=24):
        now = OHHODatetime.get_now()
        return now - datetime.timedelta(hours=hours)


if __name__ == "__main__":
    print(OHHODatetime.get_current_timestamp())
    now = OHHODatetime.get_now()
    print(now.year)
