class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_word = ""
        for char1, char2 in zip(word1, word2):
            new_word += char1 + char2
        if len(word1) < len(word2):
            new_word += word2[len(word1):]
        else:
            new_word += word1[len(word2):]
        return new_word