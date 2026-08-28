# Product Array Puzzle

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-product-array-puzzle4525` |
| Topics | Array, Prefix Sum |
| Solved | 2026-06-24 |

## Problem Statement

Given an array, **arr[] **construct a product array, **`res[]`** where each element in **res[i] **is the product of all elements in **`arr[]`** except **`arr[i]`**. Return this resultant array, `res[].
**Note:** Each element is res[] lies inside the 32-bit integer range.`

**Examples:**

**Input: **arr[] = [10, 3, 5, 6, 2]
**Output: **[180, 600, 360, 300, 900]**
Explanation: **For i=0, res[i] = 3 * 5 * 6 * 2 is 180.
For i = 1, res[i] = 10 * 5 * 6 * 2 is 600.
For i = 2, res[i] = 10 * 3 * 6 * 2 is 360.
For i = 3, res[i] = 10 * 3 * 5 * 2 is 300.
For i = 4, res[i] = 10 * 3 * 5 * 6 is 900.

**Input: **arr[] = [12, 0]
**Output: **[0, 12]
**Explanation: **For i = 0, res[i] is 0.
For i = 1, res[i] is 12.
**Constraints:**
2 <= arr.size() <= 105
-100 <= arr[i] <= 100

## AI Review

### Review
**1. Complexity:**
*   **Time:** $O(n)$. You perform two linear passes.
*   **Space:** $O(1)$ auxiliary space, as you only use a few variables regardless of input size. The $O(n)$ space for the result array is typically expected for this problem.

**2. Correctness:**
The logic correctly handles the three critical states: multiple zeros (all products are 0), one zero (only the zero index has a product), and no zeros (standard division). One minor logic flaw: checking `if zero > 1` inside the loop is redundant; checking it once before the second loop is more efficient.

**3. Optimization:**
To handle the common constraint where **division is forbidden**, use the **Prefix and Suffix Product** pattern. Create the result by multiplying the product of all elements to the left by the product of all elements to the right. This removes the need for `if/else` logic for zeros and division entirely.

**4. Key Pattern:**
**Prefix/Suffix Decomposition.** This solution currently uses a "Total Product with Zero Counting" strategy, but the problem is a classic introduction to precomputing cumulative data from both ends of an array.
