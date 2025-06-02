# Tenth Line

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-tenth-line::1651709018` |
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
