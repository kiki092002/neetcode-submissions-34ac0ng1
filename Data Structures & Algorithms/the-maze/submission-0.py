class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        queue = deque([start])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        visited = set()
        visited.add((start[0],start[1]))
        while queue:
            curr_r,curr_c = queue.popleft()
            if curr_r == destination[0] and curr_c == destination[1]:
                return True
            for dr,dc in directions:
                nr,nc = curr_r,curr_c
                while self.couldPassBy(maze,nr+dr,nc+dc):
                    nr +=dr
                    nc +=dc
                
                if (nr,nc) not in visited and self.couldPassBy(maze,nr,nc):
                    visited.add((nr,nc))
                    queue.append([nr,nc])

        return False

    def couldPassBy(self,maze,r,c):
        return 0 <= r< len(maze) and 0<=c <len(maze[0]) and maze[r][c] ==0