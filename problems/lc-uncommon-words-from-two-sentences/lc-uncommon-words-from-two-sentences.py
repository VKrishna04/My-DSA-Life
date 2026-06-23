from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        words = s1.split() + s2.split()
        count = Counter(words)
        return [word for word in count if count[word] == 1]