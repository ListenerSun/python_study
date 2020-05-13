# 如果两个模块方法名相同，后导入的会覆盖先导入的
# 1. 导入时先在  当前目录 导入，如果没有在搜索系统目录
# 2. 起名时 不要和 系统模块 重名
from 模块1 import say_hello
from 模块2 import say_hello as module2_say_hello
import random

say_hello()
module2_say_hello()
rand = random.randint(0, 10)
print(rand)