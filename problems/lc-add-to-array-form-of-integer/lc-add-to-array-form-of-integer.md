# Add to Array-Form of Integer

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-add-to-array-form-of-integer` |
| Topics | Array, Math |
| Solved | 2024-10-18 |
| Runtime | 5 ms (beats 81.90090000000001%) |
| Memory | 17.1 MB (beats 100%) |

## Problem Statement

The **array-form** of an integer `num` is an array representing its digits in left to right order.

	- For example, for `num = 1321`, the array form is `[1,3,2,1]`.

Given `num`, the **array-form** of an integer, and an integer `k`, return _the **array-form** of the integer_ `num + k`.

 

**Example 1:**

**Input:** num = [1,2,0,0], k = 34
**Output:** [1,2,3,4]
**Explanation:** 1200 + 34 = 1234

**Example 2:**

**Input:** num = [2,7,4], k = 181
**Output:** [4,5,5]
**Explanation:** 274 + 181 = 455

**Example 3:**

**Input:** num = [2,1,5], k = 806
**Output:** [1,0,2,1]
**Explanation:** 215 + 806 = 1021

 

**Constraints:**

	- `1 <= num.length <= 104`

	- `0 <= num[i] <= 9`

	- `num` does not contain any leading zeros except for the zero itself.

	- `1 <= k <= 104`

## Solutions

```Python3
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num[-1] += k
        if len(num) > 1:
            for i in range(len(num)-1,0,-1):
                if num[i] >= 10:
                    num[i-1] += num[i] // 10
                    num[i] = num[i] % 10

        while num[0] >= 10:
            num = [num[0] // 10] + num
            num[1] = num[1] % 10
        return num
```

## AI Review

### Analysis

**1. Complexity**
*   **Time:** $O(N \cdot \log_{10}K)$, where $N$ is the length of `num`. The `while` loop prepends to the list (`[val] + num`), which is an $O(N)$ operation inside a loop running $O(\log_{10}K)$ times.
*   **Space:** $O(N + \log_{10}K)$ to store the resulting digits.

**2. Correctness**
The logic is **correct**. It successfully handles:
*   Standard carries.
*   Large $K$ values that extend the array length (handled by the `while` loop).
*   Single-element arrays.

**3. Concrete Optimization**
Replace the inefficient prepending (`num = [new_digit] + num`) with `num.append()` and a final `reverse()`. Prepending creates a new list every iteration, leading to $O(N^2)$ behavior in some languages. In the current logic, you can also simplify by processing $K$ directly:
```python
for i in range(len(num) - 1, -1, -1):
    k, num[i] = divmod(num[i] + k, 10)
while k:
    num.insert(0, k % 10)
    k //= 10
```
*(Note: `insert(0, ...)` is still $O(N)$; for true $O(N)$ efficiency, use a new list and reverse it.)*

**4. Key Algorithmic Pattern**
**Manual Carry Simulation** (Elementary School Addition).
