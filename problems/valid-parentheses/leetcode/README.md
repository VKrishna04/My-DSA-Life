# Valid Parentheses

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-valid-parentheses` |
| Topics | String, Stack |
| Solved | 2024-10-20 |
| Runtime | 4 ms (beats 12%) |
| Memory | 16.6 MB (beats 100%) |

## Problem Statement

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

	- Open brackets must be closed by the same type of brackets.

	- Open brackets must be closed in the correct order.

	- Every close bracket has a corresponding open bracket of the same type.

 

**Example 1:**

**Input:** s = "()"

**Output:** true

**Example 2:**

**Input:** s = "()[]{}"

**Output:** true

**Example 3:**

**Input:** s = "(]"

**Output:** false

**Example 4:**

**Input:** s = "([])"

**Output:** true

**Example 5:**

**Input:** s = "([)]"

**Output:** false

 

**Constraints:**

	- `1 <= s.length <= 104`

	- `s` consists of parentheses only `'()[]{}'`.

## Hints

<details>
<summary>Hint 1</summary>

Use a stack of characters.

</details>

<details>
<summary>Hint 2</summary>

When you encounter an opening bracket, push it to the top of the stack.

</details>

<details>
<summary>Hint 3</summary>

When you encounter a closing bracket, check if the top of the stack was the opening for it. If yes, pop it from the stack. Otherwise, return false.

</details>

## Solutions

```Python3
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_bracket = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in matching_bracket.values():
                stack.append(char)
            elif char in matching_bracket:
                if stack and stack[-1] == matching_bracket[char]:
                    stack.pop()
                else:
                    return False  
            else:
                return False
        return not stack
```

## AI Review

### Analysis

1. **Complexity**:
   - **Time**: $O(N)$, where $N$ is the length of the string. We iterate through the string once, and dictionary/stack operations are $O(1)$.
   - **Space**: $O(N)$ in the worst case (e.g., a string of all opening brackets).

2. **Correctness**:
   The logic is robust. It correctly handles:
   - **Empty strings**: Returns `True`.
   - **Mismatched types**: E.g., `(]`.
   - **Incorrect order**: E.g., `([)]`.
   - **Unclosed brackets**: E.g., `((`.
   - **Extra closing brackets**: E.g., `())`.

3. **Concrete Optimisation**:
   **Early Exit**: A valid string must have an even length. Add a check at the beginning:
   ```python
   if len(s) % 2 != 0: return False
   ```
   This provides an $O(1)$ rejection for many invalid inputs. Additionally, `matching_bracket.values()` creates a view; for maximum efficiency, map **opening** brackets to **closing** brackets to simplify the `if` logic.

4. **Key Algorithmic Pattern**:
   **Stack (LIFO)**: The stack ensures that the most recently opened bracket is the first one closed, which is the core requirement for nested structures.
