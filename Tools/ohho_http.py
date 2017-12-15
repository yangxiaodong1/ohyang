import requests


class OHHOHttp(object):
    @staticmethod
    def get(url):
        r = requests.get(url)
        return r.text

    @staticmethod
    def post(url, headers, data):
        s = requests.Session()
        s.headers.update(headers)
        r = s.post(url, data=data)
        return r.text

if __name__ == "__main__":
    import time
    import hashlib
    #
    # APPKEY[efec4cbb9a1c436545ec76261a06131c] < br / > Nonce[b0017e639bb54eaca7249ab9ca2b5eaf] < br / > CurTime[
    #     1500607467] < br / > CheckSum[31392
    # a8c3bce0d2e015eaae07b7980857b24ca28] < br / >
    appkey = "efec4cbb9a1c436545ec76261a06131c"
    appsecret = "d6cf63c8f5dc"
    nonce = "b0017e639bb54eaca7249ab9ca2b5eaf"
    current_time = str(int(time.time()))
    # current_time = "1500607467"
    sha1_string = appsecret + nonce + current_time
    print(sha1_string)
    # check_sum1 = "31392a8c3bce0d2e015eaae07b7980857b24ca28"
    check_sum = hashlib.sha1(sha1_string.encode("utf-8")).hexdigest()
    print(int(time.time()))
    # print(check_sum1)
    print(check_sum)
    url = "https://api.netease.im/nimserver/user/create.action"
    headers = {
        "APPKEY": appkey,
        "NONCE": nonce,
        "CurTime": current_time,
        "CheckSum": check_sum
    }
    data = {
        "accid": "lileliang",
    }
    print(OHHOHttp.post(url, headers, data))


