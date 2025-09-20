# Minimum Moves to Reach Target Score

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-minimum-moves-to-reach-target-score::1777023549` |
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
