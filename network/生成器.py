
#  当一个函数中有yeild语句, 那么这个就不再是函数, 而是一个生成器的模板
def creat_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        yield  a
        a, b = b, a + b
        current_num += 1


# 如果在调用 creat_num 函数的时候, 发现这个函数中有yeild 语句，那么此时不是调用函数 而是创建一个生成器对象
# 返回的是 yeild 后面的值
obj = creat_num(10)
ret = next(obj)
print(ret)
ret2 = next(obj)
print(ret2)
print("==============")
for num in obj:
    print(num)