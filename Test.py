# # 定义一个字符串
#
# # content = '你好啊'
# # print(content[0:5])
# # s = str(123)
# # print(s);
# # 定义生肖，根据年份记录生效
# chinese_zodiac = '鼠牛虎猫兔龙蛇马羊猴鸡狗猪'
# year = 2019
# index = (year % 12)
# print(chinese_zodiac[index])
# # 字符串的操作
# print('狗' in chinese_zodiac)
# print('狗' not in chinese_zodiac)
# # 重复字符串
# print(chinese_zodiac * 3)
# # 字符串相加
# print(chinese_zodiac + '哈哈')
#
#  filter
a = (1, 3, 6, 8, 9)
b = 4
print(list(filter(lambda x: x < b, a)))  # 取出小于 4 的元素

# 根据日期计算星座
zodiac_name = ('魔羯座', '水瓶座', '双鱼座', '白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座')
zodiac_days = {(1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23), (8, 23), (9, 23), (10, 23), (11, 23),
               (12, 23)}
(month, day) = (2, 15)  # 某个日期
zodiac_day = filter(lambda x: x <= (month, day), zodiac_days)
# print(list(zodiac_day))
index = len(list(zodiac_day)) % 12
print(zodiac_name[index])

# 定义链表
temp_list = ['abc', 'xyz', 'asd']
temp_list.append('qqq')  # 添加一个元素
print(temp_list)
temp_list.remove('abc')