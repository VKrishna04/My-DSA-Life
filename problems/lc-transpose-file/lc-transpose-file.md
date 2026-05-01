# Transpose File

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-transpose-file` |
| Topics | Shell |
| Solved | 2026-05-01 |
| Runtime | 78 ms (beats 11.792500000000016%) |
| Memory | 7.8 MB (beats 12.028400000000005%) |

## Problem Statement

Given a text file `file.txt`, transpose its content.

You may assume that each row has the same number of columns, and each field is separated by the `' '` character.

**Example:**

If `file.txt` has the following content:

name age
alice 21
ryan 30

Output the following:

name alice ryan
age 21 30

## Solutions

```Bash
# Read from the file file.txt and print its transposed content to stdout.
awk '{
        for (i = 1; i <= NF; i++) {
            s[NR, i] = $i
        }
    }
    NF > max_nf { max_nf = NF }
    END {
    for (i = 1; i <= max_nf; i++) {
        for (j = 1; j <= NR; j++) {
            printf "%s%s", s[j, i], (j == NR ? "" : " ")
        }
    print ""
    }
}' file.txt
```

## AI Review

**1. Complexity**
*   **Time:** $O(R \times C)$, where $R$ is the number of rows and $C$ is the number of columns. Every element is processed exactly twice (once for storage, once for output).
*   **Space:** $O(R \times C)$. The script stores the entire file in memory within an associative array.

**2. Correctness**
*   **Edge Cases:**
    *   **Memory Limit:** Will fail on extremely large files because it loads everything into RAM.
    *   **Ragged Rows:** If rows have unequal lengths, `max_nf` ensures all columns are processed, but it may print trailing spaces or empty strings for missing elements.
    *   **Trailing Whitespace:** The ternary operator `j == NR` correctly prevents trailing spaces on lines.

**3. Optimization**
Instead of storing every element individually, concatenate strings column-wise during the first pass. This reduces array lookups and simplifies the output loop:
```awk
{
    for (i = 1; i <= NF; i++) {
        res[i] = (NR == 1) ? $i : res[i] " " $i
    }
}
END {
    for (i = 1; i <= length(res); i++) print res[i]
}
```

**4. Key Algorithmic Pattern**
**Matrix Transposition** using **Associative Arrays** (simulating a 2D grid with `s[row, col]`).
