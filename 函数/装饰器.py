#装饰器的作用 ：在定义一个函数后，想在这个函数前后加东西，但是又不能更改原函数内容，并想仍然用原始函数名来调用，就可以使用装饰器



#开放封闭原则：
#  开放：对扩展是开放的
#  封闭：对内部修改是封闭的

#装饰器（decorator）形成的过程
#（1）被装饰函数无参数，无返回
import time
'''
def timmer(f):               #timmer就实现了一个装饰器的功能，f()就是被装饰的函数
    def inner():
        start = time.time()
        f()
        end = time.time()
        print(end - start)
    return inner

@timmer    #语法糖：在被装饰的函数定义上添加：@装饰器名字 ，相当于 func=timmer(func)
def func():
    time.sleep(3)
    print('guangjing is sb')

#func=timmer(func)          #先将func函数内存地址传给timmer，得到inner函数的内存地址，并重新赋值给func这个变量
func()                     #此时func() 相当于调用inner函数，inner函数中的f()则为原来'func'的功能

'''





#（2）如果被装饰函数有返回值


'''def func():
    time.sleep(3)
    print('guangjing is sb')
    return 'yes ,actually!'

def timmer(f):
    def inner():
        start = time.time()
        ret=f()
        end = time.time()
        print(end - start)
        return ret   #需要在innder返回这个返回值
    return inner

func=timmer(func)

fret = func()   #定义一个变量去接收这个返回值ret
print(fret)
'''

#（3）如果被装饰函数需要带参数

'''def func(a):
    time.sleep(3)
    print('{} is sb'.format(a))
    return 'yes ,actually!'

def timmer(f):
    def inner(a):
        start = time.time()
        f(a)
        end = time.time()
        print(end - start)
    return inner

func=timmer(func)
func('guangjing')  #给inner的a传参
'''

#装饰器固定模式：
#（1）定义一个装饰器wrapper，参数必须为被装饰的函数名
#（2）定义闭包inner函数（是否需要参数，是否有返回）
#（3）warpper内必须返回inner函数名
#（4）在被装饰函数上添加语法糖：@wrapper
'''def wrapper(func):
    def inner(*args,**kwargs):
        #想在函数前添加的功能代码
        fres=func(*args,**kwargs)
        #想在函数后添加的功能代码
        return fres
    return inner

@wrapper
def func(*args,**kwargs):
    print('this is func')
    return 'this is func return'

fres=func(11,22,33,44,'ddf')
print(fres)
'''



#-----------------------------------------------------------------------------------------------#

#装饰器进阶内容：

 #（1）带参数的装饰器


需要套上第三个









#（2）多个装饰器装饰一个函数：


def wrapper1(f):
    def inner1():
        print('wrapper1 before')
        f()
        print('wrapper1 after')
    return inner1

def wrapper2(f):
    def inner2():
        print('wrapper2 before')
        f()
        print('wrapper2 after')
    return inner2


#程序是从上往下执行，但是装饰器顺序是先加上wrapper1，再加上wrapper2
@wrapper2    #inner1=wrapper2(inner1)
@wrapper1   #func=wrapper1(func)=inner1
def func():
    print('this is func')

func()











#-----------------------------------------------------------------------------------------------#

#作业：
#1：编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件)，并且一旦登录成功，后续的函数都无需重新登录

'''flag = False
def login(func):
    def inner(*args,**kwargs):
        global Flag
        if Flag :
            ret = func(*args, **kwargs)
            return ret
        else :
        #登录程序
            uname=input('please input your name:')
            pwd=input('please input your password:')
            if uname=='suyayan' and pwd == '123456ff':
                Flag = True
                ret = func(*args,**kwargs)
                return ret
            else:
                print('log in failed')
    return inner


@login
def shoplist_add():
    print('增加一件物品')

@login
def shoplist_del():
    print('删除一件物品')

shoplist_add()
shoplist_add()
shoplist_del()
'''

#2:编写装饰器为多个函数加上记录调用功能，要求每次调用函数都将被调用的函数名称写入文件

'''def log(func):
    def inner():
        with open('/Users/suyayan/Downloads/py file operation/log.text',mode='a',encoding='utf-8') as f :
            f.write(func.__name__+'\n')
        func()
    return inner

@log
def shoplist_add():
    print('增加一件物品')

@log
def shoplist_del():
    print('删除一件物品')

shoplist_add()
shoplist_del()
shoplist_add()
shoplist_add()
shoplist_add()
'''

#3 编写下载网页内容的函数：用户传入一个url，函数返回页面下载的结果，并为这个函数编写装饰器，实现缓存网页内容的功能（下载的页面存放于文件中，如果文件内有值，就优先从文件中读取网页内容）
'''import os
from urllib.request import urlopen

def cache(func):
    def inner(url):
        if os.path.getsize('/Users/suyayan/Downloads/py file operation/web_cache.text'):
            with open('/Users/suyayan/Downloads/py file operation/web_cache.text',mode='rb') as w:
                return w.read()
        ret = func(url)
        with open('/Users/suyayan/Downloads/py file operation/web_cache.text',mode='wb') as w2:
            w2.write(b'dddd'+ret)
        return ret
    return inner


@cache
def get(url):
    code = urlopen(url).read()
    return code

ret=get('http://www.baidu.com')
print(ret)
'''


