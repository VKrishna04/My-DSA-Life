# Largest Number

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-largest-number` |
| Topics | Array, String, Greedy, Sorting |
| Solved | 2024-10-21 |
| Runtime | 3 ms (beats 63%) |
| Memory | 16.4 MB (beats 100%) |

## Problem Statement

Given a list of non-negative integers `nums`, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

**Example 1:**

**Input:** nums = [10,2]
**Output:** "210"

**Example 2:**

**Input:** nums = [3,30,34,5,9]
**Output:** "9534330"

 

**Constraints:**

	- `1 <= nums.length <= 100`

	- `0 <= nums[i] <= 109`

## Solutions

```Python3
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        nums.sort(key=cmp_to_key(compare))
        
        result = ''.join(nums)
        
        return '0' if result[0] == '0' else result

```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(N \log N \cdot K)$, where $N$ is the number of integers and $K$ is the average number of digits. String concatenation and comparison inside the sort both take $O(K)$.
*   **Space Complexity:** $O(N \cdot K)$ to store the list of string representations.

### 2. Correctness
The solution is **correct**. It handles the primary edge case where the input contains multiple zeros (e.g., `[0, 0]`). The final check `result[0] == '0'` ensures that instead of returning `"00"`, it returns `"0"`.

### 3. Optimization
In Python, **custom key classes** are often faster than `cmp_to_key`. You can wrap strings in a class that overrides the `__lt__` method:
```python
class LargerNum(str):
    def __lt__(x, y):
        return x + y > y + x  # Reversed for descending sort

nums.sort(key=LargerNum)
```
This integrates more natively with Timsort and avoids the overhead of the comparison wrapper function.

### 4. Key Algorithmic Pattern
**Greedy Algorithm via Custom Sorting.** The problem relies on the transitive property of the concatenation comparison ($A+B > B+A$), ensuring that a local optimal choice (sorting strings by this rule) leads to the global maximum.
