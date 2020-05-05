# 家具类

class HouseItem:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f" % (self.name, self.area)


# 房子类

class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        # 家具列表
        self.item_list = []

    def __str__(self):
        # Python 能够自动的将一对括号内部的代码连接在一起
        return ("户型：%s\n总面积：%.2f[剩余：%.2f]\n家具：%s"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))

    def add_item(self, item: HouseItem):
        if self.free_area < item.area:
            return "房子面积已经无法添加家具"
        self.item_list.append(item.name)
        self.free_area = self.free_area - item.area
        print("%s 添加成功" % item.name)


# 创建房子对象
my_house = House("两室一厅" , 75)
bed = HouseItem("席梦思", 4)
desk = HouseItem("桌子", 20)
my_house.add_item(bed)
my_house.add_item(desk)
print(my_house)
print(my_house.item_list)