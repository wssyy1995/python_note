#普通函数
'''def calc(n):
    return n**n
print(calc(3))
'''

#匿名函数 :
# （1）参数可以有多个，用逗号隔开
# （2）匿名函数函数不允许换行，逻辑执行结束后的内容就是返回值

calc2 = lambda n:n**n

#匿名函数可以匿名
#例子 ：求字典里value最大的key

dic={'k1':111,'k2':222,'k3':333}
print(max(dic,key=lambda k:dic[k]))

#匿名函数都可以跟带key的函数合作
