# Can Make Arithmetic Progression From Sequence

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-can-make-arithmetic-progression-from-sequence` |
| Topics | Array, Sorting |
| Solved | 2025-05-06 |
| Runtime | 0 ms (beats 100%) |
| Memory | 17.6 MB (beats 100%) |

## Problem Statement

A sequence of numbers is called an **arithmetic progression** if the difference between any two consecutive elements is the same.

Given an array of numbers `arr`, return `true` _if the array can be rearranged to form an **arithmetic progression**. Otherwise, return_ `false`.

 

**Example 1:**

**Input:** arr = [3,5,1]
**Output:** true
**Explanation: **We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.

**Example 2:**

**Input:** arr = [1,2,4]
**Output:** false
**Explanation: **There is no way to reorder the elements to obtain an arithmetic progression.

 

**Constraints:**

	- `2 <= arr.length <= 1000`

	- `-106 <= arr[i] <= 106`

## Hints

<details>
<summary>Hint 1</summary>

Consider that any valid arithmetic progression will be in sorted order.

</details>

<details>
<summary>Hint 2</summary>

Sort the array, then check if the differences of all consecutive elements are equal.

</details>

## Solutions

```Python3
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr)):
            if i == 0:
                diff = arr[1] - arr[0]
            if (i != 0) and (i != len(arr)-1):
                if arr[i] - arr[i-1] != arr[i+1] - arr[i] != diff:
                    return False
        return True
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(N \log N)$ due to the `arr.sort()` function. The subsequent linear scan is $O(N)$.
*   **Space Complexity:** $O(1)$ or $O(N)$ depending on the Python version's `sort()` implementation (Timsort typically uses $O(N)$ auxiliary space).

### 2. Correctness & Edge Cases
*   **Logical Flaw:** The expression `a != b != diff` is evaluated as `(a != b) and (b != c)`. This does not correctly verify if the current difference matches the initial `diff`.
*   **Index Error:** If `len(arr) < 2`, `arr[1]` will raise an `IndexError`.
*   **Redundancy:** The loop checks the same differences multiple times. A simple check of `arr[i] - arr[i-1] == diff` for all $i > 0$ is sufficient.

### 3. Optimization
To achieve **$O(N)$ time complexity**, use a Hash Set:
1. Find `min_val` and `max_val`.
2. Calculate the expected common difference: `d = (max_val - min_val) / (len(arr) - 1)`.
3. If `d == 0`, all elements must be equal.
4. If `d` is not an integer, return `False`.
5. Iterate through the array and ensure every `min_val + k * d` exists in the set.

### 4. Key Algorithmic Pattern
**Sorting.** By ordering the elements, the arithmetic property becomes a simple local check between neighbors.
