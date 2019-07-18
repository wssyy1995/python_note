#函数的嵌套调用
'''def max2(a,b):
    return a if a>b else b

def max3(x,y,z):
    c=max(x,y)
    return max(c,z)

max=max3(989,6,111)
print(max)
'''

#函数的嵌套定义
'''def outer():
    a=3
    def inner():
        print(a) #上一级局部命名空间的名字可以在下一级的局部命名空间内使用，但不能直接修改该不可修改类型
        nonlocal a #声明上一级的局部变量（对全部无效），但python 3.7会报错       
        a+=3
        print('innter')
        print(a)
    inner()
outer()
'''

#闭包：内部函数对外部函数作用域里变量的引用（非全局变量），则称内部函数为闭包。

#闭包三要素：1、嵌套函数　 2、变量的引用 3、返回内部函数
'''#定义一个嵌套函数（要素1）
 def test(num):
      def test_in(num_in):
         #内部函数引用外部函数的变量(非全局变量)（要素2）
          print("sum = %s"%(num + num_in))
          #返回的结果可以被打印出来
          return num,num_in
      #返回内部的函数（要素3）
      return test_in
 这里的rtn就是当num为10时的test_in
 rtn = test(10) 
 print(rtn)
 #内部函数test_in传参
 print(rtn(20))
'''

#闭包的应用
#基础版
'''from urllib.request import urlopen
'ret = urlopen('http://www.baidu.com').read()
print(ret)
'''

#升级版：为了能每次使用函数，减少局部变量ret在内存中重复开辟空间
'''from urllib.request import urlopen
def get_url():
    url='http://www.baidu.com'
    def get():
        ret = urlopen(url).read()
        print(ret)
    return get

get=get_url()
get()
'''

