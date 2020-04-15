# 冒泡排序
'''
1.比较相邻的元素。如果第一个比第二个大，就交换他们两个

2.对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。第一轮下来，最后的元素会是最大的数。

3.针对所有的元素重复以上的步骤，除了最后一个。

4.持续每次对越来越少的元素重复上面的步骤，直到比较完第一个和第二个元素；比较结束
'''
l=[8,2,6,5,9,3,1,4,3,7,0]
# def bubble(l):
#     for i in range(1,len(l)):
#         for j in range(0,len(l)-i):
#             if l[j]>l[j+1]:
#                 l[j],l[j+1]=l[j+1],l[j]
#
#     return l
#
# print(bubble(l))



# 快速排序
'''
1.首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置

2.再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。

2.重复第二步，直到所有元素均排序完毕。
'''
#
# def quicksort(l):
#     for i in range(0,len(l)-1):
#         minIndex=i
#         for j in range(i+1,len(l)):
#             if l[j]<l[minIndex]:
#                 minIndex=j
#         l[i],l[minIndex]=l[minIndex],l[i]
#
#     return l
#
# print(quicksort(l))









#二分查找，必须处理有序的列表

# 实现
l=[0,1,2,3,4,5,66,77,88,99,111,113,114,115,116,117]
def find(l,aim,start=0,end=len(l)-1): #默认参数end不能直接放len(l)??
    # end = len(l) if end is None else end
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



ret=find(l,77)
print(ret)
print(l.index(77))

