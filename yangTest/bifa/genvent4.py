
import gevent
# from gevent import monkey; monkey.patch_all()
import time

def func1(n):
    for i in range(3):
        print('\033[31;1m李闯在跟海涛搞...\033[0m')
        print(n)
        gevent.sleep(10)
        print('\033[31;1m李闯又回去跟继续跟海涛搞...\033[0m')
# def func1(n):
#     print('\033[31;1m李闯在跟海涛搞...\033[0m')
#     print(n)
#     gevent.sleep(10)
#     print('\033[31;1m李闯又回去跟继续跟海涛搞...\033[0m')


# def func2():
#     print('\033[32;1m李闯切换到了跟海龙搞...\033[0m')
#     gevent.sleep(1)
#     print('\033[32;1m李闯搞完了海涛，回来继续跟海龙搞...\033[0m')


time1 = time.time()
a = [gevent.spawn(func1, i) for i in range(3)]

gevent.joinall(a)

# gevent.joinall([
#     gevent.spawn(func1),
#     gevent.spawn(func1),
# ])

time2 = time.time() - time1
print(time2)