__author__ = 'zenghuan'

"""
一个回合制游戏，每个角色都有hp和power
hp代表血量，power代表攻击力，hp初始值为1000，power初始值为200
定义一个fight方法
final_hp = hp - enemy_power
enemy_final_hp = enemy_hp - power
两个hp进行对比，血量剩余多的获胜

优化：将hp,power通过传参传入
第二个角色，叫后裔，继承了角色hp,power
houyi_hp = hp+defense-enemy_power


"""
class Game_test:
    def __init__(self,hp,power):
        self.hp = hp
        self.power =power


    def fight(self,enemy_hp,enemy_power):
        final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - self.power
        if final_hp > enemy_final_hp:
            print("我方胜！")
        elif final_hp == enemy_final_hp:
            print("平！")
        else:
            print("敌方胜！")


# class HouYi(Game_test):
#     #如果在子类中重新定义了__init__，那么父类的init会被覆盖
#     def __init__(self,defense):
#         super().__init__(1000,200)
#         self.defense = defense
#
#     def houyi_fight(self,enemy_hp,enemy_power):
#         final_hp = self.hp + self.defense - enemy_power
#         enemy_final_hp = enemy_hp + self.defense - self.power
#         if final_hp > enemy_final_hp:
#             print("我方胜！")
#         elif final_hp == enemy_final_hp:
#             print("平！")
#         else:
#             print("敌方胜！")


# hp = 1000
# power = 200
# g1 = Game_test(hp,power)
# g1.fight(800,100)

# defense = 100
# houyi = HouYi(defense)
# houyi.houyi_fight(800,100)


