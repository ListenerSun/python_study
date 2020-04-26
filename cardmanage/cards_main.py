import cards_tools
# 名片管理系统程序主入口

while True:
    cards_tools.showMenu()
    action_str = input("请执行您的操作:")
    print("您执行的操作为【%s】" % action_str)

    if action_str in ["1", "2", "3"]:
        if action_str == "1":
            cards_tools.showAllCards()
        elif action_str == "2":
            cards_tools.addCard()
        elif action_str == "3":
            cards_tools.delCard()
        pass
    elif action_str == "0":
        print("名片管理系统结束")
        break;
    else:
        print("您输入的选项不正确!请重新输入")
