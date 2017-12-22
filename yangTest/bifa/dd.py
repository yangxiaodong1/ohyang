import threading
import time


def threadFunc(num):
    global total, mutex

    # 打印线程名

    for x in range(0, int(num)):
        # 取得锁
        mutex.acquire()
        total = total + 1
        print(total)
        time.sleep(2)
        # 释放锁
        mutex.release()


def main(num):
    # 定义全局变量
    global total, mutex
    total = 0
    # 创建锁
    mutex = threading.Lock()

    # 定义线程池
    threads = []
    # 先创建线程对象
    for x in range(0, num):
        threads.append(threading.Thread(target=threadFunc, args=(10,)))
        # 启动所有线程
    t1 = time.time()
    for t in threads:
        t.setDaemon(True)
        t.start()
        t.join()
        # 主线程中等待所有子线程退出



    # for t in threads:
    #     t.join()
    t2 = time.time()
    t3 = t2 - t1
        # 打印执行结果
    print(total)
    print(t3)



if __name__ == '__main__':
    # 创建40个线程
    main(4)

