# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    

        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # base case
        def dfs(node,cumSum)-> int:
            if not node:
                return False
            cumSum += node.val
            if not node.left and not node.right:
                return cumSum == targetSum
            
            left_found =  dfs(node.left,cumSum)
            
            right_found=    dfs(node.right,cumSum)
            return left_found or right_found
        return dfs(root,0)