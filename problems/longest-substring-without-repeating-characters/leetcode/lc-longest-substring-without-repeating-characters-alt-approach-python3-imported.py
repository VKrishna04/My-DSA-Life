class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # max_length = 1
        # if s is "":
        #     return 0
        # for i in range(len(s)):
        #     st = ""
        #     for ch in s[i:]:
        #         if ch not in st:
        #             st += ch
        #             max_length=max(max_length,len(st))
        #         else:
        #             break
        # print(max_length)
        # return max_length

        start = 0  
        max_length = 0  
        seen_chars = set()  

        for end in range(len(s)):
            while s[end] in seen_chars:
                seen_chars.remove(s[start])
                start += 1
            
            seen_chars.add(s[end])
            
            max_length = max(max_length, end - start + 1)

        return max_length