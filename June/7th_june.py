# LC 2196 Create Binary Tree From Descriptions

class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right 


class Solution:
    def createBinaryTree(self,descriptions):

#         # pattern 
#         nodes = {}        # value -> TreeNode
# children = set() # all nodes that appeared as child

# # build links

# root = all_nodes - children
        # root is the node that never appears as a child
        nodes={}
        children=set()
        for parent,child,isLeft in descriptions:
            if parent not in nodes:
                nodes[parent]=TreeNode(parent)

            if child not in nodes:
                nodes[child]=TreeNode(child)

            if isLeft:
                nodes[parent].left=nodes[child]
            else:
                nodes[parent].right=nodes[child]

            children.add(child)

        for node_val in nodes:
            if node_val not in children:
                return nodes[node_val]


# preorder traversal
def preorder(root):
    if not root:
        return

    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)


def display(root, level=0):

    if root is None:
        return

    display(root.right, level + 1)

    print("    " * level + str(root.val))

    display(root.left, level + 1)


descriptions=[[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]

sol=Solution()

root=sol.createBinaryTree(descriptions)

preorder(root)
