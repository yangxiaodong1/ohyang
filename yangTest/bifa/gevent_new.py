#
# import gevent
#
#
# def func1():
#     print('\033[31;1m李闯在跟海涛搞...\033[0m')
#     gevent.sleep(2)
#     print('\033[31;1m李闯又回去跟继续跟海涛搞...\033[0m')
#
#
# def func2():
#     print('\033[32;1m李闯切换到了跟海龙搞...\033[0m')
#     gevent.sleep(1)
#     print('\033[32;1m李闯搞完了海涛，回来继续跟海龙搞...\033[0m')
#
#
# # gevent.joinall([
# #     gevent.spawn(func1),
# #     gevent.spawn(func2),
# #     # gevent.spawn(func3),
# # ])
#
# gevent.joinall([
#     gevent.spawn(func1),
#     gevent.spawn(func2),
# ])

from gevent import monkey; monkey.patch_socket()
import gevent

def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)

g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
g1.join()
g2.join()
g3.join()

