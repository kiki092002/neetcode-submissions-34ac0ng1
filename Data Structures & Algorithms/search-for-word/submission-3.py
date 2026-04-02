class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def backtrack(row, col, i):
            # Base case: last character matched
            if i == len(word) - 1:
                return board[row][col] == word[i]

            # If current cell matches word[i]
            if board[row][col] != word[i]:
                return False

            visited[row][col] = True

            # Explore 4 directions
            for dr, dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    if backtrack(nr, nc, i + 1):
                        return True

            visited[row][col] = False  # backtrack
            return False

        # Try starting from each cell
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        return False
