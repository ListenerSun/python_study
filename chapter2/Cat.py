class Cat:

    def __init__(self, name):
        '''
            构造方法
        :param name:
        '''
        self.name = name

    def drink(self):
        print("%s 在喝水" % self.name)

    def eat(self):
        print("%s 在吃饭" % self.name)


tom = Cat("大懒猫")
tom.eat()
tom.drink()
