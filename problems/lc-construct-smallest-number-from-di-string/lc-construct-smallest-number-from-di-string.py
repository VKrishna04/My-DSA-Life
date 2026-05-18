# class Solution:
#     def smallestNumber(self, pattern: str) -> str:
#         output = [1]
#         pos = [_ for _ in range(2,11)]
#         for char in pattern:
#             if char == "D":
#                 i = min([x for x in pos if x <= output[-1]])
#                 pos.remove(i)
#                 output.append(i)
#             if char == 'I':
#                 i = min([x for x in pos if x > output[-1]])
#                 pos.remove(i)
#                 output.append(i)

#         return "".join(map(str, output))

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        dp = [1]
        temp = []
        i = 2
        for char in pattern:
            if char == 'I':
                while temp:
                    dp.append(temp.pop())
                dp.append(i)
                i += 1
            else:
                temp.append(dp.pop())
                dp.append(i)
                i += 1
        while temp:
            dp.append(temp.pop())
        s = ""
        for i in dp:
            s+= str(i)
        return s