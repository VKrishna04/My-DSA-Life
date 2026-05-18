class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        totalc = 0
        alfa = 26

        for chars, chart in zip(s,t):
            start = ord(chars) - ord('a')
            target = ord(chart) - ord('a')

            forward = (target - start) % alfa
            backward = (start - target) % alfa

            forwardc = sum(nextCost[(start + i) % alfa] for i in range(forward))
            backwardc = sum(previousCost[(start - i) % alfa] for i in range(backward))

            totalc += min(forwardc, backwardc)
        return totalc