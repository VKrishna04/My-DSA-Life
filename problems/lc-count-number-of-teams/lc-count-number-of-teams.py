class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0

        for j in range(1, len(rating) - 1):
            ls = 0
            lb = 0
            for i in range(j):
                if rating[i] < rating[j]:
                    ls += 1
                if rating[i] > rating[j]:
                    lb += 1
            rs = 0
            rb = 0
            for k in range(j + 1, len(rating)):
                if rating[j] < rating[k]:
                    rb += 1
                if rating[j] > rating[k]:
                    rs += 1
            count += (ls * rb) + (lb * rs)

        return count
