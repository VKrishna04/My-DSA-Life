# Find if Digit Game Can Be Won

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-find-if-digit-game-can-be-won::1428167266` |
| Topics | Array, Math |
| Solved | 2024-10-20 |
| Runtime | 0 ms (beats 100%) |
| Memory | 16.5 MB (beats 100%) |

## Problem Statement

You are given an array of **positive** integers `nums`.

Alice and Bob are playing a game. In the game, Alice can choose **either** all single-digit numbers or all double-digit numbers from `nums`, and the rest of the numbers are given to Bob. Alice wins if the sum of her numbers is **strictly greater** than the sum of Bob's numbers.

Return `true` if Alice can win this game, otherwise, return `false`.

 

**Example 1:**

**Input:** nums = [1,2,3,4,10]

**Output:** false

**Explanation:**

Alice cannot win by choosing either single-digit or double-digit numbers.

**Example 2:**

**Input:** nums = [1,2,3,4,5,14]

**Output:** true

**Explanation:**

Alice can win by choosing single-digit numbers which have a sum equal to 15.

**Example 3:**

**Input:** nums = [5,5,5,25]

**Output:** true

**Explanation:**

Alice can win by choosing double-digit numbers which have a sum equal to 25.

 

**Constraints:**

	- `1 <= nums.length <= 100`

	- `1 <= nums[i] <= 99`

## Solutions

```Python3
class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = 0
        double = 0
        for num in nums:
            if len(str(num)) == 2:
                double += num
            else:
                single += num

        if single == double:
            return False
        return True
```

## AI Review

### Evaluation
1.  **Complexity**: 
    *   **Time**: $O(N)$, where $N$ is the number of elements in `nums`. Converting integers $\le 99$ to strings takes constant time.
    *   **Space**: $O(1)$, as only two integer variables are used regardless of input size.

2.  **Correctness**: The logic is correct. Alice wins if $Sum_{single} > Sum_{double}$ or $Sum_{double} > Sum_{single}$. This is mathematically equivalent to $Sum_{single} \neq Sum_{double}$. It handles the constraints ($1 \le nums[i] \le 99$) properly.

3.  **Optimization**: Avoid string conversion (`len(str(num))`), which is computationally expensive due to object allocation. Instead, use a direct numeric comparison:
    ```python
    if num < 10:
        single += num
    else:
        double += num
    ```
    Alternatively, use a single accumulator to track the difference: `diff += (num if num < 10 else -num)`. If `diff != 0`, Alice wins.

4.  **Key Algorithmic Pattern**: **Linear Scan / Accumulation**. The solution iterates through the data once to aggregate values into categories for comparison.
