class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0 
        m,n = len(grid),len(grid[0])
        max_area = 0 
        def dfs(i,j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
            # marked visited 0 to avoid calculate multiple time 
            grid[i][j] =0
            #Recursively visit all four adjacent cells (up, down, left, right) and sum their areas.
            area =1
            area += dfs(i-1,j)
            area += dfs(i+1,j)
            area += dfs(i,j-1)
            area += dfs(i,j+1)
            return area

        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # call dfs and cal the area 
                    curr_max_area = dfs(i,j)
                    max_area = max(max_area,curr_max_area)
        return max_area