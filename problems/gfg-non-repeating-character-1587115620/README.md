# Non Repeating Character

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-non-repeating-character-1587115620` |
| Topics | Hash Table, String |
| Solved | 2026-06-24 |

## Problem Statement

Given a string **s** consisting of **lowercase **English** **Letters. return the first non-repeating character in **s**. If there is no non-repeating character, return **'$'**.

**Examples:**

**Input: **s = "geeksforgeeks"
**Output: **'f'**
Explanation: **In the given string, 'f' is the first character in the string which does not repeat.
**Input: **s = "racecar"
**Output: **'e'
**Explanation: **In the given string, 'e' is the only character in the string which does not repeat.
**Input: **s = "aabbccc"
**Output: '$'**
**Explanation: **All the characters in the given string are repeating.
**Constraints:**
1 &le; s.size() &le; 105

## Solutions

```python3
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
```
