# Find the XOR of Numbers Which Appear Twice

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-find-the-xor-of-numbers-which-appear-twice` |
| Topics | Array, Hash Table, Bit Manipulation |
| Solved | 2024-10-19 |
| Runtime | 0 ms (beats 100%) |
| Memory | 16.5 MB (beats 100%) |

## Problem Statement

You are given an array `nums`, where each number in the array appears **either**_ _once_ _or_ _twice.

Return the bitwise_ _`XOR` of all the numbers that appear twice in the array, or 0 if no number appears twice.

 

**Example 1:**

**Input:** nums = [1,2,1,3]

**Output:** 1

**Explanation:**

The only number that appears twice in `nums` is 1.

**Example 2:**

**Input:** nums = [1,2,3]

**Output:** 0

**Explanation:**

No number appears twice in `nums`.

**Example 3:**

**Input:** nums = [1,2,2,1]

**Output:** 3

**Explanation:**

Numbers 1 and 2 appeared twice. `1 XOR 2 == 3`.

 

**Constraints:**

	- `1 <= nums.length <= 50`

	- `1 <= nums[i] <= 50`

	- Each number in `nums` appears either once or twice.

## Hints

<details>
<summary>Hint 1</summary>

The constraints are small. Brute force checking each value in the array.

</details>

## Solutions

```Python3
from functools import reduce
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 0
        result = 0
        for key, value in frequency.items():
            if value == 1:
                result = result ^ key
        return result
```

## AI Review

**Review of Easy Python3 solution for LeetCode 'Find the XOR of Numbers Which Appear Twice'**

1.  **Time Complexity**: O(N), where N is the number of elements in `nums`. The first loop iterates through `nums` once, with average O(1) dictionary operations. The second loop iterates through unique elements (at most N).
    **Space Complexity**: O(N). The `frequency` dictionary stores counts for up to N unique numbers.

2.  **Correctness**: The solution is **correct**. The specific frequency counting logic (`frequency[num] = 0` for the first occurrence, then `+= 1` for subsequent ones) correctly maps numbers appearing *exactly twice* to a `value` of `1` in the dictionary. The `if value == 1` condition correctly identifies and XORs these numbers. No edge cases should fail.

3.  **One Concrete Optimisation**: Use `collections.Counter` for cleaner and more Pythonic frequency counting:
    ```python
    from collections import Counter
    class Solution:
        def duplicateNumbersXOR(self, nums: List[int]) -> int:
            counts = Counter(nums)
            result = 0
            for num, count in counts.items():
                if count == 2: # Explicitly check for count == 2
                    result ^= num
            return result
    ```
    This maintains O(N) time/space complexity but improves code readability and reduces custom logic for frequency tracking.

4.  **Key Algorithmic Pattern**:
    *   **Frequency Counting**: Using a hash map (dictionary) to track element occurrences.
    *   **Bitwise XOR**: Employing the XOR operator to combine the identified numbers, leveraging its properties for aggregation.
