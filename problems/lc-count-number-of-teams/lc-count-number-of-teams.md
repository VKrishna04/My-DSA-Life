# Count Number of Teams

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-count-number-of-teams` |
| Topics | Array, Dynamic Programming, Binary Indexed Tree, Segment Tree |
| Solved | 2026-05-03 |
| Runtime | 564 ms (beats 31.12300000000019%) |
| Memory | 19.3 MB (beats 86.9898%) |

## Problem Statement

There are `n` soldiers standing in a line. Each soldier is assigned a **unique** `rating` value.

You have to form a team of 3 soldiers amongst them under the following rules:

	- Choose 3 soldiers with index (`i`, `j`, `k`) with rating (`rating[i]`, `rating[j]`, `rating[k]`).

	- A team is valid if: (`rating[i] < rating[j] < rating[k]`) or (`rating[i] > rating[j] > rating[k]`) where (`0 <= i < j < k < n`).

Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

 

**Example 1:**

**Input:** rating = [2,5,3,4,1]
**Output:** 3
**Explanation:** We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 

**Example 2:**

**Input:** rating = [2,1,3]
**Output:** 0
**Explanation:** We can't form any team given the conditions.

**Example 3:**

**Input:** rating = [1,2,3,4]
**Output:** 4

 

**Constraints:**

	- `n == rating.length`

	- `3 <= n <= 1000`

	- `1 <= rating[i] <= 105`

	- All the integers in `rating` are **unique**.

## Solutions

```Python3
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0

        for j in range(1, len(rating) - 1):
            ls = 0
            lb = 0
            for i in range(j):
                if rating[i] < rating[j]:
                    ls += 1
                if rating[i] > rating[j]:
                    lb += 1
            rs = 0
            rb = 0
            for k in range(j + 1, len(rating)):
                if rating[j] < rating[k]:
                    rb += 1
                if rating[j] > rating[k]:
                    rs += 1
            count += (ls * rb) + (lb * rs)

        return count

```

## AI Review

### Analysis

1. **Complexity**:
    *   **Time**: $O(n^2)$ — It uses a nested loop structure where for each "middle" element $j$, it performs two linear scans of the array.
    *   **Space**: $O(1)$ — Only a few integer variables are used regardless of input size.

2. **Correctness**:
    *   **Correct**. The logic captures both strictly increasing ($ls \times rb$) and strictly decreasing ($lb \times rs$) triplets by treating each element as a potential pivot. Since ratings are unique per problem constraints, equality checks are unnecessary. It correctly handles arrays with length $< 3$ by returning 0.

3. **Optimization**:
    *   **Fenwick Tree (Binary Indexed Tree) or Segment Tree**: You can reduce time complexity to **$O(n \log n)$**. By processing elements and updating a BIT, you can query the number of elements smaller or larger than the current rating in $O(\log n)$ time rather than $O(n)$.

4. **Key Algorithmic Pattern**:
    *   **Middle-Out Counting (Pivot Pattern)**: Instead of iterating through all triplets ($O(n^3)$), the algorithm fixes the middle element $j$ and uses combinatorics to calculate valid pairs around it.
