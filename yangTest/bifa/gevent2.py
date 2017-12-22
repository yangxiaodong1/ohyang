
import gevent
import time


def func1():
    print('\033[31;1m李闯在跟海涛搞...\033[0m')
    gevent.sleep(10)
    print('\033[31;1m李闯又回去跟继续跟海涛搞...\033[0m')


def func2():
    print('\033[32;1m李闯切换到了跟海龙搞...\033[0m')
    gevent.sleep(10)
    print('\033[32;1m李闯搞完了海涛，回来继续跟海龙搞...\033[0m')


time1 = time.time()
gevent.joinall([
    gevent.spawn(func1),
    gevent.spawn(func2),
])
time2 = time.time()
time3 = time2 - time1
print(time3)