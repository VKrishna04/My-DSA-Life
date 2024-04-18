class Solution:
  def scoreOfString(self, s: str) -> int:
    score = 0
    for char in range(len(s)-1):
      score += abs(ord(s[char]) - ord(s[char+1]))
    return score
