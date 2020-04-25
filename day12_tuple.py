# 元组学习

tuple_name = ("张三", "里斯", "张三", "王五")

# 取值和索引
print(tuple_name[1])
print(tuple_name.index("王五"))

# 计算个数

print(tuple_name.count("张三"))

# 计算元组个数
print(len(tuple_name))
print("=============================")

# 格式化字符串 后面就是一个元组

tuple_info = ("小明", 18, 1.75)
print("%s 年龄是 %d 身高 %.2f" % tuple_info)

xiaoming_info = "%s 年龄是 %d 身高 %.2f" % tuple_info
print(xiaoming_info)

print("=============================")

# 列表和元组转换

list_info = list(tuple_info)
print(list_info)
list_to_tuple = tuple(list_info)
print(list_to_tuple)

