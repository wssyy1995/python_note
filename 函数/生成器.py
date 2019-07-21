#生成器本质就是迭代器
#生成器的表现形式： （1）生成器函数 （2）生成器表达式

#（1）生成器函数

#普通函数
'''def generator():
     print(1)
     return 'a'

ret= generator()
print(ret)
'''

#生成器函数 ：只要含有yield关键字的函数都是生成器函数，yield只能写在函数内部，且不能跟return共用
# 使用yield语句一次返回一个结果，执行到yield，返回当前yield值之后挂起当前状态，下次调用的时候会从当前状态继续。：

'''def generator():
    print(1)
    print(22)
    yield 'a'
    print(33)
    print(44)
    yield 'b'


g = generator() #执行之后会得到一个生成器作为返回值
print(g)


ret = g.__next__() #第一次执行__next__方法，只执行第一个yield的上面的代码，只返回第一个yield的值
print(ret)
ret = g.__next__() 
print(ret)
'''



#生成器也是一个迭代器，可以用for循环

'''for i in g:
    print(i)
    
'''


#例子1：调用一个函数，生成2000个数据sb1,sb2,sb3...sb2000
# 应用生成器的好处：一边生成，一边执行，节省空间

'''def sbgenerator():
    for i in range(200):
        print('number:',i)
        yield 'this is sb{}'.format(i)

sbg=sbgenerator()
'''

#例子1.2： sb生成器想先生成50个，再继续生成20个

'''count=0
for i in sbg:
    count += 1
    print(i)       # i=sbg.__next__() 是在刚进入循环就执行的，所以要先把yield输出才能break
    if count > 49:
        break

print('上面是50个sb,下面是20个sb')

for i in sbg:
    count += 1
    print(i)
    if count > 69:
        break
        '''

#生成器函数进阶

#(1)生成器函数需要有yield结尾，否则调用__next__()会报错

'''def generator():
    print('this is 1')
    yield 1
    print('this is 2')
    yield 2
    print('this is 3')

g=generator()
ret = g.__next__()
print(ret)

ret = g.__next__()
print(ret)
'''
#第三次 调用 g.__next__()时会报错，因为没有yield，所以函数无法结束

#（2）send :效果与next基本一致，但是在获取下一个yield值的同时，到函数内上一个yield的位置传一个数据
#    使用send 的注意事项：1.第一次使用生成器的时候，必须用next  2.最后一个yield不能接受外部的值


'''def generator():
    print('this is 1')
    content = yield 1 #程序执行到这一行，是先执行等式右边的，所以yield 1 返回1之后，就挂起了，需要下一次执行send的时候，将send的值返回给content
    print('this is 2')
    print('sent content:',content)
    content2=yield 2
    print('this is 3')
    print('send cont:',content2)
    content3=yield 3
    print('send content:',content3)
    yield


g=generator()
ret = g.__next__()
print(ret)

ret = g.send('hello')
print(ret)

ret =g.send('hello2')
print(ret)

g.send('hello3')

'''

# send例子：求移动平均值 ava=sum/count

'''def average():
    sum = 0
    count = 0
    avg = 0
    while True:
        num = yield avg
        sum += num
        count += 1
        avg=sum/count

avg_g = average()
avg_g.__next__()
avg1=avg_g.send(10)
avg1=avg_g.send(20)

print(avg1)

'''

#（1）生成器表达式

#列表推导式
egg_list=['egg%d'%i for i in range(10)]
print(egg_list)

#生成器表达式
g=(i for i in range(10)) #生成器

print(g)
for i in g:
    print(i)

chicken=('egg%d'%i for i in range(10))  #生成器
print(chicken)
for egg in chicken:
    print(egg)



#生成器表达式与列表推导式的区别：
# 1.括号不一样
# 2.返回的值不一样，几乎不占内存





#进阶：各种推导式




