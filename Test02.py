#   if语句
chinese_zodiac = '猴鸡狗猪鼠牛虎猫兔龙蛇马羊'
# year = int(input('请输入年份:'))
# if chinese_zodiac[year % 12] == '狗':
#     print('狗年好!')
# elif chinese_zodiac[year % 12] == '鸡':
#     print('鸡年好!')
# else:
#     print('既不是鸡年又不是狗年!')

#     for循环
# demo01
# for cz in chinese_zodiac:
#     print(cz)
# demo02 输出月份
# for i in range(1, 13):
#     print(i)
# demo03 根据年份计算生效 字符串代替
# for year in range(2000, 2020):
#     print('%s 年的生肖是 %s ' % (year, chinese_zodiac[year % 12]))

# while 循环

#  while 和 if 语句一起用
# num = 5
# while True:
#     num += 1
#     if num == 10:
#         # continue    #  跳过当前循环
#         break
#     print(num)
#  for语句和if语句一起用
zodiac_name = ('魔羯座', '水瓶座', '双鱼座', '白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23), (8, 23), (9, 23), (10, 23), (11, 23),
               (12, 23))

print((1, 20, 30) < (2, 1))
print(range(len(zodiac_days)))
for i in range(len(zodiac_days)):
    print(zodiac_days[i])
month = int(input('请输入月份:'))
day = int(input('请输入日期:'))
for zodiac_num in range(len(zodiac_days)):
    if zodiac_days[zodiac_num] >= (month, day):
        print(zodiac_name[zodiac_num])
        break
    elif month == 12 and day > 23:
        print(zodiac_name[0])
        break

