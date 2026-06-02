# Height Checker

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-height-checker` |
| Topics | Array, Sorting, Counting Sort |
| Solved | 2024-09-19 |
| Runtime | 28 ms (beats 5.203599999999995%) |
| Memory | 16.4 MB (beats 100%) |

## Problem Statement

A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in **non-decreasing order** by height. Let this ordering be represented by the integer array `expected` where `expected[i]` is the expected height of the `ith` student in line.

You are given an integer array `heights` representing the **current order** that the students are standing in. Each `heights[i]` is the height of the `ith` student in line (**0-indexed**).

Return _the **number of indices** where _`heights[i] != expected[i]`.

 

**Example 1:**

**Input:** heights = [1,1,4,2,1,3]
**Output:** 3
**Explanation:** 
heights:  [1,1,4,2,1,3]
expected: [1,1,1,2,3,4]
Indices 2, 4, and 5 do not match.

**Example 2:**

**Input:** heights = [5,1,2,3,4]
**Output:** 5
**Explanation:**
heights:  [5,1,2,3,4]
expected: [1,2,3,4,5]
All indices do not match.

**Example 3:**

**Input:** heights = [1,2,3,4,5]
**Output:** 0
**Explanation:**
heights:  [1,2,3,4,5]
expected: [1,2,3,4,5]
All indices match.

 

**Constraints:**

	- `1 <= heights.length <= 100`

	- `1 <= heights[i] <= 100`

## Hints

<details>
<summary>Hint 1</summary>

Build the correct order of heights by sorting another array, then compare the two arrays.

</details>

## Solutions

```Python3
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights.copy())        
        return len([i for i in range(len(heights)) if heights[i] != expected[i]])

```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(n \log n)$ due to the `sorted()` function (Timsort). Iterating through the lists takes $O(n)$.
*   **Space Complexity:** $O(n)$ to store the `expected` list and the temporary list created by the list comprehension.

### 2. Correctness
The logic is **correct**. It accurately implements the problem requirements by comparing the original array against its sorted version. It handles edge cases like already sorted arrays, arrays with duplicate heights, and minimum/maximum constraints effectively.

### 3. Concrete Optimization
**Use Counting Sort:** Since the problem constraints state heights are between 1 and 100, you can achieve **$O(n)$ time** and **$O(1)$ extra space** (excluding output) by using a frequency array.

Alternatively, to optimize the current approach's space, use a **generator expression** with `sum` to avoid creating an intermediate list:
```python
return sum(h != e for h, e in zip(heights, expected))
```

### 4. Key Algorithmic Pattern
**Sorting and Comparison:** The fundamental approach relies on generating a "target" state via sorting and performing a linear scan to count discrepancies.
