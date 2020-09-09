__author__ = 'zenghuan'

from python_test import control
from python.control import *

def method(a,b=[]):
    b.append(a)
    #print(b)
    return b

print(method(2))
print(method(3))

# list = range(3,6)
# print(*list)
#
# y = lambda x:x+2
# print(y(12))

print(control.name)
print(control.big_num)
control.sum_hundred()

