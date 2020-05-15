# 线程学习
import threading
import time


def sing():
    for i in range(5):
        print("我在唱歌......")
        time.sleep(1)


def eat():
    for i in range(5):
        print("我在吃饭......")
        time.sleep(1)


if __name__ == '__main__':
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=eat)
    t1.start()
    t2.start()

    # 查看线程数量
    while True:
        thread_num = len(threading.enumerate()) 
        if thread_num <= 1:
            break 
        print(thread_num)
        time.sleep(1)
