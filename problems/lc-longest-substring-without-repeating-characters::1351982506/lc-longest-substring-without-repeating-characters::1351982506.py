class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 1
        if s is "":
            return 0
        for i in range(len(s)):
            st = ""
            for ch in s[i:]:
                if ch not in st:
                    st += ch
                    max_length=max(max_length,len(st))
                else:
                    break
        print(max_length)
        return max_length