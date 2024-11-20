# Tenth Line

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-tenth-line` |
| Topics | Shell |
| Solved | 2025-06-02 |
| Runtime | 21 ms (beats 86.8768%) |
| Memory | 4 MB (beats 1.250700000000009%) |

## Problem Statement

Given a text file `file.txt`, print just the 10th line of the file.



**Example:**



Assume that `file.txt` has the following content:




Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10


Your script should output the tenth line, which is:




Line 10


**Note:**

1. If the file contains less than 10 lines, what should you output?

2. There's at least three different solutions. Try to explore all possibilities.

## Solutions

```Bash
# Read from the file file.txt and output the tenth line to stdout.
awk 'NR == 10 {print; exit}' file.txt
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(1)$ relative to total file size. Because of the `exit` command, the script only processes the first 10 lines and ignores the rest, regardless of how large the file is.
*   **Space Complexity:** $O(W)$, where $W$ is the maximum width (length) of a single line, as `awk` processes the file line-by-line.

### 2. Correctness
The solution is **correct**. 
*   **Edge Case (< 10 lines):** If the file has fewer than 10 lines, `awk` reaches the end of the file without triggering the `NR == 10` condition, resulting in no output. This is the expected behavior for this LeetCode problem.
*   **Large Files:** The `exit` statement prevents unnecessary overhead by stopping execution immediately after the target line is found.

### 3. Optimization
The provided solution is already highly optimized for Bash. A slightly more concise alternative is:
`sed -n '10p;10q' file.txt`
This uses `sed` to print the 10th line (`10p`) and immediately quit (`10q`), behaving identically to your `awk` logic.

### 4. Key Algorithmic Pattern
**Stream Filtering with Early Termination (Short-circuiting):** Processing data sequentially until a specific condition is met, then halting to avoid redundant computation.
