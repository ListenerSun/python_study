
name_list = ["张三", "李四", "王五", "王五", "奥奥"]
num_list = [1, 3, 9, 5, 2, 10]
count = name_list.count("王五")
print("王五count %d %d" % (count,count))

# 升序
# 汉字升序按照字母排序
# name_list.sort()
# num_list.sort()

# 降序
# name_list.sort(reverse=True)
# num_list.sort(reverse=True)

# 反转
# name_list.reverse()
# num_list.reverse()
#
# print(name_list)
# print(num_list)

#迭代遍历
for name in name_list:
    print(name)
