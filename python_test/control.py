__author__ = 'zenghuan'
import random
#
# a =2
# if a > 1:
#     print("大于1")
# elif a > 2:
#     print("dayu 2")
# else:
#     print("no")

big_num = 1000
name = "huanhuan"


# #计算1到100求和
# #加入分支结构实现1-100之间的偶数求和
def sum_hundred():
    x =0
    for i in range(2,101,2):
        # print(i)
         x = x+i
    print(x)


    # b=2
    # while b==1:print("yes")
    # else:print("no")
#sum_hundred()

'''
猜数字游戏
计算机给出一个1-100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示，大一点/小一点/猜对了
'''
def  guess_number():
    computer_number = random.randint(1,100)
    print("机器人给的数字是：",computer_number)

    while True:
        person_number = int(input("请输入一个数字："))
        if person_number > computer_number:
            print("小一点")
        elif person_number < computer_number:
            print("大一点")
        elif person_number == computer_number:
            print("猜对了")
            break

#guess_number()
























