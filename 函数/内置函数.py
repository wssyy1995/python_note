#某个方法属于某个数据类型的变量，就用.调用
#如果某个方法不依赖于任何数据类型， 就直接调用   ----内置函数和自定义函数




#(1)作用域相关
'''1.globals() #查看全局作用域中所有的名字
2.locals()  #查看局部作用域中所有的名字
'''

#（2）迭代器相关

'''
1.next（迭代器） = 迭代器.__next__() #作用完全一样,对迭代器进行下一次取值
2.iter(可迭代对象) = 可迭代对象.__iter__()  #生成一个迭代器
3.range() #（可迭代对象，不是迭代器）
'''



#（3）其他

'''1.dir（[]） #查看一个变量，类型拥有的所有方法
2.callable(print)  #查看一个名字是否是一个函数名字，返回True/False
3 help(str)  #打印出这个数据类型，函数相关的信息
4.import os 相当于 os = __import__('os') #导入模块
5.open（）  #打开一个文件
6.id（）  #返回一个变量的内存地址
7.hash(数据类型) #对于相同可hash数据的hash值在一次程序的执行过程中总是不变的；不可哈希则报错
#dict字典寻址方式：key是可哈希数据类型，通过key哈希值来寻找value
8.input()
9.print() #print(end='')>指定输出结束符 ，print(sep='|')>指定输出多个值之间的分隔符
'''import time
for i in range(0,101,2):
    time.sleep(0.05)
    char_num=i//2  #i整除2
    per_str='\r%s%%:%s\n'%(i,'*'*char_num) if i==100 else '\r%s%%:%s'%(i,'*'*char_num)
    print(per_str,end='',flush=True)

#\r使得每次从行首开始打印，end=''使得从当前一行开始打印，配合使用则可以覆盖上一条打印的数据
'''
10.exec('print(123)')
11eval('print(456)')
#exec和eval都可以执行字符串类型的代码，建议不要用
#eval有返回值-有结果的简单计算，exec没有返回值-简单的流程控制
12.compile() #编译一段代码，用exec（流程类）/eval（计算类）/single（交互类）去执行
'''

#基础数据类型相关

'''1.bool() #布尔
2.int()   #整型
3.float() #浮点数
#数据类型转换时使用

4.complex  #复数
5.bin(10) #转换成二进制
6.oct(10)  #转换成十进制
7.hex(10)  #转换成十六进制
8.abs(-8)  #绝对值
9.divmod(7,2) #返回商数与余数
10.round(3.14159,3)  #小数的精确
11.pow(2,3)  #求幂运算，2的三次方
12.sum(只接受可迭代的数据类型) #sum([1,2,3,4,5,6])
13.min(可迭代的数据类型 或 *args) # key='abs'，
14.max(可迭代的数据类型 或 *args)

15.list() #列表
16.tuple() #元祖
#数据类型转换时使用

17.list.reverse() #将list内的数据反序
18.12=reversed(list) #生成一个新的迭代器，将list内的数据反序
19.slice() #列表切片

20.str() #数据类型转换时使用

21.format()
 功能很多
 #占位符（常用）
 #调整输出格式 ：format('test','<20')

22.bytes #unicode转成gbk/utf-8
bytes('你好'，encoding='gbk/utf-8')
#网络编程，照片和视频，html网页爬去到的都是二进制编码

23.bytearray #一个列表，每一个元素为一个人字节编码，可以用来操作字节

24.memoryview

25.ord #字符按照unicode转数字
26.chr #数字按照unicode转字符
27.ascii()  #如果是ascii编码内的字符就打印出来，如果不是则输出\u编码

28.repr()  #返回一个对象的string格式

29.dict
30.set
31.frozenset  #frozenset可以作为字典的key,因为是不可变类型
32.all()  #接收可迭代对象，判断是否有bool值为false的值,有一个False则为false
all([1,2,''])
33.any()  #判断是否有bool值为True的值,有一个True则为True
'''
#重要方法

1.zip() # 将两组序列组合拉上

l=[1,2,3]
l2=['a','b','c']
print(zip(l,l2))
for i in zip(l,l2):
    print(i)


2.filter(判断函数，可迭代对象)

def is_odd(x):
    return x%2==1
ret = filter(is_odd,[1,2,3,4,5,6,7]) #返回一个过滤器类型，实现了__iter__和__next__方法，相当于一个迭代器，可以用for循环将每个迭代的元素放入判断函数，如果值是True，才返回
for i in ret:
    print(i)

3.map(参数1：函数名,参数二：可迭代对象)：依次将可迭代对象里的元素引应用到参数1的函数中
ret=map(abs,[1,-4,-5,2,-9])
for i in ret:
    print(i)

相当于：
for i in [1,-4,-5,2,-9]:
    print(abs(i))


reduce(参数1：函数，参数二:可迭代对象)：依次将可迭代对象里的元素引应用到参数1的函数中，但是参数1接受两个元素，上两个元素的结果将作为第一个参数，与下一个元素继续传入
l=[1,2,3,4,5,6]
sum(1,2)



4.sorted([1,4,7,2,3]) #生成一个新的列表，与reversed不同，缺点：sorted是一次性生成，占内存
#l.sort 在元列表的基础上进行排序

list=['    ',[1,2],'hello world']
ret= sorted(list,key=len)
print(ret)
