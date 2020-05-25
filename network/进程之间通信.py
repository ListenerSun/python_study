# 进程之间通信
import multiprocessing

def down_from_web(q):
    """
    从网络中下载数据
    :return:
    """
    data = [11, 22, 33, 44]
    for d in data:
        q.put(d)
    print("进程1从网络上下载了数据")

def analysis_data(q: multiprocessing.Queue):
    """
     分析数据
    :param q:
    :return:
    """
    print("进程2开始分析数据")
    while not q.empty():
        print(q.get())



def main():
    # 创建一个队列
    q = multiprocessing.Queue()
    # 创建两个进程
    p1 = multiprocessing.Process(target=down_from_web, args=(q,))
    p2 = multiprocessing.Process(target=analysis_data, args=(q,))
    p1.start()
    p2.start()



if __name__ == '__main__':
    main()