class Solution:
    def isBalanced(self, s):
        stack = []
        dic = {']':'[', '}':'{', ')':'('}
        ope = 0
        clo = 0
        for char in s:
            if char in dic.values():
                ope += 1
                stack.append(char)
            if char in dic.keys():
                clo += 1
                if stack and dic[char] == stack[-1]:
                    stack.pop()
        if ope != clo or stack:
            return False
        return True