# 多继承

# 1.如果 两个父类有 同名的 属性和方法  应该避免多继承
class A:

    def a(self):
        print("A的 a 方法")

class B:

    def b(self):
        print("B的 b 方法")

class C(A,B):

    def c(self):
        pass

c = C()
c.a()
c.b()