class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] == 0:
                    continue
                matrix[i][j] = 1+ min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])

        return sum(sum(row) for row in matrix)