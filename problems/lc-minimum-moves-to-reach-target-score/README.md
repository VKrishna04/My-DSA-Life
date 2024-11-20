# Minimum Moves to Reach Target Score

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-minimum-moves-to-reach-target-score` |
| Topics | Math, Greedy |
| Solved | 2025-09-20 |
| Runtime | 2 ms (beats 14%) |
| Memory | 17.8 MB (beats 100%) |

## Problem Statement

You are playing a game with integers. You start with the integer `1` and you want to reach the integer `target`.

In one move, you can either:

	- **Increment** the current integer by one (i.e., `x = x + 1`).

	- **Double** the current integer (i.e., `x = 2 * x`).

You can use the **increment** operation **any** number of times, however, you can only use the **double** operation **at most** `maxDoubles` times.

Given the two integers `target` and `maxDoubles`, return _the minimum number of moves needed to reach _`target`_ starting with _`1`.

 

**Example 1:**

**Input:** target = 5, maxDoubles = 0
**Output:** 4
**Explanation:** Keep incrementing by 1 until you reach target.

**Example 2:**

**Input:** target = 19, maxDoubles = 2
**Output:** 7
**Explanation:** Initially, x = 1
Increment 3 times so x = 4
Double once so x = 8
Increment once so x = 9
Double again so x = 18
Increment once so x = 19

**Example 3:**

**Input:** target = 10, maxDoubles = 4
**Output:** 4
**Explanation:**** **Initially, x = 1
Increment once so x = 2
Double once so x = 4
Increment once so x = 5
Double again so x = 10

 

**Constraints:**

	- `1 <= target <= 109`

	- `0 <= maxDoubles <= 100`

## Hints

<details>
<summary>Hint 1</summary>

Solve the opposite problem: start at the given score and move to 1.

</details>

<details>
<summary>Hint 2</summary>

It is better to use the move of the second type once we can to lose more scores fast.

</details>

## Solutions

```Python3
class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        steps = 0

        while target != 1:
            if target % 2 != 0:
                # the target is odd
                steps += 1
                print(f"odd {target}")
                target -= 1
            
            # Now all targets are even

            if maxDoubles > 0:
                print(f"even {target}")
                target = int(target / 2)
                maxDoubles -= 1
                steps += 1
            else:
                break
        print(f"steps {steps}, target {target-1}")
        steps += target - 1
        return steps
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(\min(\text{maxDoubles}, \log(\text{target})))$. Each division reduces the target by half, and the loop terminates early if `maxDoubles` reaches zero.
*   **Space Complexity:** $O(1)$. Only a few integer variables are used.

### 2. Correctness
The solution is **correct**. Working backward from the target is the optimal greedy strategy: you should divide by 2 as late as possible (when the number is largest) to maximize the "value" of each double. It correctly handles `target = 1` and cases where `maxDoubles = 0`.

### 3. Concrete Optimization
Replace the modulo check and division with a more concise combined update. Instead of checking `if target % 2 != 0`, you can calculate the steps for both the potential decrement and the division in one go:

```python
while target > 1 and maxDoubles > 0:
    steps += 1 + (target % 2)
    target //= 2
    maxDoubles -= 1
```
This reduces branching and uses integer division (`//`) instead of float conversion (`int(target / 2)`).

### 4. Key Algorithmic Pattern
**Greedy Strategy (Backward Induction):** By reversing the operations (divide instead of double, subtract instead of add), the greedy choice becomes clear: always divide by 2 if the number is even and doubles are available.
