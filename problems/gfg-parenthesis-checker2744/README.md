# Parenthesis Checker

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-parenthesis-checker2744` |
| Topics | Strings, Stack, STL, Data Structures |
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
