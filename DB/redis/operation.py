import redis
import json
from Tools.ohho_operation import OHHOOperation

# # redis cluster start
# from rediscluster import StrictRedisCluster
#
# redis_nodes = [
#     {'host': 'localhost', 'port': 6378},
#     {'host': 'localhost', 'port': 6379},
#     {'host': 'localhost', 'port': 6380},
#     {'host': 'localhost', 'port': 6381},
# ]
#
# r = StrictRedisCluster(startup_nodes=redis_nodes)
#
# # redis cluster end

r = redis.Redis(host='localhost', port=6379)
DEFAULT_EXPIRE = 20 * 60


class RedisDB(object):
    #  hash
    @staticmethod
    def hash_set(name, key, value):
        return r.hset(name, key, value)

    @staticmethod
    def hash_get(name, key):
        return r.hget(name, key)

    @staticmethod
    def data2dict(data):
        try:
            value = OHHOOperation.to_str(data)
            value = value.replace("\'", "\"")
            value_dict = json.loads(value)
            return value_dict
        except Exception as ex:
            return dict()

    @staticmethod
    def hash_del(name, key):
        return r.hdel(name, key)

    @staticmethod
    def get_all_key(name):
        return r.hgetall(name)

    @staticmethod
    def hash_multi_set(name, key_value_dict):
        return r.hmset(name, key_value_dict)

    @staticmethod
    def hash_exist(name, key):
        return r.hexists(name, key)

    @staticmethod
    def hash_delete(name, key):
        return r.hdel(name, key)

    # set
    @staticmethod
    def set_add(name, value):
        return r.sadd(name, value)

    @staticmethod
    def set_is_member(name, value):
        return r.sismember(name, value)

    @staticmethod
    def set_expire(name, interval=DEFAULT_EXPIRE):
        return r.expire(name, interval)

    # list
    @staticmethod
    def list_left_push(name, value):
        return r.lpush(name, value)

    @staticmethod
    def list_right_pop(name):
        return r.rpop(name)

    @staticmethod
    def list_length(name):
        return r.llen(name)

    @staticmethod
    def list_get_all(name):
        result = list()
        length = RedisDB.list_length(name)
        for i in range(length):
            result.append(RedisDB.list_right_pop(name))
        return result

    # geo
    @staticmethod
    def geo_add(name, *values):
        return r.geoadd(name, *values)

    @staticmethod
    def geo_hash(name, *values):
        return r.geohash(name, *values)

    @staticmethod
    def geo_distance(name, place1, place2, unit):
        return r.geodist(name, place1, place2, unit)

    @staticmethod
    def geo_position(name, *values):
        return r.geopos(name, *values)

    @staticmethod
    def geo_radius(name, longitude, latitude, radius, unit=None,
                   withdist=False, withcoord=False, withhash=False, count=None,
                   sort=None, store=None, store_dist=None):
        return r.georadius(name, longitude, latitude, radius,
                           unit=unit, withdist=withdist,
                           withcoord=withcoord, withhash=withhash,
                           count=count, sort=sort, store=store,
                           store_dist=store_dist)

    @staticmethod
    def geo_radius_by_member(name, member, radius, unit=None,
                             withdist=False, withcoord=False, withhash=False,
                             count=None, sort=None, store=None, store_dist=None):
        return r.georadiusbymember(name, member, radius, unit=unit,
                                   withdist=withdist, withcoord=withcoord,
                                   withhash=withhash, count=count,
                                   sort=sort, store=store,
                                   store_dist=store_dist)

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


if __name__ == "__main__":
    # name = "test"
    # key = "count"
    # RedisDB.hash_set(name, key, 1)
    # print(RedisDB.hash_get(name, key))
    # RedisDB.hash_del(name, key)
    # print(RedisDB.hash_get(name, key))
    #
    # list_name = "user_id_1"
    # RedisDB.list_left_push(list_name, "1,10")
    # RedisDB.list_left_push(list_name, (2, 11))
    # RedisDB.list_left_push(list_name, (3, 12))
    # print(RedisDB.list_length(list_name))
    # data = RedisDB.list_get_all(list_name)
    # print(RedisDB.to_bytes(data[0]))
    name = "position"
    longitude = 116.37
    latitude = 37.116
    city_name = "beijing"
    RedisDB.geo_add(name, longitude, latitude, city_name)
    print(RedisDB.geo_hash(name, city_name))
    position = RedisDB.geo_position(name, city_name)
    print(type(position))
    print(position[0][0])

    nearby = RedisDB.geo_radius(name, longitude, latitude, 2, unit="km", withcoord=True)
    print(type(nearby))
    print(nearby)

    # test = {"name": "lileliang", "longitude": 117.234324, "latitude": 37.823233, "floor": 1}
    # RedisDB.hash_set("test", "abc", test)
    # data = RedisDB.hash_get("test", "abc")
    # data_dict = RedisDB.data2dict(data)
    # print(data)
    # print(data_dict)
    # print(type(data_dict["name"]))
    # print(data_dict["name"])
    # print(type(data_dict["longitude"]))
    # print(data_dict["longitude"])
    # print(type(data_dict["latitude"]))
    # print(data_dict["latitude"])
    # print(type(data_dict["floor"]))
    # print(data_dict["floor"])
