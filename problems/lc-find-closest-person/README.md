# Find Closest Person

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-find-closest-person` |
| Topics | Math |
| Solved | 2025-06-02 |
| Runtime | 4 ms (beats 2%) |
| Memory | 17.6 MB (beats 100%) |

## Problem Statement

You are given three integers `x`, `y`, and `z`, representing the positions of three people on a number line:

	- `x` is the position of Person 1.

	- `y` is the position of Person 2.

	- `z` is the position of Person 3, who does **not** move.

Both Person 1 and Person 2 move toward Person 3 at the **same** speed.

Determine which person reaches Person 3 **first**:

	- Return 1 if Person 1 arrives first.

	- Return 2 if Person 2 arrives first.

	- Return 0 if both arrive at the **same** time.

Return the result accordingly.

 

**Example 1:**

**Input:** x = 2, y = 7, z = 4

**Output:** 1

**Explanation:**

	- Person 1 is at position 2 and can reach Person 3 (at position 4) in 2 steps.

	- Person 2 is at position 7 and can reach Person 3 in 3 steps.

Since Person 1 reaches Person 3 first, the output is 1.

**Example 2:**

**Input:** x = 2, y = 5, z = 6

**Output:** 2

**Explanation:**

	- Person 1 is at position 2 and can reach Person 3 (at position 6) in 4 steps.

	- Person 2 is at position 5 and can reach Person 3 in 1 step.

Since Person 2 reaches Person 3 first, the output is 2.

**Example 3:**

**Input:** x = 1, y = 5, z = 3

**Output:** 0

**Explanation:**

	- Person 1 is at position 1 and can reach Person 3 (at position 3) in 2 steps.

	- Person 2 is at position 5 and can reach Person 3 in 2 steps.

Since both Person 1 and Person 2 reach Person 3 at the same time, the output is 0.

 

**Constraints:**

	- `1 <= x, y, z <= 100`

## Hints

<details>
<summary>Hint 1</summary>

Compare the distances from Persons 1 and 2 to Person 3 to determine the answer.

</details>

## Solutions

```Python3
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        a = abs(z - x) 
        b = abs(z - y)
        # if b > a:
        #     return 1
        # elif a > b:
        #     return 2
        # else:
        #     return 0

        return 1 if a < b else 2 if a > b else 0
```

## AI Review

### Review

**1. Complexity**
*   **Time Complexity:** $O(1)$ — Basic arithmetic and comparisons take constant time.
*   **Space Complexity:** $O(1)$ — Only a few integer variables are used.

**2. Correctness**
The solution is **correct**. It properly handles:
*   **Equidistance:** Returns `0` when $|z-x| = |z-y|$.
*   **Negative Coordinates:** `abs()` correctly calculates distance regardless of sign.
*   **Large Integers:** Python 3 handles arbitrary-precision integers, preventing the overflow issues common in languages like C++ or Java.

**3. Optimization**
While the code is already optimal in terms of complexity, you can simplify the logic by removing the intermediate variables `a` and `b` to reduce memory overhead slightly (though negligible):

```python
return 1 if abs(z - x) < abs(z - y) else 2 if abs(z - x) > abs(z - y) else 0
```
However, the current version is more readable.

**4. Key Algorithmic Pattern**
*   **Absolute Difference / Manhattan Distance (1D):** The problem relies on calculating the magnitude of the displacement between points on a number line.
