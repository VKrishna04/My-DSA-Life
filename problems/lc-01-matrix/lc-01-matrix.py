from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return
        q = deque()
        rows, cols = len(mat), len(mat[0])
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = -1
        
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= rows or nc < 0 or nc >=cols or mat[nr][nc] != -1:
                    continue
                
                mat[nr][nc] = mat[r][c]+1
                q.append((nr, nc))
        return mat