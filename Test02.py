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
for year in range(2000, 2020):
    print('%s 年的生肖是 %s ' % (year, chinese_zodiac[year % 12]))
