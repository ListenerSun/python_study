# 字符串学习

str_temp = "hello Listener"

# 统计字符串长度
print(len(str_temp))
# 查找字符索引
print("ll字符的索引为: %d " % str_temp.index("ll"))
# 如果查找字符不在 字符串中  会报错
# print("sss字符的索引为: %d " % str_temp.index("sss"))
# 计算字符个数
print(" l 字符个数为: %s" % str_temp.count("l"))
# 遍历字符串
#
# for s in str_temp:
#     print(s)
print("============文本对齐=============")
# 文本对齐

# poems = ["静夜思",
#          "床前明月光",
#          "疑是地上霜",
#          "举头望明月",
#          "低头思故乡"]
#
# for poem in poems:
#     print("|%s|" % poem.center(10, " "))

print("==========去除空白字符===============")
# 去除空白字符

str_space = "hello world   "

print("|%s|" % str_space)
print("|%s|" % str_space.strip())

print("===========拆分字符串 合并字符串==============")
# 拆分字符串 合并字符串
str_temp2 = 'hello hello'
str_temp2_list = str_temp2.split("h")
print(str_temp2_list)
str_temp3 = "1"
print("join的字符串为:|%s|" % str_temp3.join(str_temp2_list))

print("===========字符切片  包头不包尾==============")
str_temp4 = "0123456789"

print("从2->5切割: %s" % str_temp4[2:6])
print("从6->9倒序切割: %s" % str_temp4[-4:])
print("字符串逆序: %s" % str_temp4[-1::-1])
print("索引从1开始每隔2个取一个: %s" % str_temp4[1::2])