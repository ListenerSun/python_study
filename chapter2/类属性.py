
# 类属性 就是给 类对象 中定义的 属性
# 通常用来记录 与这个类相关的 特征
# 类属性 不会用于 记录 具体 对象的特征

class Tool(object):
    # 使用赋值语句 定义 类属性
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1



tool = Tool("车子")
book = Tool("房子")
print(Tool.count)