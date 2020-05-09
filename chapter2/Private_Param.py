# 私有属性  方法

## 在属性前面 增加两个下划线  代表私有属性
# 私有属性在外部 不允许访问
# 其实并不存在 真正的 私有属性  私有方法
class Women:

    def __init__(self, name):
        self.name = name
        self.__age = 18

    def secret(self):
        print("%s 的年龄是 %s" % (self.name, self.__age))


my = Women("小红")
print(my.secret())

# 在外部调用私有属性
print(my._Women__age)
