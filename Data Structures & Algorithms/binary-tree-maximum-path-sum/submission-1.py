# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.global_max = float('-inf')
        def dfs(node):
            if not node: return 0 
            left_path_sum = max(0,dfs(node.left)) # avoid negative num
            right_path_sum = max(0,dfs(node.right))

            self.global_max = max(self.global_max,left_path_sum+node.val + right_path_sum)
            return max(left_path_sum,right_path_sum)+node.val
        dfs(root)
        return self.global_max