
# 继承线程 重写 run() 方法

import threading
import time


class MyThread(threading.Thread):

    def run(self):
        for i in range(5):
            print("I am %s----%s" % (self.name, str(i)))
            time.sleep(0.5)


if __name__ == "__main__":

    for i in range(3):
        thread_num = len(threading.enumerate())
        print("当前线程的数量为: %s" % thread_num)
        t = MyThread()
        t.start()
    time.sleep(10)
    print("main 方法结束了:")
