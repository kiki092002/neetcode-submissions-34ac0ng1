class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid and not grid[0]:
            return 0 
        m, n = len(grid), len(grid[0])
        def dfs(i,j):
            # check out of boundary or it's water
            if i <0 or i >= m or j < 0 or j >= n or grid[i][j] =='0':
                return 
            grid[i][j] ='0' 
            # marked visited cell 0 to avoid count same cells multiple time 
            # Recursively visit all adjacent cells (up, down, left, right)
            dfs(i - 1, j)  # up
            dfs(i + 1, j)  # down
            dfs(i, j - 1)  # left
            dfs(i, j + 1)  # right

        count = 0 
        # traverse tho grid 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count +=1
                    dfs(i,j)
        return count 