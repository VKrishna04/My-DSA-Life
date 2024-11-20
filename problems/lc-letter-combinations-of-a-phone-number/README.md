# Letter Combinations of a Phone Number

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-letter-combinations-of-a-phone-number` |
| Topics | Hash Table, String, Backtracking |
| Solved | 2025-07-23 |
| Runtime | 0 ms (beats 100%) |
| Memory | 17.8 MB (beats 100%) |

## Problem Statement

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in **any order**.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

 

**Example 1:**

**Input:** digits = "23"
**Output:** ["ad","ae","af","bd","be","bf","cd","ce","cf"]

**Example 2:**

**Input:** digits = "2"
**Output:** ["a","b","c"]

 

**Constraints:**

	- `1 <= digits.length <= 4`

	- `digits[i]` is a digit in the range `['2', '9']`.

## Solutions

```Python3
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        
        alpha = {
            '2': ["a", "b", "c"],
            '3': ["d", "e", "f"],
            '4': ["g", "h", "i"],
            '5': ["j", "k", "l"],
            '6': ["m", "n", "o"],
            '7': ["p", "q", "r", "s"],
            '8': ["t", "u", "v"],
            '9': ["w", "x", "y", "z"],
        }
        
        def back(i,cur):
            if len(cur) == len(digits):
                res.append(cur)
                return
            for c in alpha[digits[i]]:
                back(i+1,cur+c)
        if digits:
            back(0,"")
        return res

```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(N \cdot 4^N)$, where $N$ is the length of `digits`. There are at most $4^N$ combinations, and constructing each string takes $O(N)$ time.
*   **Space Complexity:** $O(N)$ for the recursion stack depth. (Ignoring the $O(N \cdot 4^N)$ space required for the output list).

### 2. Correctness
The code is **correct** and handles the primary edge case (empty input) with the `if digits:` check. It follows the standard recursive approach for generating permutations.

### 3. Optimization
**String Builder Pattern:** In Python, strings are immutable. Using `cur + c` creates a new string at every recursive step. While negligible for $N \le 4$, for larger inputs, passing a **list of characters** and using `''.join(path)` when `len(path) == len(digits)` is more memory-efficient.

Alternatively, use a **mapping string** instead of a list in the dictionary (e.g., `'2': "abc"`) to save minor initialization overhead.

### 4. Key Algorithmic Pattern
**Backtracking (Depth-First Search):** The algorithm explores every possible branch of the decision tree (one digit at a time) and "backtracks" to explore alternative letters.
