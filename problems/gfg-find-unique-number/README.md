# Find Unique Number

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-find-unique-number` |
| Topics | Bit Manipulation |
| Solved | 2026-06-24 |

## Problem Statement

Given a **unsorted **array **arr[]** of positive integers having all the numbers occurring exactly **twice**, except for one number which will occur only **once**. Find the number occurring only once.

**Examples :**

**Input: **arr[] = [1, 2, 1, 5, 5]**
Output: **2
**Explanation: **Since 2 occurs once, while other numbers occur twice, 2 is the answer.
**Input: **arr[] = [2, 30, 2, 15, 20, 30, 15]
**Output: **20
**Explanation: **Since 20 occurs once, while other numbers occur twice, 20 is the answer.
**Constraints**
1 &le;  arr.size()  &le; 106
0 &le; arr[i] &le; 109

## AI Review

### Review

**1. Complexity**
*   **Time Complexity:** $O(\log n)$ as the search space is halved in each iteration. This is optimal for a sorted input.
*   **Space Complexity:** $O(1)$ since only a few variables are used. You avoided the $O(n)$ space pitfall common in frequency-counting approaches.

**2. Correctness**
The solution assumes the array is **sorted** and all duplicates occur in pairs. 
*   **Edge Cases:** It correctly handles a single-element array ($n=1$) because the `while` loop condition fails immediately and returns `arr[0]`.
*   **Potential Fail:** If $n=0$, the code will raise an `IndexError`. Always verify if the input can be empty.

**3. Concrete Optimisation**
Instead of the `if mid % 2 == 1` block, you can use bitwise XOR to find the "partner" index. Comparing `arr[mid]` with `arr[mid ^ 1]` automatically checks the correct neighbor regardless of whether `mid` is even or odd, simplifying the branching logic.

**4. Key Algorithmic Pattern**
**Binary Search on Parity:** The logic exploits the fact that before the unique element, pairs start at even indices $(i, i+1)$, but after the unique element, they start at odd indices.
