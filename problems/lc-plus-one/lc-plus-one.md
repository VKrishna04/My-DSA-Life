# Plus One

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-plus-one` |
| Topics | Array, Math |
| Solved | 2024-10-18 |
| Runtime | 0 ms (beats 100%) |
| Memory | 16.7 MB (beats 100%) |

## Problem Statement

You are given a **large integer** represented as an integer array `digits`, where each `digits[i]` is the `ith` digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading `0`'s.

Increment the large integer by one and return _the resulting array of digits_.

 

**Example 1:**

**Input:** digits = [1,2,3]
**Output:** [1,2,4]
**Explanation:** The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

**Example 2:**

**Input:** digits = [4,3,2,1]
**Output:** [4,3,2,2]
**Explanation:** The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

**Example 3:**

**Input:** digits = [9]
**Output:** [1,0]
**Explanation:** The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

 

**Constraints:**

	- `1 <= digits.length <= 100`

	- `0 <= digits[i] <= 9`

	- `digits` does not contain any leading `0`'s.

## Solutions

```Python3
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        if len(digits) > 1:
            for i in range(len(digits)-1,0,-1):
                if digits[i] == 10:
                    digits[i] = 0
                    digits[i-1] += 1

        if digits[0] == 10:
            digits[0] = 0
            digits = [1] + digits
        return digits
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(n)$, where $n$ is the number of digits. In the worst case (e.g., `[9,9,9]`), the code traverses the entire array once.
*   **Space Complexity:** $O(n)$. While mostly in-place, the operation `[1] + digits` creates a new list of size $n+1$ in the worst case.

### 2. Correctness
The code is **correct**. It handles standard cases, single-digit inputs (like `[9]`), and carry propagation through the entire array. One minor redundancy is the `if len(digits) > 1` check, as the logic could be unified, but it does not break functionality.

### 3. Optimization
**Early Return:** You can exit the loop as soon as no carry is generated. This avoids unnecessary iterations.

```python
for i in range(len(digits) - 1, -1, -1):
    digits[i] += 1
    if digits[i] < 10:
        return digits # Optimization: stop early
    digits[i] = 0
return [1] + digits
```

### 4. Key Algorithmic Pattern
**Schoolbook Addition (Carry Propagation):** Iterating from the least significant digit to the most significant, mimicking manual long-addition.
