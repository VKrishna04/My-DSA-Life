# Shift Distance Between Two Strings

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-shift-distance-between-two-strings` |
| Topics | Array, String, Prefix Sum |
| Solved | 2024-11-23 |
| Runtime | 2445 ms (beats 7.318000000000165%) |
| Memory | 17.9 MB (beats 100%) |

## Problem Statement

You are given two strings `s` and `t` of the same length, and two integer arrays `nextCost` and `previousCost`.

In one operation, you can pick any index `i` of `s`, and perform **either one** of the following actions:

	- Shift `s[i]` to the next letter in the alphabet. If `s[i] == 'z'`, you should replace it with `'a'`. This operation costs `nextCost[j]` where `j` is the index of `s[i]` in the alphabet.

	- Shift `s[i]` to the previous letter in the alphabet. If `s[i] == 'a'`, you should replace it with `'z'`. This operation costs `previousCost[j]` where `j` is the index of `s[i]` in the alphabet.

The **shift distance** is the **minimum** total cost of operations required to transform `s` into `t`.

Return the **shift distance** from `s` to `t`.

 

**Example 1:**

**Input:** s = "abab", t = "baba", nextCost = [100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], previousCost = [1,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

**Output:** 2

**Explanation:**

	- We choose index `i = 0` and shift `s[0]` 25 times to the previous character for a total cost of 1.

	- We choose index `i = 1` and shift `s[1]` 25 times to the next character for a total cost of 0.

	- We choose index `i = 2` and shift `s[2]` 25 times to the previous character for a total cost of 1.

	- We choose index `i = 3` and shift `s[3]` 25 times to the next character for a total cost of 0.

**Example 2:**

**Input:** s = "leet", t = "code", nextCost = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], previousCost = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

**Output:** 31

**Explanation:**

	- We choose index `i = 0` and shift `s[0]` 9 times to the previous character for a total cost of 9.

	- We choose index `i = 1` and shift `s[1]` 10 times to the next character for a total cost of 10.

	- We choose index `i = 2` and shift `s[2]` 1 time to the previous character for a total cost of 1.

	- We choose index `i = 3` and shift `s[3]` 11 times to the next character for a total cost of 11.

 

**Constraints:**

	- `1 <= s.length == t.length <= 105`

	- `s` and `t` consist only of lowercase English letters.

	- `nextCost.length == previousCost.length == 26`

	- `0 <= nextCost[i], previousCost[i] <= 109`

## Hints

<details>
<summary>Hint 1</summary>

- For every unordered pair of characters `(a, b)`, the cost of turning `a` into `b` is equal to the minimum between: 

- If `i < j`, `nextCost[i] + nextCost[i + 1] + … + nextCost[j - 1]`, and `nextCost[i] + nextCost[i + 1] + … + nextCost[25] + nextCost[0] + … + nextCost[j - 1]` otherwise.

    
    - If `i < j`, `prevCost[i] + prevCost[i - 1] + … + prevCost[0] + prevCost[25] + … + prevCost[j + 1]`, and `prevCost[i] + prevCost[i - 1] + … + prevCost[j + 1]` otherwise.

    
    Where `i` and `j` are the indices of `a` and `b` in the alphabet.

</details>

<details>
<summary>Hint 2</summary>

The shift distance is the sum of costs of turning `s[i]` into `t[i]`.

</details>

## Solutions

```Python3
class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        totalc = 0
        alfa = 26

        for chars, chart in zip(s,t):
            start = ord(chars) - ord('a')
            target = ord(chart) - ord('a')

            forward = (target - start) % alfa
            backward = (start - target) % alfa

            forwardc = sum(nextCost[(start + i) % alfa] for i in range(forward))
            backwardc = sum(previousCost[(start - i) % alfa] for i in range(backward))

            totalc += min(forwardc, backwardc)
        return totalc
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(N \times \Sigma)$, where $N$ is the length of string `s` and $\Sigma = 26$. For each character, the code iterates up to 26 times to sum costs.
*   **Space Complexity:** $O(1)$, as it uses a constant amount of extra space regardless of input size.

### 2. Correctness
The logic is **correct**. It correctly calculates the cumulative cost for shifting forward ($i \to i+1$) and backward ($i \to i-1$) using modulo arithmetic to handle the circular alphabet. It properly identifies the minimum of the two paths for every character pair.

### 3. Optimization
**Precompute a Cost Matrix:** Instead of recalculating sums for every character in the string, precompute a $26 \times 26$ matrix where `matrix[i][j]` stores the minimum cost to shift from character $i$ to $j$. 
*   Use **Prefix Sums** of `nextCost` and `previousCost` to compute any `forwardc` or `backwardc` in $O(1)$. 
*   This reduces the string traversal complexity from $O(N \times 26)$ to $O(N + 26^2)$.

### 4. Key Algorithmic Pattern
**Greedy with Prefix Sum Logic:** The problem treats each character position independently, making a local optimal choice (greedy) based on the computed costs of two possible directions.
