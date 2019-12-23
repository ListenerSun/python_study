#   if语句
chinese_zodiac = '鼠牛虎猫兔龙蛇马羊猴鸡狗猪'
year = int(input('请输入年份:'))
if chinese_zodiac[year % 12] == '狗':
    print('狗年好!')
elif chinese_zodiac[year % 12] == '鸡':
    print('鸡年好!')
else:
    print('既不是鸡年又不是狗年!')
