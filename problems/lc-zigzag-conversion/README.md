# Zigzag Conversion

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-zigzag-conversion` |
| Topics | String |
| Solved | 2024-11-07 |
| Runtime | 11 ms (beats 55.90290000000001%) |
| Memory | 16.7 MB (beats 100%) |

## Problem Statement

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: `"PAHNAPLSIIGYIR"`

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

 

**Example 1:**

**Input:** s = "PAYPALISHIRING", numRows = 3
**Output:** "PAHNAPLSIIGYIR"

**Example 2:**

**Input:** s = "PAYPALISHIRING", numRows = 4
**Output:** "PINALSIGYAHRPI"
**Explanation:**
P     I    N
A   L S  I G
Y A   H R
P     I

**Example 3:**

**Input:** s = "A", numRows = 1
**Output:** "A"

 

**Constraints:**

	- `1 <= s.length <= 1000`

	- `s` consists of English letters (lower-case and upper-case), `','` and `'.'`.

	- `1 <= numRows <= 1000`

## Solutions

```Python3
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        line = [''] * numRows
        cycle_length = (numRows - 1) * 2
        for i in range(len(s)):
            cycle_pos = i % cycle_length
            if cycle_pos < numRows:
                line[cycle_pos] += s[i]
            else:
                line[cycle_length - cycle_pos] += s[i]
            
        return "".join(line)
```

## AI Review

**1. Complexity**
*   **Time:** $O(n)$, where $n$ is the length of string `s`. We iterate through the string once and perform a final join.
*   **Space:** $O(n)$ to store the characters in the `line` array before joining them into the final result.

**2. Correctness**
The solution is **correct**. It robustly handles:
*   `numRows = 1`: Guarded at the start.
*   `numRows >= len(s)`: Guarded; returns the original string.
*   General zigzag logic: The math `cycle_length - cycle_pos` correctly maps the "upward" diagonal characters back to the appropriate row.

**3. Concrete Optimization**
While the current approach is efficient, you can replace the modulo and conditional logic with a **direction toggle**. This avoids repeated arithmetic operations:
```python
row, step = 0, 1
for char in s:
    line[row] += char
    if row == 0: step = 1
    elif row == numRows - 1: step = -1
    row += step
```
This improves readability and slightly reduces the constant factor by replacing division/modulo with simple addition.

**4. Key Algorithmic Pattern**
**Simulation (Row Tracking):** The algorithm simulates the traversal of the zigzag pattern by tracking the current vertical position (row) for each character.
