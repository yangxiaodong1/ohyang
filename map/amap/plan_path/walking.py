from Tools.ohho_http import OHHOHttp
from map.amap.constant import KEY, WALKING_URL
from Tools.ohho_operation import OHHOOperation


class Walking(object):
    @staticmethod
    def get(origin, destination, sig=None, output="JSON", callback=None):
        origin_string = str(origin[0]) + "," + str(origin[1])
        destination_string = str(destination[0]) + "," + str(destination[1])
        url = WALKING_URL + "?key=" + KEY + "&origin=" \
              + origin_string + "&destination=" + \
              destination_string
        if sig:
            url += "&sig=" + sig
        if output:
            url += "&output=" + output

        if callback:
            url += "&callback=" + callback
        return OHHOHttp.get(url)


if __name__ == "__main__":
    origin = (117.500244, 40.417801)
    destination = (117.400244, 40.317801)
    print(OHHOOperation.get_degree(origin[1], origin[0], destination[1], destination[0]))

    the_dict = OHHOOperation.json2dict(Walking.get(origin, destination))
    route = the_dict["route"]
    paths = route["paths"]
    steps = paths[0]["steps"]
    # orientation = steps["orientation"]
    result = steps
    print(len(steps))
    for i in range(len(steps)):
        print(steps[i])
    print(steps)
