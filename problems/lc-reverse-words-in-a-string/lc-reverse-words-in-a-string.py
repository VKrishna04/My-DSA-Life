class Solution:
    def reverseWords(self, s: str) -> str:
        words = list(s.strip().split())
        words = [words[0]]+[word+' ' for word in words[1:]]
        return ''.join(words[::-1])