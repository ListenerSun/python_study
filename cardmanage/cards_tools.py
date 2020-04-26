
# 名片列表
card_list = []
# 显示欢迎界面
def showMenu():
    print("*" * 50)
    print("【欢迎使用名片管理系统】")
    print("1.显示名片")
    print("2.添加名片")
    print("3.删除名片")
    print("0.退出系统")
    print("*" * 50)

# 显示所有名片
def showAllCards():
    print("-" * 50)
    print("显示所有名片")
    for name in ["姓名", "电话", "QQ"]:
        print("%s" % name, end="\t\t\t")
    print("")
    print("=" * 50)
    for card_info in card_list:
        print("%s\t\t\t%s\t\t\t%s" % (card_info["name"], card_info["phone"], card_info["QQ"]))

# 添加名片
def addCard():
    print("-" * 50)
    name = input("请输入姓名")
    phone = input("请输入电话")
    QQ = input("请输入QQ")
    card_info = {
        "name":name,
        "phone": phone,
        "QQ": QQ
    }
    card_list.append(card_info)
    print("新增 %s 名片成功" % name)


# 删除名片
def delCard():
    print("-" * 50)
    print("删除名片")