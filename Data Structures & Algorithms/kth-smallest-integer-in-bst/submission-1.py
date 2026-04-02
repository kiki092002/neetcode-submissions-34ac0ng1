# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return
        self.val = 0
        self.count = 0
        def inorder(node):
            if not node:
                return 
            l = inorder(node.left)
            self.count +=1
            if self.count == k:
                self.val= node.val
            
            
            r = inorder(node.right)
        inorder(root)
        return self.val
       