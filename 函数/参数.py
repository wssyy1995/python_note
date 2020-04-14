
#位置传参
'''def devide(a,b):
    dev=a/b
    return dev
dev1=devide(1,2)
print(dev1)
'''

#关键字传参
'''
dev2=devide(b=1,a=2)
print(dev2)
'''

#默认参数
'''
def classmate(name,sex='男'):
     print('{}是{}的'.format(name,sex))


classmate('koko','男')
classmate('koko') #如果与默认参数的值相等，则不需要传了
classmate('yayan','女')
'''

#默认参数的陷阱：如果默认参数的值是一个，那么每一次调用函数，如果不传参，则会共用这个资源

'''def func(l=[]):
    l.append(1)
    print(l)

func()
func()
func() 
'''

#动态参数-*args:只能接收位置参数 。需要传多个参数，但是不确定数量的时候, *args相当于接收了一个元祖 ，但是只能

'''def sum(*args):
    sum=0
    for i in args:
        sum=sum+i
    return sum

sum=sum(1,2,3)
print(sum)
'''

# 动态参数-**kwargs : 接收关键字参数，并组成一个字典
'''def dic(**kwargs):
    print(kwargs)

dic(a=1,b=2,c=3)
'''

#定义参数顺序： 位置参数 > *args > 默认参数 > **kwargs


# 动态参数的另外一种方式
'''def func(*args):
    print(args)

l=[1,2,3,4,5,6,7,8]
func(*l)
 '''
#在传参时，如果是一个序列，加上* ，就是将这个序列按顺序传入args