# Minimize Maximum Pair Sum in Array

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-minimize-maximum-pair-sum-in-array` |
| Topics | Array, Two Pointers, Greedy, Sorting |
| Solved | 2025-08-10 |
| Runtime | 930 ms (beats 5.055999999999983%) |
| Memory | 31.4 MB (beats 99.5872%) |

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

### 1. Complexity
*   **Time Complexity:** $O(n \log n)$ due to the `nums.sort()` operation. The subsequent two-pointer traversal is $O(n)$.
*   **Space Complexity:** $O(1)$ or $O(n)$ depending on the sorting implementation (Python's Timsort uses $O(n)$ auxiliary space in the worst case).

### 2. Correctness
The solution is **correct**. To minimize the maximum pair sum, you must pair the smallest remaining element with the largest remaining element (Greedy strategy). 
*   **Edge Cases:** The code correctly handles the minimum array size ($n=2$), duplicate values, and already sorted inputs.

### 3. Optimization
If the range of numbers is small (e.g., values $\le 10^5$), you can use **Counting Sort** (Bucket Sort) to achieve **$O(n + \text{max\_val})$** time complexity, which is faster than $O(n \log n)$ for large $n$.

### 4. Key Algorithmic Pattern
*   **Greedy Algorithm:** Making the locally optimal choice (pairing smallest with largest) to achieve a global optimum.
*   **Two Pointers:** Converging from both ends of a sorted array to process pairs.
