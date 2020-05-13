#  单例模式 study
class Player(object):
    instance = None

    # 重写 _new_ 方法
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

player1 = Player()
player2 = Player()
print(player1)
print(player2)