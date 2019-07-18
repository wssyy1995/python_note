#递归函数
   #了解什么是递归 ：在一个函数里再调用这个函数本身
   #能看懂递归
   #能知道递归的应用场景
   #初始递归
   #算法--二分查找算法
   #三级菜单--递归实现

#求年龄的例子：
#n=4,age(4)=40
#n<4 age(n)=age(n+1)+2
def age(n):
    if n == 4:
        return 40
    else:
        return age(n+1)+2

print(age(1))




#二分查找算啊，必须处理有序的列表

代码实现
l=[2,3,6,7,8,9,10,12,23,34,35,36,37,38,39,44,45,47,48,51,56,57,58,59,60,66,67,68,69,76,77,78,79,98,99]

def find(l,aim,start=0,end=None): #默认参数end不能直接放len(l)
    end = len(l) if end is None else end
    mid_index = (end-start)//2+start   #计算中间值
    if start <= end:
        if l[mid_index] < aim:
            ret=find(l,aim,start=mid_index+1,end=end)
            return ret
        elif l[mid_index] > aim :
            ret=find(l,aim,start=start,end=mid_index-1)
            return ret
        else:
            return mid_index
    else:print('can not find')



ret=find(l,2)
print(ret)



#递归三级菜单


