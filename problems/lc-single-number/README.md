# Single Number

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-single-number` |
| Topics | Array, Bit Manipulation |
| Solved | 2024-10-19 |
| Solve Time | 16m 50s |
| Runtime | 13 ms (beats 11.494600000000016%) |
| Memory | 18.9 MB (beats 100%) |

## Problem Statement

Given a **non-empty** array of integers `nums`, every element appears _twice_ except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

**Example 1:**

**Input:** nums = [2,2,1]

**Output:** 1

**Example 2:**

**Input:** nums = [4,1,2,1,2]

**Output:** 4

**Example 3:**

**Input:** nums = [1]

**Output:** 1

 

**Constraints:**

	- `1 <= nums.length <= 3 * 104`

	- `-3 * 104 <= nums[i] <= 3 * 104`

	- Each element in the array appears twice except for one element which appears only once.

## Solutions

```Python3
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 0
        print(frequency)
        for key, value in frequency.items():
            if value == 0:
                return key
```

## AI Review

### Review of Python3 Solution

**1. Complexity**
*   **Time Complexity:** $O(n)$, where $n$ is the number of elements in `nums`. The list is traversed twice (once to build the map, once to find the key).
*   **Space Complexity:** $O(n)$ to store the dictionary containing unique elements.

**2. Correctness**
*   **Logic:** The code is technically correct for the specific constraint where elements appear exactly twice. By initializing at `0` and incrementing to `1` on the second occurrence, the single number is correctly identified as having a value of `0`.
*   **Edge Cases:** If the input `nums` is empty, the function will implicitly return `None`. However, if any "other" number appears three or more times, the `value == 0` check would fail to identify it correctly.

**3. Optimization**
Use **Bit Manipulation (XOR)**. Since $x \oplus x = 0$ and $x \oplus 0 = x$, XORing all elements together cancels out the pairs, leaving only the single number. This reduces space complexity to **$O(1)$**.
```python
res = 0
for n in nums:
    res ^= n
return res
```

**4. Key Algorithmic Pattern**
**Hash Map (Frequency Counting)**. This approach tracks occurrences to identify elements based on their count.
