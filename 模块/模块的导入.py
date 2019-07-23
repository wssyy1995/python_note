'''import importtest
import importtest2
import sys

#先从sys.module里查看是否已经被导入，
# 如果没有被导入，则依据sys.path路径去寻找模块，找到就导入，没找到报错
#创建这个模块的命名空间
#把文件中的名字都放到命名空间里

print(sys.modules())
importtest.it1()
importtest2.it2()

#给一个模块起别名(重命名之后，不能再用之前的名字)：
    import time as t

#导入模块规则：
    1/ 应该在文件最上方导入全部模块
    2/ 先导入内置模块，再导入扩展模块
    3/ 自定义的

#单独从某个模块调入某个方法，直接调用
    #如果本模块又定义一个相同名字的方法，会覆盖导入的那个方法

    from time import sleep
    sleep(1)

    from importtest import it11
    it11()


#from importtest2 import it222

from importtest2 import it222,it22
#print(it222)
it22()
it222=4
print(it222)


#将某个模块中的所有变量名全部导入
    from importtest2 import *
    it22()

#在模块中，有一个变量__name__,这个变量在当前模块下的值为__main__
当我们直接执行这个模块的时候，__name__ =='__main__' 下的方法在会被运行
当我们在另一个模块中import这个模块，__name__ 等于这个被导入的模块的名字，所以__name__ =='__main__' 下的变量与方法不会执行
总结：在某个模块中，有一些方法或者变量，你不需要被继承者运行，则用if __name__ =='__main__' 包裹一下



'''
import importtest2


