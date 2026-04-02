class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(i,j):
            board[i][j] ='#'
            for nr,nc in directions:
                dr = i+nr
                dc = j+nc
                if 0<=dr<rows and 0<= dc<cols and board[dr][dc] =='O':
                    dfs(dr,dc)
        for i in range(rows):
            for j in range(cols):
                if i==0 or j == 0 or i == rows-1 or j == cols-1:
                    if board[i][j] == 'O':
                        dfs(i,j)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] ='X'
                if board[i][j] =='#':
                    board[i][j] ='O'
    