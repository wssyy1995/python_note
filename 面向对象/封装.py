（1）封装概念
#广义上面向对象的封装：代码的保护，面向对象思想本身就是一种
#只让自己的对象能调用自己类中的方法

狭义上的封装 -- 面向对象的三大特性之一
#属性和方法都藏起来，不让你看见


（2）私有属性:变量前面加上双下划线


class Person:
    def __init__(self, name, pwd):
        self.name = name
        self.__pwd = pwd  # 私有属性

    def get_pwd(self):
        print(self.__dict__)
        return self.__pwd   #只要在类的内部使用私有属性，就会自动带上_类名



yayan=Person('yayan','wssyyyyqx1128')
print(yayan.__dict__)  #{'name': 'yayan', '_Person__pwd': 'wssyyyyqx1128'}
print(yayan._Person__pwd)  #通过使用_类型__属性名就可以调到这个属性
#print(yayan.__pwd) #会报错
print(yayan.get_pwd())  #不会报错，因为get_pwd不是私有方法，及时这个方法内部返回了私有属性




（3）私有方法：在方法前面加上双下划线
#私有方法

class Person:
    def __init__(self, name, pwd):
        self.name = name
        self.__pwd = pwd  # 私有属性

    def __pwd(self):
        print(self.__dict__)
        return self.__pwd   #只要在类的内部使用私有属性，就会自动带上_类名
    def getpwd(self):
        __pwd()
yayan=Person('yayan','wssyyyyqx1128')
print(yayan.__pwd())  #__pwd方法为私有方法，会报错


(4)父类的私有属性，子类无法调用
class Animal:
    def __init__(self,name,hp):
        self.mame = name
        self.hp = hp
    def __eat(self):
        print('animal eat medicine')
        self.hp+=100

class Dog(Animal):

    def eat2(self):
        print('dog eat medicine')
        self.hp+= 200

dog=Dog('suisui',100)
dog.__eat() #报错，__eat()是父类的私有方法
print(dog.hp)







