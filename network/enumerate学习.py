

# 1 遍历列表
#  index 是索引, person 是每个元组对象
persons = [(0, "sqt"), (1, "zyp"), (2, "wby")]
for index, person in enumerate(persons):
    print(index, person)
print("="*20)
# 指定 索引
for index, person in enumerate(persons, 2):
    print(index, person)

print("="*20)

# 正常遍历
for index, name in persons:
    print(index, name)