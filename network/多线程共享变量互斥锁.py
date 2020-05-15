# 多线程计数 上锁案例
# 新建线程还可以 传参数

import threading,time
num = 0

def count1(count:int):
    global num
    for i in range(count):
        # 获取锁
        lock.acquire()
        num += 1
        # 释放锁
        lock.release()

lock = threading.Lock()
if __name__ == "__main__":
    t1 = threading.Thread(target=count1, args=(10000000,))
    t2 = threading.Thread(target=count1, args=(10000000,))
    t1.start()
    t2.start()
    time.sleep(30)
    print(num)
    pass