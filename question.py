(1)random 生成多个区间的随机数

(2)导入模块中的变量与方法，在当前模块重新为这个变量赋值（不是应该会覆盖吗？），调用这个方法，为什么仍然指向原内存地址
from importtest2 import it222,it22
it222=4
it22()


已解决：(3)当对象去调用类的静态属性时，会在自己的命名空间里生成新的这个属性？之后再通过对象调用这个静态属性，就不再向类寻找了？
class Course:
    language='Chinese'
    def __init__(self,name,price):
        self.name=name
        self.price=price

#    对象的命名空间通过类对象指针，指向类的命名空间
#    每当对象调用一个属性时，先会在自己的命名空间里找，如果找不到，就去类的命名空间里找
python=Course('python',1000)
print(Course.language)
print(python.language)
Course.language='English'
python.language='japanese'
Course.language='france'
print(Course.language)
print(python.language)

（4）多继承
广度优先问题

class A:
    def func(self):
        print('A')


class B(A):
    def func(self):
        super().func()
        print('B')

class C(A):
    def func(self):
        super().func()
        print('C')

class D(B,C):
    def func(self):
        super().func()
        print('D')



d=D()
d.func()

