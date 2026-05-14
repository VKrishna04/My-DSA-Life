import sys
sys.setrecursionlimit(2000)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        if not board: return
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return

            board[r][c] = 'T'

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for c in range(cols):
            if board[0][c] == 'O': dfs(0, c)
            if board[rows - 1][c] == 'O': dfs(rows - 1, c)
            
        for r in range(1, rows - 1):
            if board[r][0] == 'O': dfs(r, 0)
            if board[r][cols - 1] == 'O': dfs(r, cols - 1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'