# 定义一个字符串

# content = '你好啊'
# print(content[0:5])
# s = str(123)
# print(s);
# 定义生肖，根据年份记录生效
chinese_zodiac = '鼠牛虎猫兔龙蛇马羊猴鸡狗猪'
year = 2019
index = (year % 12)
print(chinese_zodiac[index])
# 字符串的操作
print('狗' in chinese_zodiac)
print('狗' not in chinese_zodiac)
# 重复字符串
print(chinese_zodiac * 3)
# 字符串相加
print(chinese_zodiac + '哈哈')
