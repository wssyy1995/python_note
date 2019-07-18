#命名空间：
#    （1）全局命名空间
#    （2）局部命名空间
#    （3）内置命名空间

#解释器启动>加载input.print等内置命名空间>程序开始执行>加载全局命名空间，有input,part>程序执行到到part()>加载part里的命名空间，
# part里没有定义过input，所以先向上全局命名空间里找input,有则调用全局命名空间里的input
'''def input():
    print('this a global name')

def part():
    input()

part()
'''

#作用域
#全局作用域 ：内置和全局命名空间的名字都属于全局作用域 globals()查看
#局部作用域：函数（局部）命名空间的名字属于局部作用域   locals()查看


#对于全局作用域中的，不可变数据类型()，无法直接在局部作用域中修改
#如要修改，需加上global声明

'''a=1
def achange():
    global a
    a +=2

achange()
print(a)
'''




