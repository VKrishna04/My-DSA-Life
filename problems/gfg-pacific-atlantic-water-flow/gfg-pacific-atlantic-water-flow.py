from collections import deque
class Solution:
    def countCoordinates(self, mat):
        n, m = len(mat), len(mat[0])
        p, a = set(), set()
        pq, aq = deque(), deque()
        for r in range(n):
            pq.append((r, 0)); p.add((r, 0))
            aq.append((r, m-1)); a.add((r, m-1))
        for c in range(m):
            pq.append((0, c)); p.add((0, c))
            aq.append((n-1, c)); a.add((n-1, c))
        while pq:
            r, c = pq.popleft()
            for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in p and mat[nr][nc] >= mat[r][c]:
                    p.add((nr, nc)); pq.append((nr, nc))
        while aq:
            r, c = aq.popleft()
            for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in a and mat[nr][nc] >= mat[r][c]:
                    a.add((nr, nc)); aq.append((nr, nc))
        return len(p & a)