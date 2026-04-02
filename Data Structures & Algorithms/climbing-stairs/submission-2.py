class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def dfs(n):
        
            if n<=2:
                return n 
            
            if n in cache:
                return cache[n]
            
            cache[n] = dfs(n-1) + dfs(n-2)
            return cache[n]
        return dfs(n)