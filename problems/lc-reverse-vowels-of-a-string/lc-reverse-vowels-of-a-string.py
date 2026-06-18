class Solution:
    def reverseVowels(self, s: str) -> str:
        letters = list(s)
        l = 0
        r = len(letters)-1
        vow = set('aeiouAEIOU')

        while l < r:
            if not letters[l] in vow:
                l += 1
            elif not letters[r] in vow:
                r -= 1
            else:
                letters[l], letters[r] = letters[r], letters[l]
                l += 1
                r -= 1
                
        return ''.join(letters)