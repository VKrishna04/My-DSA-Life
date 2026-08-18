class Solution:
    def rotateMatrix(self, mat):
        mat[:] = mat[::-1]

        for row in mat:
            row[:] = row[::-1]

        return mat
        