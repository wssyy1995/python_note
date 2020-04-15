完全二叉树和满二叉树：
(1)满二叉树属于完全二叉树，但是每层都挂满了节点，总节点数为2^h-1
(2)完全二叉树的高度是h的话，第1-(h-1)层都是满节点，即满二叉树，第h层的节点是紧靠左排列的；总节点数范围为2^(h-1) ~ 2^h-1


二叉树的遍历
    -广度优先:一层层遍历，每一层从左向右遍历
    -深度优先
        -先序遍历：根—左—右:从根开始，就先将根pop进队列，每一层都是先访问左边子节点，如果子节点有下一层孙节点，就下探到孙节点的左边子节点（如果当前下探的左边子节点没有下一层，才遍历右边的节点，但是右边的节点往下也是从左边开始遍历）
        -中序遍历：左-根—右：每一层也都是向子节点的左边先遍历，但是只有当左子节点都遍历完，上回到根节点，将根节点pop进队列

class Tree():
    def __init__(self,value=None,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right


def pretraverse(tree):

    if tree == None:
        return
    print(tree.value)
    pretraverse(tree.left)
    pretraverse(tree.right)

def midtraverse(tree):

    if tree == None:
        return
    midtraverse(tree.left)
    print(tree.value)
    midtraverse(tree.right)

def righttraverse(tree):

    if tree == None:
        return
    righttraverse(tree.left)
    righttraverse(tree.right)
    print(tree.value)
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