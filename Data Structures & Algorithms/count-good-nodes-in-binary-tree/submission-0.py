# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if node is None:
                return 0

            print(f"Visiting Node: {node.val}, Max so far: {max_val}")

            is_good = node.val >= max_val
            count = 1 if is_good else 0

            if is_good:
                print(f"Node {node.val} is GOOD")
            else:
                print(f"Node {node.val} is NOT good")

            max_val = max(max_val, node.val)

            count += dfs(node.left, max_val)
            count += dfs(node.right, max_val)

            print(f"Returning count {count} from node {node.val}")
            return count

        return dfs(root, root.val)
        
        
