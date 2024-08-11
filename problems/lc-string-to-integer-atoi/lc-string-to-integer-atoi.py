class Solution:
    def myAtoi(self, s: str) -> int:
        neg = False
        num = 0
        if not s:
            return 0
        s = s.lstrip()
        if not s:
            return 0
        if s[0] is '-':
            neg = True
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        if not s:
            return 0
        for i in range(len(s)):
            if s[i] != '0':
                s = s[i:]
                if not s:
                    return 0
                break
            
        for i, c in enumerate(s):
            if '0' <= c <= '9':
                num = num * 10 + (ord(c) - ord('0'))
            
            else:
                break
        

        if neg:
            num = -num
        
        if num > (2**31 -1):
            num = 2**31 -1
        elif num < -2**31:
            num = -2**31
        
        return num
            
            