# Parenthesis Checker

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-parenthesis-checker2744` |
| Topics | String, Stack, Stl |
| Solved | 2026-06-24 |

## Problem Statement

Given a string **s**, composed of different combinations of '(' , ')', '{', '}', '[', ']'. Determine whether the Expression is **balanced **or not.
An expression is balanced if:

- Each opening bracket has a corresponding closing bracket of the same type.

- Opening brackets must be closed in the correct order.

**Examples :**

**Input: **s = "[{()}]"
**Output:** true
**Explanation: **All the brackets are well-formed.
**Input: **s = "[()()]{}"
**Output:** true
**Explanation: **All the brackets are well-formed.

**Input:** s = "([]"
**Output: **false
**Explanation: **The expression is not balanced as there is a missing ')' at the end.

**Input:** s = "([{]})"
**Output: **false
**Explanation: **The expression is not balanced as there is a closing ']' before the closing '}'.

**Constraints:**
1 &le; s.size() &le; 106
s[i] &isin; {'{', '}', '(', ')', '[', ']'}

## Solutions

```python3
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
```
