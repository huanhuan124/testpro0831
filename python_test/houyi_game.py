from python.game import Game_test

__author__ = 'zenghuan'


class HouYi(Game_test):
    #如果在子类中重新定义了__init__，那么父类的init会被覆盖
    def __init__(self,defense):
        super().__init__(1000,200)
        self.defense = defense

    def houyi_fight(self,enemy_hp,enemy_power):
        while True:
            self.hp = self.hp + self.defense - enemy_power
            enemy_hp = enemy_hp + self.defense - self.power
            print("我的最后血量{}：".format(self.hp))
            print("敌人的最后血量{}：".format(enemy_hp))
            if self.hp <= 0:
                print("我输了！")
                break
            elif enemy_hp <= 0:
                print("敌方输了！")
                break



defense = 100
houyi = HouYi(defense)
houyi.houyi_fight(1000,200)