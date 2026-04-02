class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        rows,cols = len(heights),len(heights[0])

        pacific_reachable = set() # cells that reach pacific ocean
        atlantic_reachable = set() # cells that reach atlantic ocean 
        # up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(r,c,visited,prev_height):
            #base case : out of bounds and height is invalid 
            if (r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or heights[r][c] < prev_height):
                return
            visited.add((r,c))
            print(visited)
            for dr,dc in directions:
                dfs(r+dr,c+dc,visited,heights[r][c])
            


        # loop thro top cols
        for c in range(cols):
            # top row
            dfs(0,c,pacific_reachable,heights[0][c])
        # loop thro left rows
        for r in range(rows):
            dfs(r,0, pacific_reachable,heights[r][0])
        # loop thro bottom row
        for c in range(cols):
            dfs(rows-1,c, atlantic_reachable,heights[rows-1][c])
        # loop thro right bottom 
        for r in range(rows):
            dfs(r,cols-1, atlantic_reachable,heights[r][cols-1])

        print(pacific_reachable)
        print(atlantic_reachable)
        result = list(pacific_reachable & atlantic_reachable)
        return result