# Construct Smallest Number From DI String

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-construct-smallest-number-from-di-string` |
| Topics | String, Backtracking, Stack, Greedy |
| Solved | 2024-10-24 |
| Runtime | 0 ms (beats 100%) |
| Memory | 16.7 MB (beats 100%) |

## Problem Statement

You are given a **0-indexed** string `pattern` of length `n` consisting of the characters `'I'` meaning **increasing** and `'D'` meaning **decreasing**.

A **0-indexed** string `num` of length `n + 1` is created using the following conditions:

	- `num` consists of the digits `'1'` to `'9'`, where each digit is used **at most** once.

	- If `pattern[i] == 'I'`, then `num[i] < num[i + 1]`.

	- If `pattern[i] == 'D'`, then `num[i] > num[i + 1]`.

Return _the lexicographically **smallest** possible string _`num`_ that meets the conditions._

 

**Example 1:**

**Input:** pattern = "IIIDIDDD"
**Output:** "123549876"
**Explanation:
**At indices 0, 1, 2, and 4 we must have that num[i] < num[i+1].
At indices 3, 5, 6, and 7 we must have that num[i] > num[i+1].
Some possible values of num are "245639871", "135749862", and "123849765".
It can be proven that "123549876" is the smallest possible num that meets the conditions.
Note that "123414321" is not possible because the digit '1' is used more than once.

**Example 2:**

**Input:** pattern = "DDD"
**Output:** "4321"
**Explanation:**
Some possible values of num are "9876", "7321", and "8742".
It can be proven that "4321" is the smallest possible num that meets the conditions.

 

**Constraints:**

	- `1 <= pattern.length <= 8`

	- `pattern` consists of only the letters `'I'` and `'D'`.

## Hints

<details>
<summary>Hint 1</summary>

With the constraints, could we generate every possible string?

</details>

<details>
<summary>Hint 2</summary>

Yes we can. Now we just need to check if the string meets all the conditions.

</details>

## Solutions

```Python3
# class Solution:
#     def smallestNumber(self, pattern: str) -> str:
#         output = [1]
#         pos = [_ for _ in range(2,11)]
#         for char in pattern:
#             if char == "D":
#                 i = min([x for x in pos if x <= output[-1]])
#                 pos.remove(i)
#                 output.append(i)
#             if char == 'I':
#                 i = min([x for x in pos if x > output[-1]])
#                 pos.remove(i)
#                 output.append(i)

#         return "".join(map(str, output))

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        dp = [1]
        temp = []
        i = 2
        for char in pattern:
            if char == 'I':
                while temp:
                    dp.append(temp.pop())
                dp.append(i)
                i += 1
            else:
                temp.append(dp.pop())
                dp.append(i)
                i += 1
        while temp:
            dp.append(temp.pop())
        s = ""
        for i in dp:
            s+= str(i)
        return s
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(n)$, where $n$ is the length of the pattern (max 8). The code iterates through the string once, and stack operations are $O(1)$.
*   **Space Complexity:** $O(n)$ to store the `dp` and `temp` stacks and the final string.

### 2. Correctness
The logic is **correct**. It greedily assigns the next available digit and uses a temporary stack to reverse sequences during "D" (decreasing) segments, ensuring the lexicographically smallest result. Since the pattern length is $\le 8$, the digits stay within the 1-9 range.

### 3. Concrete Optimisation
Replace the string concatenation loop with `"".join(map(str, dp))` to avoid $O(n^2)$ overhead from string immutability. Additionally, the logic can be simplified:
```python
res, stack = [], []
for i in range(len(pattern) + 1):
    stack.append(str(i + 1))
    if i == len(pattern) or pattern[i] == 'I':
        while stack:
            res.append(stack.pop())
return "".join(res)
```
This version removes the need for two separate stacks and complex `if/else` logic.

### 4. Key Algorithmic Pattern
**Greedy with a Stack.** The stack reverses the order of digits during decreasing sequences to satisfy the "D" condition while keeping digits as small as possible.
