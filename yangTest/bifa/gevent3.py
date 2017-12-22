
import gevent
from gevent import monkey; monkey.patch_socket()
import time

def func1(n):
    print('\033[31;1m李闯在跟海涛搞...\033[0m')
    gevent.sleep(1)
    print(n)
    # time.sleep(10)
    print('\033[31;1m李闯又回去跟继续跟海涛搞...\033[0m')


time1 = time.time()
gevent.joinall([
    gevent.spawn(func1, 1),
    gevent.spawn(func1, 1),
    gevent.spawn(func1, 1),
])
time2 = time.time()
time3 = time2 - time1
print(time3)

# def func1(n):
#     print('\033[31;1m李闯在跟海涛搞...\033[0m')
#     gevent.sleep(10)
#     print(n)
#     # time.sleep(10)
#     print('\033[31;1m李闯又回去跟继续跟海涛搞...\033[0m')
#
#
# time1 = time.time()
#
# a = [gevent.spawn(func1(i)) for i in range(3)]
# gevent.joinall(a)
# # gevent.joinall([
# #     gevent.spawn(func1),
# #     gevent.spawn(func1),
# # ])
# time2 = time.time()
# time3 = time2 - time1
# print(time3)