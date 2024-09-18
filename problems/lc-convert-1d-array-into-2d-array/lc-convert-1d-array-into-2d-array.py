class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        arr = []
        if len(original) != m*n:
            return arr
        for i in range(m):
            arr.append(original[n * i:n * (i + 1)])
        return arr