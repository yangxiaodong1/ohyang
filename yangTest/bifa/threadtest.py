
import threading
import time


def target():
    print("start")
    time.sleep(5)
    print("end")

time1 = time.time()
t = threading.Thread(target=target)
t2 = threading.Thread(target=target)
t.start()
t2.start()
time2 = time.time()
time3 = time2 - time1
# t.join()
# t2.join()
print(time3)
# t.join()
print(threading.current_thread().name)

# def target():
#     print("start")
#     time.sleep(5)
#     print("end")
#
# time1 = time.time()
# t = threading.Thread(target=target)
# t2 = threading.Thread(target=target)
# t.start()
# t2.start()
# time2 = time.time()
# time3 = time2 - time1
# # t.join()
# # t2.join()
# print(time3)
# # t.join()
# print(threading.current_thread().name)


