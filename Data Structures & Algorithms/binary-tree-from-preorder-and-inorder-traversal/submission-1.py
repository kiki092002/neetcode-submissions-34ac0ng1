# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        else:
            root = TreeNode(preorder[0])
            root_index = inorder.index(root.val)

            leftSubtree = inorder[:root_index]
            rightSubtree = inorder[root_index+1:]

            leftPreorder = preorder[1:1+len(leftSubtree)]
            rightPreorder = preorder[1+len(leftSubtree):]
            root.left = self.buildTree(leftPreorder,leftSubtree)
            root.right = self.buildTree(rightPreorder,rightSubtree)
        return root