#


def test(char, times):
    """ 打印一行字符

    @param char: 字符
    @param times: 次数
    """
    print(char * times)


# 函数2
def print_line(char, times):
    """
        打印多行字符
    @param char: 字符
    @param times: 次数
    """
    row = 0
    while row < 5:
        test(char, times)
        row += 1


print_line("*", 50)
