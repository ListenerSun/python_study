# 定义参数缺省值

# 缺省值参数 要放在末尾

def getSex(my_name, gender=True):
    """

    :param my_name: name
    :param gender:
    :return:
    """
    if my_name.startswith("L"):
        print(my_name)
    gender_text = "男"
    if not gender:
        gender_text = "女"
    return gender_text


name = "ListenerSun"
sex = getSex(name)
print("%s 的性别是 %s" % (name, sex))
print("==============定义多值参数===============")


# 一个 * 可以接受元组; 两个* 可以接收 字典
def moreParam(num, *name, **persons):
    """

    :param num:
    :param name:
    :param persons:
    :return:
    """
    print("num参数是 %s" % num)
    print(name)
    print(persons)


moreParam(1, "小明", "小红", age="Listener", height=1.72)


def getCount(*args):
    """
    计算多个数的和
    :param args:
    :return:
    """
    result = 0
    for num in args:
        result += num
    return result


print(getCount(1, 2, 3, 4))


print("==============拆包===============")

def up_package(*args1, **args2):

    print(args1)
    print(args2)


gl_name_list = ["Listener", "zyp", "chenlei"]
gl_person_dict = {
    "name": "txy",
    "age": 19,
    "height": 172
}
# 传参时  元组前加 *   字典前加 **
up_package(*gl_name_list, **gl_person_dict)


print("==============递归===============")

# 实现数字的累加

def numCount(num: int) -> int:
    if num == 1:
        return 1
    return num + numCount(num - 1)



print(numCount(10))