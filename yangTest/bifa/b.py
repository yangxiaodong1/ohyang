import gevent
import time

def sleep_fun():
    for i in range(2):
        print("hao")
        time.sleep(2)
def aa():
    time1 = time.time()
    for i in range(10):
        gevent.spawn(sleep_fun).join()
    time2 = time.time()
    time3 = time2 - time1
    print(time3)
aa()
# def sleep_fun():
#     print("hao")
#     for i in range(2):
#         time.sleep(2)
#
# time1 = time.time()
# gevent.joinall([
#     gevent.spawn(sleep_fun),
#     gevent.spawn(sleep_fun),
#     gevent.spawn(sleep_fun),
#     gevent.spawn(sleep_fun),
#     gevent.spawn(sleep_fun),
#     gevent.spawn(sleep_fun),
# ])
# time2 = time.time()
# time3 = time2 - time1
# print(time3)