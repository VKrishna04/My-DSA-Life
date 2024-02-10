# Find Numbers with Even Number of Digits

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-find-numbers-with-even-number-of-digits` |
| Topics | Array, Math |
| Solved | 2024-02-10 |
| Runtime | 1 ms (beats 99.6546%) |
| Memory | 42.6 MB (beats 100%) |

## Problem Statement

Given an array `nums` of integers, return how many of them contain an **even number** of digits.

 

**Example 1:**

**Input:** nums = [12,345,2,6,7896]
**Output:** 2
**Explanation: 
**12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.

**Example 2:**

**Input:** nums = [555,901,482,1771]
**Output:** 1 
**Explanation: **
Only 1771 contains an even number of digits.

 

**Constraints:**

	- `1 <= nums.length <= 500`

	- `1 <= nums[i] <= 105`

## Solutions

```Java
class Solution {
    public static int findNumbers(int[] nums) {
        int result = 0;
        for (int i : nums) {
            if (NoOfDigits(i,0)%2==0){
                result++;
            }
        }
        return result;
    }

    public static int NoOfDigits(int n, int result) {
        if (n < 10) {
            return result + 1;
        }
        return NoOfDigits(n / 10, result + 1);
    }
}
```

## AI Review

### Analysis of Java Solution

**1. Complexity**
*   **Time Complexity:** $O(N \times K)$, where $N$ is the number of elements and $K$ is the maximum number of digits (logarithmic relative to the value of the number).
*   **Space Complexity:** $O(K)$ due to the recursion stack depth for each number.

**2. Correctness**
*   **General:** The logic is correct for positive integers.
*   **Edge Cases:** 
    *   **Zero:** Works correctly (returns 1 digit).
    *   **Negative Numbers:** If the input contained negative numbers (e.g., -15), the `n < 10` check would immediately return 1, which is incorrect. However, LeetCode constraints for this problem usually specify $1 \le nums[i] \le 10^5$.
    *   **Stack Overflow:** For very large numbers (outside integer range), recursion could theoretically hit limits, but not within $10^5$.

**3. Optimization**
Replace recursion with **mathematical calculation** or **range checks** to achieve $O(1)$ space and faster execution:
```java
// Math optimization
if (((int)Math.log10(i) + 1) % 2 == 0) result++;

// Range check (fastest for constraints up to 10^5)
if ((i >= 10 && i <= 99) || (i >= 1000 && i <= 9999) || i == 100000) result++;
```

**4. Key Algorithmic Pattern**
**Array Traversal** combined with **Digit Counting**.
