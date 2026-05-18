class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_side = 0
        for i in range(len(matrix)):
            matrix[i][0] = int(matrix[i][0])
            max_side = max(max_side, matrix[i][0])
        for j in range(len(matrix[0])):
            matrix[0][j] = int(matrix[0][j])
            max_side = max(max_side, matrix[0][j])

        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] == '0':
                    continue
                matrix[i][j] = 1 + min(int(matrix[i-1][j]), int(matrix[i-1][j-1]), int(matrix[i][j-1]))
                max_side = max(max_side, matrix[i][j])
        return max_side ** 2