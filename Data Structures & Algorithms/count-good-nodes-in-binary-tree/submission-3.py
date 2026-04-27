# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def preorder(node,global_max):
            
            if not node:return 0
            res = 1 if node.val >=global_max else 0
            res += preorder(node.left,max(global_max,node.val))
            res += preorder(node.right,max(global_max,node.val))
            return res
        return preorder(root,root.val)