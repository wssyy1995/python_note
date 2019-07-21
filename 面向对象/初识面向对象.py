一.初始面向对象

(1)定义一个类：
class 类名：
    属性='a'

(2)查看一个属性
类名.属性

(3)类里的__init__方法：只要一调用类，就会调用这个方法

class Person():
    country='china' #创造了一个只要是这个类就一定有的属性，类属性，静态属性
    def __init__(self,*args):  #初始化方法，self是对象，是一个必须传的参数
        self.name=args[0]
        self.hobbie=args[1]
        self.age=args[2]

    def walk(self,n):     #方法，一般情况下必须传self参数，且必须传self参数，后面可以传其他参数
        print('%s走走走，走了%s步'%(self.name,n))


guangjing = Person('sb','eat',18)  #guangjing对象
print(guangjing.name)
guangjing.walk(10)
print(Person.country)

#对象=类名()
#过程：
    #类名() 首先会创造出一个对象，创建一个self变量
    #调用__init__方法，类型()括号里的参数会被这里接受
    #执行__init__方法
    #返回self
    #调用这个类的属性时，执行'对象.属性' 相当于调用self.属性



(4)类名和对象名.__dict__ ：可以查看这个类和对象的属性，对象的属性可以通过__dict__进行修改
guangjing.__dict__['hobbie']='sleep'    相当于 guangjing.hobbie='sleep'
__dict__对于类中的名字不能进行操作




（5）什么时候使用面向对象？
  1.当有几个函数需要反反复复传入相同参数的时候，就可以考虑面向对象。这些参数都是对象的属性
  2.当处理一类事物具有相似的属性和功能


例子：circle属性，半径，两个方法：求周长和面积
2pir,pir**2
from math import pi
class circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        return pi*(self.r**2)
    def perimeter(self):
        return 2*pi*self.r

c1=circle(5)
print(c1.r)
c1a=c1.area()
c1p=c1.perimeter()
print(c1a)
print(c1p)

#组合:一个类里的属性是另一个类的对象
class Ring:
    def __init__(self,inside_r,outside_r):
        self.inside_c=circle(inside_r)
        self.outside_c=circle(outside_r)

    def area(self):
        return self.outside_c.area() - self.inside_c.area()

    def perimeter(self):
        return self.outside_c.perimeter()+self.inside_c.perimeter()

ring1=Ring(5,10)
print(ring1.inside_c)
print(ring1.outside_c)
print(ring1.area())
print(ring1.perimeter())


二.类的命名空间
(1)类里可以定义两种属性：静态属性，动态属性
class Course:
    language='Chinese'
    def __init__(self,name,price):
        self.name=name
        self.price=price
(2)更改这个类的静态属性
Course.language='English'

(3)创建一个这个类的对象，这个对象也能调用这个类的静态属性
#    对象的命名空间通过类对象指针，指向类的命名空间
#    每当对象调用一个属性时，先会在自己的命名空间里找(对象命名空间里有的，就直接用自己的)，如果找不到，就去类的命名空间里找
#    如果在类的命名空间里找到了，会在自己的命名空间里用相同的值生成新的这个属性，之后再通过对象调用这个静态属性，就直接用自己命名空间里的
#   如果需要删除这个属性  del
python=Course('python',1000)
python.language='japanese'
print(python.language)
del python.language
print(python.language)

(4) 类变量最好用类名操作


