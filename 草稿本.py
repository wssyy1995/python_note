
# class Node(object):
#     def __init__(self, data, next=None):
#         self.val = data
#         self.next = next
#
#
# def fun4(head):
#     if head == None:
#         return None
#     L, M, R = None, None, head
#     while R.next != None:
#         L = M
#         M = R
#         R = R.next
#         M.next = L
#     R.next = M
#     return R
#
# # 测试用例
# if __name__ == '__main__':
#     l1 = Node(3)
#     l1.next = Node(2)
#     l1.next.next = Node(1)
#     l1.next.next.next = Node(9)
#     l = ReverseList(l1)
#     print(l.val, l.next.val, l.next.next.val, l.next.next.next.val)




# #随机红包：
# import random
# def hongbao(total,num):
#     each=[]
#     already=0
#     for i in range(0,num):
#         t = round(random.uniform(0.01,2), 2)
#         each.append(t)
#         already=already+t
#     each.append(total-already)
#     return each
#
# ret=hongbao(10,5)
# print(ret)


#
# class Tree():
#     def __init__(self,value=None,left=None,right=None):
#         self.value=value
#         self.left=left
#         self.right=right
#
#
# def pretraverse(tree):
#
#     if tree == None:
#         return
#     print(tree.value)
#     pretraverse(tree.left)
#     pretraverse(tree.right)
#
# def midtraverse(tree):
#
#     if tree == None:
#         return
#     midtraverse(tree.left)
#     print(tree.value)
#     midtraverse(tree.right)
#
# def righttraverse(tree):
#
#     if tree == None:
#         return
#     righttraverse(tree.left)
#     righttraverse(tree.right)
#     print(tree.value)
#
#
# tree=Tree('A',left=Tree('B',right=Tree('C',left=Tree('D'))),right=Tree('E',right=Tree('F',left=Tree('G',left=Tree('H'),right=Tree('K')))))
#
# print('前序遍历')
# pretraverse(tree)
#
#
# print('中序遍历')
# midtraverse(tree)
#
# print('后序遍历')
# righttraverse(tree)

# m=1234
#
# print(n)
#




a = [1,3,5,7,9]
b = [2,4,6,7,10,11,34,55]
for i in b:
    a.append(i)

a.sort()
print(a)

test1 = [1, 3, 5, 7, 9]
test2 = [2, 4, 6, 7, 10, 11, 34, 55]


def mergetest(test1, test2):
    result = []
    len1 = len(test1)
    len2 = len(test2)
    i = 0
    j = 0
    while i < len1 and j < len2:
        if test1[i] <= test2[j]:
            result.append(test1[i])
            i += 1
        else:
            result.append(test2[j])
            j += 1
    if i < len1:
        for z in range(i + 1, len1):
            result.append(test1[z])
    elif j < len2:
        for z in range(j + 1, len2):
            result.append(test2[z])
    return result


print(mergetest(test1, test2))
