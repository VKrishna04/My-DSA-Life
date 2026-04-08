class Solution:
    def myAtoi(self, s):
        s = s.strip()
        if not s:
            return 0
        
        sign = 1
        i = 0
        
        if s[i] in ['+', '-']:
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        num = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            num = num * 10 + digit
            i += 1
        
        return sign * num