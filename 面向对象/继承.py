#面向对象的三大特性：继承，多态，封装

一.继承

（1）新建的类可以继承一个或多个父类

class A:    #父类A
    pass

class B:       #父类B
    pass

class A_son(A): #子类，括号中是父类 ，一个类可以被多个类继承
    pass

class AB_son(A,B):  #一个类可以继承多个父类（python独有）
    pass




（2）单继承
print(A_son.__bases__)  # 看这个类继承了哪些类
# 在python3里，所有的类都有父类，如果他没有继承，默认继承object，称为新式类

例子：
class Animal:
    def __init__(self,name,hp):
        self.mame=name
        self.hp=hp
        self.func()

    def func(self):
        print('animal function')



#当子类调用父类的方法时，传入的self是子类的对象，当子类有这个方法时用自己的，没有自己的方法才用父类的
class Dog(Animal):
    def func(self):
        print('dog fucntion')
dog=Dog('suisui',100)     #生成实例，调用init方法，Dog类中没有，于是到父类中找，将self=dog，name='suisui',hp=100传入父类的init方法,所以在父类init方法中的，self.func()调用的是Dog类的func()



#派生属性：当子类调用父类的__init__方法，想再添加自己的独特的属性,可以在init方法中调用父类的init，在添加上自己独有的属性，称为派生属性
class Animal:
    def __init__(self,name,hp):
        self.mame = name
        self.hp = hp
class Dog(Animal):
    def __init__(self, name, hp, kind):
        Animal.__init__(self, name, hp)
        self.kind = kind

#派生方法:如果父类中没有的方法，在子类中出现，叫做派生方法

#子类调用一个方法，先在自己的类中寻找这个名字，没有的话用父类的
#如果想用父类的方法中，并再添加一些功能，可以在子类的方法中，调用父类方法，再添加功能
class Animal:
    def __init__(self,name,hp):
        self.mame = name
        self.hp = hp
    def eat(self):
        print('animal eat medicine')
        self.hp+=100

class Dog(Animal):
    def eat(self):
        Animal.eat(self)  #调用父类方法，记得加上self
        print('dog eat medicine')
        self.hp+= 200

dog=Dog('suisui',100,'tugou')
dog.eat()
print(dog.hp)

#super() 的使用（仅限python3）
上面派生属性和派生方法中，子类中调用父类的方法，可以用super()来代替父类的名字，并不需要再加self

如：
Animal.__init__(self, name, hp)  =  super().__init__(name.hp)
Animal.eat(self) = super().eat()

super()外部调用：括号内传入类名，对象名 ： super(Dog,dog).eat()



（3）多继承
就近原则：优先调用A的属性和方法
class D(A,B,C)

钻石继承：D继承B,C, B&C继承A，那么D也继承了A的方法和属性
        寻找顺序是：D> B>C >A（广度优先算法，在B 的节点，有A和C 两种选择，但是C也可到达A，所以先走C）

漏斗继承：D继承B,C，B继承A，C继承E
        寻找顺序是：D>B>A>C>E (在B的节点，因为A只有B 继承了，错过这个节点就找不到A了，所以优先找A)


查看继承顺序：D.mor()  #这个方法只在新式类里
新式类：广度优先，python2.7以上的类都是新式类（继承object的类）
经典类：深度优先，python2.7以下有新式类和经典类

super()用法在多继承里的用法：
    不是直接找这个节点的父类，而是根据调用者的节点位置的继承顺序来的