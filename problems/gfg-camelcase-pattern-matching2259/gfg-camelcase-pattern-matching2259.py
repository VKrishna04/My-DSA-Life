#User function Template for python3

class Solution:
    def pascalCase(self,arr,pat):
        output = []
        for word in arr:
            curr = ''
            for char in word:
                if char in 'QWERTYUIOPASDFGHJKLZXCVBNM':
                    curr += char
            if pat in curr[:len(pat)]:
                output.append(word)
        return output