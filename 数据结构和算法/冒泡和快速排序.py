













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