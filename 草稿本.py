#
# # class Node(object):
# #     def __init__(self, data, next=None):
# #         self.val = data
# #         self.next = next
# #
# #
# # def fun4(head):
# #     if head == None:
# #         return None
# #     L, M, R = None, None, head
# #     while R.next != None:
# #         L = M
# #         M = R
# #         R = R.next
# #         M.next = L
# #     R.next = M
# #     return R
# #
# # # 测试用例
# # if __name__ == '__main__':
# #     l1 = Node(3)
# #     l1.next = Node(2)
# #     l1.next.next = Node(1)
# #     l1.next.next.next = Node(9)
# #     l = ReverseList(l1)
# #     print(l.val, l.next.val, l.next.next.val, l.next.next.next.val)
#
#
#
#
# # #随机红包：
# # import random
# # def hongbao(total,num):
# #     each=[]
# #     already=0
# #     for i in range(0,num):
# #         t = round(random.uniform(0.01,2), 2)
# #         each.append(t)
# #         already=already+t
# #     each.append(total-already)
# #     return each
# #
# # ret=hongbao(10,5)
# # print(ret)
#
#
#
# 输入: ["5","-2","4","C","D","9","+","+"]
# 输出: 27
# 解释:
# 第1轮：你可以得到5分。总和是：5。
# 第2轮：你可以得到-2分。总数是：3。
# 第3轮：你可以得到4分。总和是：7。
# 操作1：第3轮的数据无效。总数是：3。
# 第4轮：你可以得到-4分（第三轮的数据已被删除）。总和是：-1。
# 第5轮：你可以得到9分。总数是：8。
# 第6轮：你可以得到-4 + 9 = 5分。总数是13。
# 第7轮：你可以得到9 + 5 = 14分。总数是27。
#



ops=["-60","D","-36","30","13","C","C","-33","53","79"]


def score(ops):





    print(ops2)


    #
    # for i in range(len(ops2)):
    #     if ops2[i]=='D':
    #         ops2[i]=2*ops2[i-1]
    #
    #
    #
    #     elif ops2[i]=='+':
    #         ops2[i]= ops2[i-1]+ops2[i-2]
    #
    #     else:
    #         ops2[i]=int(ops2[i])
    #         print('数字字符串: %r'%(i))
    #     score=score+ops2[i]
    #
    #
    # return score





print(score(ops))



























# #
# # class Tree():
# #     def __init__(self,value=None,left=None,right=None):
# #         self.value=value
# #         self.left=left
# #         self.right=right
# #
# #
# # def pretraverse(tree):
# #
# #     if tree == None:
# #         return
# #     print(tree.value)
# #     pretraverse(tree.left)
# #     pretraverse(tree.right)
# #
# # def midtraverse(tree):
# #
# #     if tree == None:
# #         return
# #     midtraverse(tree.left)
# #     print(tree.value)
# #     midtraverse(tree.right)
# #
# # def righttraverse(tree):
# #
# #     if tree == None:
# #         return
# #     righttraverse(tree.left)
# #     righttraverse(tree.right)
# #     print(tree.value)
# #
# #
# # tree=Tree('A',left=Tree('B',right=Tree('C',left=Tree('D'))),right=Tree('E',right=Tree('F',left=Tree('G',left=Tree('H'),right=Tree('K')))))
# #
# # print('前序遍历')
# # pretraverse(tree)
# #
# #
# # print('中序遍历')
# # midtraverse(tree)
# #
# # print('后序遍历')
# # righttraverse(tree)
#
# # m=1234
# #
# # print(n)
# #
#
#
#
#
# a = [1,3,5,7,9]
# b = [2,4,6,7,10,11,34,55]
# for i in b:
#     a.append(i)
#
# a.sort()
# print(a)
#
# test1 = [1, 3, 5, 7, 9]
# test2 = [2, 4, 6, 7, 10, 11, 34, 55]
#
#
# def mergetest(test1, test2):
#     result = []
#     len1 = len(test1)
#     len2 = len(test2)
#     i = 0
#     j = 0
#     while i < len1 and j < len2:
#         if test1[i] <= test2[j]:
#             result.append(test1[i])
#             i += 1
#         else:
#             result.append(test2[j])
#             j += 1
#     if i < len1:
#         for z in range(i + 1, len1):
#             result.append(test1[z])
#     elif j < len2:
#         for z in range(j + 1, len2):
#             result.append(test2[z])
#     return result
#
#
# print(mergetest(test1, test2))

# class Course():
#     s_list=[1,2,4,['a','b']]
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#
#
# english=Course('yayan',18)
# print(english.name)
# print(english.price)
# english.gender='female'
# print(english.gender)
# print(english.s_list)
#
# Course.s_list.append(2)
# print(english.s_list)


#
#
# from functools import reduce
# a=[1,2,4]
# b=[6,7,8]
# print(a)
#
# def cheng(x,y):
#     return x*y
#
# c=reduce(cheng,a)
# print(c)

# a = [('a',1),('b',2),('c',3),('d',4)]
# a_1 = listmap(lambda x:x[0],a)
# print(a_1)

#
# def is_odd(x):
#     return x%2==1
# ret = list(filter(is_odd,[1,2,3,4,5,6,7]))
# print(ret)
#返回一个过滤器类型，实现了__iter__和__next__方法，相当于一个迭代器，可以用for循环将每个迭代的元素放入判断函数，如果值是True，才返回
# for i in ret:
# #     print(i)
# from functools import reduce
# a=[1,2,3,4,5,6,7]
# suma=reduce(lambda x,y:x+y,a)
# print(suma)
