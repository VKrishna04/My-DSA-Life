# Find Closest Person

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-find-closest-person` |
| Topics | Math |
| Solved | 2025-06-02 |
| Runtime | 4 ms (beats 2.4753000000000025%) |
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

**1. Complexity**
*   **Time Complexity:** $O(1)$ — Performs a constant number of arithmetic operations and comparisons.
*   **Space Complexity:** $O(1)$ — Uses a fixed amount of extra space regardless of input size.

**2. Correctness**
The logic is **correct**. It accurately calculates the absolute 1D distance (Manhattan distance) and returns the specified mapping:
*   $x$ is closer: returns 1
*   $y$ is closer: returns 2
*   Tie: returns 0
*   **Edge Cases:** Handles $x = y$ and $z$ being exactly equidistant between $x$ and $y$ correctly by returning 0.

**3. Concrete Optimization**
While the current code is efficient, you can slightly reduce the overhead of creating variables and improve readability using a sign-based approach if this logic were used in a tight loop:
```python
# Returns 1 if a < b, 2 if b < a, 0 if equal
return (a > b) + (a >= b) if a != b else 0
```
However, the most practical "optimization" for Pythonic code is using the **`cmp` logic** style if the return values were -1, 0, 1. For your specific mapping (1, 2, 0), the current ternary is already optimal.

**4. Key Algorithmic Pattern**
**Absolute Difference / Manhattan Distance (1D):** Calculating the distance between points on a line to determine proximity.
