#  类方法 study
# 要用 @classmethod 修饰
#

class ClassMethod(object):

     count = 0

     @classmethod
     def class_method(cls):
         print("类的个数为 %d" % cls.count)

     def __init__(self):
         ClassMethod.count += 1

classmethod1 = ClassMethod()
classmethod2 = ClassMethod()
classmethod3 = ClassMethod()

# 调用类方法
ClassMethod.class_method()