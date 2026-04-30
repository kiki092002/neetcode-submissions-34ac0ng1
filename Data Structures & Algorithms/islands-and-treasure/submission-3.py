class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        INF = 2147483647
        def bfs(r,c):
            q = deque([(r,c)])
            visited = set()
            visited.add((r,c))
            steps =0
            while q:
                for _ in range(len(q)):
                    row,col = q.popleft()
                    if grid[row][col] == 0:
                        return steps
                    for dr,dc in directions:
                        nr,nc = row+dr,col+dc
                        if(0<=nr<m and 0<=nc<n and (nr,nc) not in visited and grid[nr][nc]!=-1):
                            visited.add((nr,nc))
                            q.append((nr,nc))
                steps +=1
            return INF

        for i in range(m):
            for j in range(n):
                if grid[i][j] == INF:
                    grid[i][j] = bfs(i,j)


        