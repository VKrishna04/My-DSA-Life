# Minimize Maximum Pair Sum in Array

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-minimize-maximum-pair-sum-in-array` |
| Topics | Array, Two Pointers, Greedy, Sorting |
| Solved | 2025-08-10 |
| Runtime | 978 ms (beats 5.055999999999983%) |
| Memory | 30.7 MB (beats 99.6904%) |

## Problem Statement

The **pair sum** of a pair `(a,b)` is equal to `a + b`. The **maximum pair sum** is the largest **pair sum** in a list of pairs.




	- For example, if we have pairs `(1,5)`, `(2,3)`, and `(4,4)`, the **maximum pair sum** would be `max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8`.



Given an array `nums` of **even** length `n`, pair up the elements of `nums` into `n / 2` pairs such that:




	- Each element of `nums` is in **exactly one** pair, and

	- The **maximum pair sum **is **minimized**.



Return _the minimized **maximum pair sum** after optimally pairing up the elements_.



 


**Example 1:**




**Input:** nums = [3,5,2,3]
**Output:** 7
**Explanation:** The elements can be paired up into pairs (3,3) and (5,2).
The maximum pair sum is max(3+3, 5+2) = max(6, 7) = 7.


**Example 2:**




**Input:** nums = [3,5,4,2,4,6]
**Output:** 8
**Explanation:** The elements can be paired up into pairs (3,5), (4,4), and (6,2).
The maximum pair sum is max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8.


 


**Constraints:**




	- `n == nums.length`

	- `2 <= n <= 105`

	- `n` is **even**.

	- `1 <= nums[i] <= 105`

## Hints

<details>
<summary>Hint 1</summary>

Would sorting help find the optimal order?

</details>

<details>
<summary>Hint 2</summary>

Given a specific element, how would you minimize its specific pairwise sum?

</details>

## Solutions

### Alt approach (Python3) — imported

Submission #1730457343

```Python3
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        res = 0

        while i < j:
            res = max(res, nums[i] + nums[j])
            i += 1
            j -= 1
        
        return res
```

## AI Review

### Analysis

**1. Complexity**
*   **Time:** $O(N \log N)$ due to the sorting step. The subsequent linear pass is $O(N)$.
*   **Space:** $O(N)$ to store the `ans` list. (Note: Python's `sort()` also uses up to $O(N)$ auxiliary space).

**2. Correctness**
The logic is correct. By pairing the smallest available number with the largest, you greedily minimize the potential growth of the maximum sum. 
*   **Edge Cases:** The code handles the minimum constraint (even length $\ge 2$) correctly.
*   **Note:** Remove `print(nums)` in production to avoid $O(N)$ I/O overhead.

**3. Optimization**
**Space Optimization:** Instead of storing all sums in a list `ans` ($O(N)$ space) and then calling `max()`, update a running maximum variable. This reduces auxiliary space to $O(1)$ (excluding sort space).

```python
max_sum = 0
for i in range(len(nums) // 2):
    max_sum = max(max_sum, nums[i] + nums[-i - 1])
return max_sum
```

**4. Key Algorithmic Pattern**
*   **Greedy Algorithm:** Making the locally optimal choice (smallest + largest) leads to the global optimum.
*   **Two Pointers:** Implicitly used here via indices `i` and `len(nums)-1-i`.
