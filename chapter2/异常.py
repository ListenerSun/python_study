# 异常 study
def input_passwd():
    pwd = input("请输入密码:")
    if len(pwd) >= 8:
        print("你输入的密码为: %s" % pwd)
    else:
        # 抛出异常
        ex = Exception("密码长度小于 8 位")
        raise ex

try:
    input_passwd()
except Exception as result:
    print("出异常了: %s" % result)