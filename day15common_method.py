# 公共方法

print('1 < 2 结果: %s' % ("1" < "2"))
print('[1,1,1] < [2,2,2] 结果: %s' % ([1, 1, 1] < [2, 2, 2]))
print('[2, 2, 2] < [2,2,2] 结果: %s' % ([2, 2, 2] < [2, 2, 2]))

i = max(2, 3)
print("取 2 3 最大值 %d" % i)
print("=======元组切片==========")
tuple_name = ("listener", "sqt", "zyp", "wby", "cl", "txy")
print(tuple_name[1:3])

print("=======重复元素==========")

str_1 = "hello"
print("hello * 6 结果: %s" % (str_1 * 6))
list_1 = ["1", "2"]
list_2 = list_1 * 3
print("list_1*3 结果: %s" % list_2)

list_3 = ["1", "2"]
list_4 = ["3", "4"]
list_5 = list_3 + list_4
print('["1", "2"] + ["3", "4"] 结果为: %s ' % list_5)

print("=======in 和 not in==========")
str_2 = "abcde"
is_in = "a" in str_2
not_in = "a" not in str_2
print('"a" in str_2 : %s' % is_in)
print('"a" not in str_2 : %s' % not_in)

print("=======完整 for 循环==========")

#  如果 执行了 break else中的语句不会执行
#
for num in [1, 2, 3, 4]:
    print(num)
    if (num == 2):
        break
else:
    print("执行了 else")