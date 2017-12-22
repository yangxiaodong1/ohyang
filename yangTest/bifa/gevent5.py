
import gevent
# from gevent import monkey; monkey.patch_all()
import time

# global k
k = 100
def func1(n):
    global k
    for i in range(3):
        print('\033[31;1m李闯在跟海涛搞...\033[0m')
        k += 1
        print("k")
        print(k)
        print(n)
        gevent.sleep(100)
        print('\033[31;1m李闯又回去跟继续跟海涛搞...\033[0m')


time1 = time.time()
a = [gevent.spawn(func1, i) for i in range(3)]

gevent.joinall(a)

time2 = time.time() - time1
print(time2)