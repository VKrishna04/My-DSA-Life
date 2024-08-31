class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            x=-x
            neg = True

        I = int(str(x)[::-1])
        if I <= -2**31 or I >= 2**31 - 1:
            return 0
        return I if neg == False else -I
        