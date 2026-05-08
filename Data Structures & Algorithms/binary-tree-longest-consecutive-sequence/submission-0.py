# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            left_len = dfs(node.left)
            right_len = dfs(node.right)
            curr_len = 1
            if node.left and node.left.val == node.val+1:
                curr_len = max(curr_len,left_len +1)
            if node.right and node.right.val == node.val+1:
                curr_len = max(curr_len,right_len+1)
            ans = max(ans,curr_len)
            return curr_len 
        dfs(root)
        return ans


        # dfs(1) -> dfs(3) 
        # at dfs(3) -> dfs(2) left right 0 curr len = 1 ->return 1 
        # at dfs(3) -> currlen = right +1 = 3
        # dfs(4) left 0 right = 1 curr  = max(1,2) - 2 return 2-> dfs(5) left right 0 0 currlen = 1 return 1