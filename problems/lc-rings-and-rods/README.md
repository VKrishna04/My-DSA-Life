# Rings and Rods

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-rings-and-rods` |
| Topics | Hash Table, String |
| Solved | 2024-10-20 |
| Runtime | 0 ms (beats 100%) |
| Memory | 16.6 MB (beats 100%) |

## Problem Statement

There are `n` rings and each ring is either red, green, or blue. The rings are distributed **across ten rods** labeled from `0` to `9`.

You are given a string `rings` of length `2n` that describes the `n` rings that are placed onto the rods. Every two characters in `rings` forms a **color-position pair** that is used to describe each ring where:

	- The **first** character of the `ith` pair denotes the `ith` ring's **color** (`'R'`, `'G'`, `'B'`).

	- The **second** character of the `ith` pair denotes the **rod** that the `ith` ring is placed on (`'0'` to `'9'`).

For example, `"R3G2B1"` describes `n == 3` rings: a red ring placed onto the rod labeled 3, a green ring placed onto the rod labeled 2, and a blue ring placed onto the rod labeled 1.

Return _the number of rods that have **all three colors** of rings on them._

 

**Example 1:**

**Input:** rings = "B0B6G0R6R0R6G9"
**Output:** 1
**Explanation:** 
- The rod labeled 0 holds 3 rings with all colors: red, green, and blue.
- The rod labeled 6 holds 3 rings, but it only has red and blue.
- The rod labeled 9 holds only a green ring.
Thus, the number of rods with all three colors is 1.

**Example 2:**

**Input:** rings = "B0R0G0R9R0B0G0"
**Output:** 1
**Explanation:** 
- The rod labeled 0 holds 6 rings with all colors: red, green, and blue.
- The rod labeled 9 holds only a red ring.
Thus, the number of rods with all three colors is 1.

**Example 3:**

**Input:** rings = "G4"
**Output:** 0
**Explanation:** 
Only one ring is given. Thus, no rods have all three colors.

 

**Constraints:**

	- `rings.length == 2 * n`

	- `1 <= n <= 100`

	- `rings[i]` where `i` is **even** is either `'R'`, `'G'`, or `'B'` (**0-indexed**).

	- `rings[i]` where `i` is **odd** is a digit from `'0'` to `'9'` (**0-indexed**).

## Hints

<details>
<summary>Hint 1</summary>

For every rod, look through ‘rings’ to see if the rod contains all colors.

</details>

<details>
<summary>Hint 2</summary>

Create 3 booleans, 1 for each color, to store if that color is present for the current rod. If all 3 are true after looking through the string, then the rod contains all the colors.

</details>

## Solutions

```Python3
class Solution:
    def countPoints(self, rings: str) -> int:
        rods = {}
        for i in range(0,len(rings),2):
            colour = rings[i]
            rod = rings[i+1]

            if rod not in rods:
                rods[rod] = set()
            rods[rod].add(colour)
        
        count = 0
        for colour in rods.values():
            if {'R', 'G', 'B'}.issubset(colour):
                count += 1
        return count
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(n)$, where $n$ is the length of the string. We iterate through the string once and then through a maximum of 10 rods.
*   **Space Complexity:** $O(1)$. Although we use a dictionary, there are at most 10 unique rods and 3 colors per rod, making the storage size constant regardless of input length.

### 2. Correctness
The code is **correct**. It handles multiple rings of the same color on the same rod using a `set` and correctly identifies rods with all three colors. 
*   **Edge Cases:** The constraints guarantee an even length string (min 2), so empty inputs aren't an issue. The use of `issubset` (or simply checking `len(colour) == 3`) handles duplicate rings perfectly.

### 3. Optimization
**Use Bitmasks:** Instead of a dictionary of sets, use an array of 10 integers. Assign each color a bit (R=1, G=2, B=4). Perform a bitwise OR for each ring. A rod has all colors if its value is `7`. This avoids the overhead of object creation and hashing.

### 4. Key Algorithmic Pattern
**Hash Map (Frequency/Set Tracking):** Grouping attributes (colors) by a unique identifier (rod index) to evaluate a collection property.
