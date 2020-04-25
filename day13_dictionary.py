# 字典学习

# 字典不是一个有序的数据结构
sqt_info = {"name": "Listener",
            "age": 19,
            "heigth": 1.75,
            "weight": 75}

print(sqt_info)
print("======================")

# 取值
print(sqt_info["name"])

# add edit 如果 key不存在 程序运行会报错
sqt_info["name"] = "ListenerSun"
sqt_info["address"] = "河北省"
print(sqt_info)
# 删除
sqt_info.pop("name")
print(sqt_info)

print("======================")

# 合并字典
# 如果 另一个字典中的 key 重复 会覆盖
zyp_info = {"email": "1234@qq.com",
            "phone": "12344",
            "name": "parazhao"}
sqt_info.update(zyp_info)
print(sqt_info)

# 统计字典的 键值对 个数
print(len(sqt_info))
print("======================")

# for 便利字典

for item in sqt_info:
    print("%s - %s" % (item, sqt_info[item]))



