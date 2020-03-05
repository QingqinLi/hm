# coding=utf-8
class Game(object):
    # 类属性，存储历史最高分
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("帮助信息：XXXXXXXXXXXXXX")

    @classmethod
    def show_top_score(cls):
        print("历史最高分%d" % Game.top_score)

    def start_game(self):
        print("开始游戏吧%s" % self.player_name)


Game.show_help()
Game.show_top_score()
player1 = Game("小米")
player1.start_game()


