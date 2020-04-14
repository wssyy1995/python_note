
#可以被for循环的数据类型：
# str,list,dic,set,tuple,f=open(),range(),enumerate

print(dir([])) #告诉列表所拥有的所有方法

print('__iter__' in dir([])) #只要是能被for循环的数据类型（可迭代的数据类型），就一定拥有__iter__方法

#  可迭代协议 --- 只要含有__iter__方法的都是可迭代的对象

print([].__iter__())  #迭代器：一个可迭代对象 执行了__iter__方法之后，就得到一个迭代器

#迭代器协议 ---  内部含有__next__方法和__iter__方法的就是迭代器

#for循环其实就是在使用迭代器

print(dir([].__iter__())) #迭代器内部的方法

list=[1,2,3,'abc']
iterator = list.__iter__()
print(iterator.__next__()) #迭代器内部的__next__方法

# For循环的本质：
for i in list:
    pass
# 生成一个list的迭代器：iterator=list.__iter__()
# 当循环时，拿到的每一个i是由 iterator.__next__() 取到的
# 当迭代器报错时，自动结束循环


#迭代器的好处：
#   （1）从容器类型中一个个取值，会把所有值取到
#   （2）节省内存空间  such as : range(1000000) ，f=open(), 对于迭代器，并不会在内存中再占用一大块内存，而是随着循环，每次生成一个