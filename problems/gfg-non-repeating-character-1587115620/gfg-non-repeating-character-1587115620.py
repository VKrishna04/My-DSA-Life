class Solution:
    def nonRepeatingChar(self,s):
        # dic = {char : 0 for char in 'abcdefghijklmnopqrstuvwxyz'}
        
        # for char in s:
        #     dic[char] += 1
            
        # result = [k for k, v in dic.items() if v == 1]
        # # print(result)
        
        # if len(result) == 0:
        #     return '$'
        
        # if len(result) == 1: 
        #     return result[0]
        
        # for char in s:
        #     if char in result:
        #         return char
        
        dic = {}
        for char in s:
            dic[char] = dic.get(char, 0) + 1
        
        for char in s:
            if dic[char] == 1:
                return char
        return '$'