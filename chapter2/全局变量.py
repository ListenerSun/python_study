# 全局变量
num = 100


def num_count():
    # 代表引用的 全局变量
    global num
    num = 101
    # num = 101


def test2():
    print("test输出num: %s" % num)


if __name__ == "__main__":
    num_count()
    print(num)
    test2()
