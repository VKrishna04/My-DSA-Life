# Majority Element II

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-majority-element-ii` |
| Topics | Array, Hash Table, Sorting, Counting |
| Solved | 2024-11-10 |
| Runtime | 3 ms (beats 92.829%) |
| Memory | 18.3 MB (beats 100%) |

## Problem Statement

Given an integer array of size `n`, find all elements that appear more than `&lfloor; n/3 &rfloor;` times.

 

**Example 1:**

**Input:** nums = [3,2,3]
**Output:** [3]

**Example 2:**

**Input:** nums = [1]
**Output:** [1]

**Example 3:**

**Input:** nums = [1,2]
**Output:** [1,2]

 

**Constraints:**

	- `1 <= nums.length <= 5 * 104`

	- `-109 <= nums[i] <= 109`

 

**Follow up:** Could you solve the problem in linear time and in `O(1)` space?

## Hints

<details>
<summary>Hint 1</summary>

Think about the possible number of elements that can appear more than ⌊ n/3 ⌋ times in the array.

</details>

<details>
<summary>Hint 2</summary>

It can be at most two. Why?

</details>

<details>
<summary>Hint 3</summary>

Consider using Boyer-Moore Voting Algorithm, which is efficient for finding elements that appear more than a certain threshold.

</details>

## Solutions

```Python3
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [num for num, count in Counter(nums).items() if count > len(nums)/3]
```

## AI Review

**1. Complexity**
*   **Time:** $O(n)$ — Building the hash map takes linear time.
*   **Space:** $O(n)$ — In the worst case (all unique elements), the `Counter` stores $n$ entries.

**2. Correctness**
The solution is **correct** and handles all edge cases, including empty arrays, single elements, and arrays with no majority element. Since an element must appear $> n/3$ times, there can be at most **two** such elements.

**3. Optimization**
To achieve **$O(1)$ space** (as often requested in this problem's follow-up), use the **Boyer-Moore Voting Algorithm** extended for two candidates:
1. Maintain two potential candidates and two counters.
2. Iterate through `nums`:
   - If a number matches a candidate, increment its counter.
   - If a counter is zero, set the current number as the new candidate.
   - Otherwise, decrement both counters.
3. Perform a second pass to verify the candidates actually exceed the $n/3$ threshold.

**4. Key Algorithmic Pattern**
**Frequency Counting / Hashing.** (The optimized version uses **Boyer-Moore Voting**).
