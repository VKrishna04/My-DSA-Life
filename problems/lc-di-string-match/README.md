# DI String Match

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-di-string-match` |
| Topics | Array, Two Pointers, String, Greedy |
| Solved | 2024-10-21 |
| Runtime | 3 ms (beats 72%) |
| Memory | 17.6 MB (beats 100%) |

## Problem Statement

A permutation `perm` of `n + 1` integers of all the integers in the range `[0, n]` can be represented as a string `s` of length `n` where:

	- `s[i] == 'I'` if `perm[i] < perm[i + 1]`, and

	- `s[i] == 'D'` if `perm[i] > perm[i + 1]`.

Given a string `s`, reconstruct the permutation `perm` and return it. If there are multiple valid permutations perm, return **any of them**.

 

**Example 1:**

**Input:** s = "IDID"
**Output:** [0,4,1,3,2]
**Example 2:**

**Input:** s = "III"
**Output:** [0,1,2,3]
**Example 3:**

**Input:** s = "DDI"
**Output:** [3,2,0,1]

 

**Constraints:**

	- `1 <= s.length <= 105`

	- `s[i]` is either `'I'` or `'D'`.

## Solutions

```Python3
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        output = []
        d = len(s)
        i = 0
        for char in s:
            if char == "D":
                output.append(d)
                d -= 1
                continue
            output.append(i)
            i += 1
        # output.append(i)
        output.append(d)
        return output
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(n)$, where $n$ is the length of string `s`. The algorithm performs a single pass over the string.
*   **Space Complexity:** $O(n)$ to store the result list. The auxiliary space is $O(1)$.

### 2. Correctness
The solution is **correct**. It greedily picks the smallest available number for "I" and the largest for "D," ensuring the next available number in the remaining range will always satisfy the condition. 
*   **Edge Cases:** Handles single-character strings and strings with only "I"s or "D"s correctly. The remaining `i` and `d` will always be equal at the end, satisfying the final $n+1$ element requirement.

### 3. Optimization
**Pre-allocation:** Instead of using `append()`, which involves dynamic resizing overhead, pre-allocate the list:
```python
res = [0] * (len(s) + 1)
# Assign by index in the loop
```
Additionally, the `continue` is redundant; an `else` block is cleaner.

### 4. Key Algorithmic Pattern
**Two Pointers / Greedy:** It maintains two boundaries (low and high) and greedily consumes the boundary that guarantees the current constraint is met regardless of future characters.
