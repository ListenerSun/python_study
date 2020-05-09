

#  定义方法 参考规则:
#  实例方法 --- 方法内部需要访问 实例属性
#       实例方法 内部可以使用  类名 访问类属性
#  类方法 --- 只需访问 类属性
#  静态方法 --- 方法内部不需要访问 实例属性 和 类属性
#  如果方法内部 急需要访问 实例属性 又要访问 类属性 ，则需要定义 实例方法
class Game(object):

    # 历史最高分
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("帮助信息: 游戏玩法规则")

    @classmethod
    def show_top_score(cls):
        print("历史记录最高分为: %d" % cls.top_score)

    def start_game(self):
        print("%s 玩家开始游戏了......" % self.player_name)

# 1. 查看游戏帮助信息
Game.show_help()
# 2. 查看历史最高分
Game.show_top_score()
# 3. 创建玩家
xiaoming = Game("小明")
# 4. 开始游戏
xiaoming.start_game()