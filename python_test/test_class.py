__author__ = 'zenghuan'

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age= age
    gender = "male"

    def run(self):
        print("name:%s,age:%d"%(self.name,self.age))


xiaoming = Person("xiaoming",20)

xiaoming.name = "xiaoming2"
xiaoming.run()
xiaoming.gender = "female"
print(xiaoming.gender)
print(xiaoming.name)

