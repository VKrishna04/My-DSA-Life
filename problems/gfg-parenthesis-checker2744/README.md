# Parenthesis Checker

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-parenthesis-checker2744` |
| Topics | String, Stack, Stl, Hash Table |
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

## AI Review

### Review
1. **Complexity**:
- **Time**: $O(n)$ where $n$ is the length of the string. You traverse the string once.
- **Space**: $O(n)$ in the worst case (e.g., all opening brackets `((((`), which matches your recurring flag for high space usage.

2. **Correctness**:
The logic is sound. It handles empty strings, unmatched closing brackets, and mismatched pairs correctly. However, it lacks an **early exit**. For a string like `)]...[1000 more chars]`, your code processes the entire string instead of returning `False` immediately.

3. **Optimisation**:
Remove the `ope` and `clo` counters. They are redundant because `if stack` and the final `if stack:` check already capture whether brackets are balanced. Additionally, use an **early return** inside the loop: if a closing bracket doesn't match the stack top or the stack is empty, return `False` immediately. This improves average-case performance.

4. **Pattern**:
**Stack** (Last-In-First-Out). Brackets must be closed in the exact reverse order they were opened.

###
