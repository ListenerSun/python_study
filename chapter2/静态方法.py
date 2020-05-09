# static method 学习
# 定义静态方法 使用 @staticmethod  修饰
class Person(object):

    @staticmethod
    def walk():
        print("人会走路")


Person.walk()