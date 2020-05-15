# 多线程计数 线程不安全 案例
# 新建线程还可以 传参数

import threading,time
num = 0

def count1(count:int):
    global num
    for i in range(count):
        num += 1

if __name__ == "__main__":
    t1 = threading.Thread(target=count1, args=(200000,))
    t2 = threading.Thread(target=count1, args=(200000,))
    t1.start()
    t2.start()
    time.sleep(5)
    print(num)
    pass