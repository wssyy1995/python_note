一.property
#内置装饰器函数，只在面向对象中使用


from math import pi
class circle:
    def __init__(self,r):
        self.r=r

    @property
    def area(self):
        return pi*(self.r**2)

    @property
    def perimeter(self):
        return 2*pi*self.r

c1=Circle(5)
#print(c1.area()) #area和perimeter其实更像是一个属性，可以在这个方法上伪装成属性 @property

print(c1.area) #伪装成属性后，调用不需要再加括号


#property的应用（查看）
class Goods:
    discount=0.5
    def __init__(self,name,price):
        self.name=name
        self.__price=price

    @property
    def price(self):
        return self.__price * Goods.discount


apple=Goods('苹果',5)
print(apple.price)  #将原价price私有化，price方法伪装成属性，并且每次discount更改之后，调用的price也会随之更改


#property的应用（删除，修改）

class Person:
    def __init__(self,name):
        self.__name=name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,new_name):
        self.__name=new_name


    @name.deleter  #(.前面的名字必须与property装饰的方法名字一样)
    def name(self):
        del self.__name

yayan=Person('yayan')
print(yayan.name)
yayan.name='yayansb' #执行了name.setter
print()
del yayan.name    #执行了name.deleter的方法
print()


二.method方法

#classmethod  类方法
例子：
class Goods:
    __discount = 0.5

    def __init__(self, name, price):
        self.name = name
        self.__price = price

    @property
    def price(self):
        return self.__price * Goods.__discount

    # 想要一个方法来更新类的静态属性，但是这个方法希望是类的方法,不需要实例化对象了
    @classmethod   #当这个方法的操作只涉及静态属性的时候，就用classmethod来装饰这个方法
    def change_discount(cls, new_discount):
        cls.__discount = new_discount


Goods.change_discount(0.8)   #
apple = Goods('apple',100)
print(apple.price)


#staticmathod 静态的方法：在一个类里，如果这个不需要静态变量，也不需要实例化，就用staticmethod改成静态方法，静态方法没有默认参数（self,cls）
调用方式：类名.方法（）

#静态方法和类方法都是类调用的，对象名也可以调用，但是推荐用类名调用




三.反射：hasattr,getattr,setattr,delattr
#放射就是用字符串类型的名字去操作变量

例子：


class Teather:
    dic={'查看老师':'show_teather','查看学生':'show_student'}
    number=2
    def show_teather(self):
        print('teather is guangjign')

    def show_student(self):
        print('student is yayan')

    @staticmethod
    def stafunc():
        print('this is a staticmethod')

    @classmethod
    def clsfunc(cls):
        print('this is a class func,number is :',cls.number)

if hasattr(Teather,'dic'):
    ret=getattr(Teather,'dic')
    print(ret)
else:
    print('这个类里没有dic为变量名的属性或方法')

#getattr调用类的静态方法
sfunc=getattr(Teather,'stafunc')
sfunc()
#getattr调用类的类方法
cfunc=getattr(Teather,'clsfunc')
cfunc()

#getattr调用类的普通方法，所以需要实例化后，用对象名传入getattr
wang=Teather()
ss=getattr(wang,'show_student')
ss()    #调用这个方法不需要再加上前缀

#getattr调用

#getattr也可以反射当前模块中的变量或方法
import sys
i=18
def func():
    print('this is a function')
print(getattr(sys.modules['__main__'],'i'))
getattr(sys.modules['__main__'],'func')()

#但是，你这个模块可能被别的模块导入，所以应该将__main__改成__main__


#反射的应用：让用户输入需要查询的内容
for k in Teather.dic:
    print(k)

key=input('请输入需求:')
Teather.dic[key]
userinput_func=getattr(wang,Teather.dic[key])
userinput_func()

#双下方法
四.__str__,__repr__,__del__,__call__

str(obj) = obj.__str__

repr(obj) = obj.__repr__

class A:

    def __str__(self):
        return 'A is object'

    def __repr__(self):
        return str(self.__dict__)

    def __del__(self):   #析构函数:在删除一个对象之前，进行一些收尾工作
        print('执行了__del__')

    def __call__(self):
        print('执行了__call__')


a=A()
print(a)   #每当打印一个对象的时候，就是调用a.__str__ ,如果类里没有__str__方法，就会返回内存地址
print('%s'%(a)) %s相当于调用这个类的__str__里的返回值
print('%r'%(a)) %r相当于调用这个类的__repr__里的返回值
 #__repr__是__str__的备胎，当没有__str__，就会调用__repr__的返回

del a  #del先执行了__del__这个方法，又删除了变量
       #python解释器也会自动删除这个变量

a()  #对象加上括号，相当于调用这个__call__方法



五.item系列： __getitem__ , __setitem__,__delitem__

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __getitem__(self, item):
        if hasattr(self,item):    #这个self对象里，有没有name 这个变量
            return self.__dict__[item]

    def __setitem__(self,key,value):    #添加一个属性
        self.__dict__[key]=value

    def __delitem__(self,key):
        del self.__dict__[key]
Y=Person('yayan',18)
print(Y['name'])  #将name传给getitem里的item
Y['hobby']='sleep'  #将hobby,sleep传入__setitem__
print(Y.hobby) #Y.hobby = Y['hobby']
del Y['hobby']
print(Y['hobby'])

六.__new__ : 构造方法，创建一个对象
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __new__(cls,*args,**kwargs):
        print('new function')
        return object.__new__(A,*args,**kwargs)  #实例化对象是谁取决于__new__方法,__new__返回什么就是什么,


七.__eq__ :当判断两个对象是否相等的时候，正常情况是判断它们内存地址是否相同，可以改写__eq__方法

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __eq__(self, other):
        if self.__dict__ == other.__dict__ :
            return True


y=Person('yayan',18)
w=Person('yayan',18)

print(y == w)


八.__hash__

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


y = Person('yayan', 18)
w = Person('yayan', 18)
print(hash(y))
print(hash(w))  #默认会根据内存地址去哈希，并且每次调用，结果不同

#如果想要当每个对象属性相同，则hash值相同，可以更改类中的hash方法
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __hash__(self):
        return hash(self.name+str(self.age))

y = Person('yayan', 18)
w = Person('yayan', 18)
print(hash(y))
print(hash(w))


九.set依赖对象的hash和eq值
 应用：当某两个对象的个别属性相同时，想要去重，用set

















