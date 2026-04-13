# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        boundaries = [root.val] 
        def left_bdr(node):
            if node:
                
                if node.left:
                    boundaries.append(node.val)
                    
                    left_bdr(node.left)
                elif node.right:
                    boundaries.append(node.val)
                    left_bdr(node.right)

        left_bdr(root.left)
        def leaves_bdr(node):
            if node:
                if node.left is None and node.right is None:
                    boundaries.append(node.val)
                    return 
                leaves_bdr(node.left)
                leaves_bdr(node.right)
        
        leaves_bdr(root.left)
        leaves_bdr(root.right)
        def right_bdr(node):
            if node:
                if node.right:
                    right_bdr(node.right)
                    boundaries.append(node.val)
                elif node.left:
                    right_bdr(node.left)
                    boundaries.append(node.val)
                
        right_bdr(root.right)
        return boundaries
                