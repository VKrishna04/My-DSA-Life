# Max Consecutive Ones

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-max-consecutive-ones` |
| Topics | Array |
| Solved | 2024-02-10 |
| Runtime | 3 ms (beats 60.4658%) |
| Memory | 44.9 MB (beats 100%) |

## Problem Statement

Given a binary array `nums`, return _the maximum number of consecutive _`1`_'s in the array_.

 

**Example 1:**

**Input:** nums = [1,1,0,1,1,1]
**Output:** 3
**Explanation:** The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

**Example 2:**

**Input:** nums = [1,0,1,1,0,1]
**Output:** 2

 

**Constraints:**

	- `1 <= nums.length <= 105`

	- `nums[i]` is either `0` or `1`.

## Hints

<details>
<summary>Hint 1</summary>

You need to think about two things as far as any window is concerned. One is the starting point for the window. How do you detect that a new window of 1s has started? The next part is detecting the ending point for this window.

How do you detect the ending point for an existing window? If you figure these two things out, you will be able to detect the windows of consecutive ones. All that remains afterward is to find the longest such window and return the size.

</details>

## Solutions

```Java
class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int j = 0, result = 0;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                j = 0;
                continue;
            }
            j++;
            result = Math.max(j, result);
        }
        return result;
    }
}
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(n)$, where $n$ is the length of the array. The algorithm performs a single pass through the input.
*   **Space Complexity:** $O(1)$. Only two integer variables (`j`, `result`) are used, regardless of input size.

### 2. Correctness
The solution is **correct** and handles all standard edge cases:
*   **All 0s:** `result` remains 0.
*   **All 1s:** `result` updates every iteration to the full length.
*   **Single Element:** Works correctly for both `[0]` and `[1]`.
*   **Ends with 1:** Because `result` is updated *before* the next iteration/return, the final streak is captured.

### 3. Concrete Optimization
Currently, `Math.max` is called for every `1` in the array. You can reduce the number of comparisons by only updating `result` when a `0` is encountered or at the end of the array. Alternatively, replace `Math.max` with a manual `if` check to avoid the overhead of a method call:
```java
if (j > result) result = j;
```

### 4. Key Algorithmic Pattern
**Linear Scan (Single Pass):** The problem is solved by iterating through the data once and maintaining a running state (the current streak) and a global maximum.
