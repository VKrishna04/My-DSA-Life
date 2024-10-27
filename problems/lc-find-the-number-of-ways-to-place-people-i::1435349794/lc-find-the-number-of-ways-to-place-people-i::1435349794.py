class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: (x[0],-x[1]))
        output = 0
        l = len(points)
        for i in range(l):
            start = points[i][0]
            end = float("-inf")
            for j in range(i+1,l):
                if points[j][1] > points[i][1]:
                    continue
                if points[j][1] > end:
                    end = points[j][1]
                    output += 1
        return output