class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append(((i,j),0))


        while q : 
            for _ in range(len(q)):
                (i,j),dist = q.popleft()
                for ni,ny in [(0,1),(0,-1),(1,0),(-1,0)]:
                    di = i+ni
                    dj = j+ny
                    if 0<= di < rows and 0<=dj<cols:
                        if grid[di][dj] ==2147483647:
                            
                            grid[di][dj] = dist +1
                            q.append(((di,dj),dist+1))
                        elif grid[di][dj] == 0 and  grid[di][dj] == -1:
                            continue

