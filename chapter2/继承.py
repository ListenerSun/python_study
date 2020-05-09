# 继承学习

# 子类 不可以 访问父类的 私有方法 私有属性
# 子类 可以 通过父类的公共方法  访问 父类的 私有属性和方法

class Animal:


    def run(self):
        self.__haha()
        print("跑......")

    def eat(self):
        print("吃......")

    def __haha(self):
        print("haha 私有方法")

# 继承
class Dog(Animal):
    def bark(self):
        print("汪汪汪......")


dog = Dog()
dog.eat()


# 重写父类方法

class Cat(Animal):

    def run(self):
        super().run()
        print("猫在叫......")


cat = Cat()
cat.run()


