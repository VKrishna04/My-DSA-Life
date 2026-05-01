# Valid Phone Numbers

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-valid-phone-numbers` |
| Topics | Shell |
| Solved | 2026-05-01 |
| Runtime | 63 ms (beats 61.406199999999984%) |
| Memory | 3.4 MB (beats 71.7854%) |

## Problem Statement

Given a text file `file.txt` that contains a list of phone numbers (one per line), write a one-liner bash script to print all valid phone numbers.

You may assume that a valid phone number must appear in one of the following two formats: (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)

You may also assume each line in the text file must not contain leading or trailing white spaces.

**Example:**

Assume that `file.txt` has the following content:

987-123-4567
123 456 7890
(123) 456-7890

Your script should output the following valid phone numbers:

987-123-4567
(123) 456-7890

## Solutions

```Bash
# Read from the file file.txt and output all valid phone numbers to stdout.
grep -E '^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$' file.txt

```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(N \times M)$, where $N$ is the number of lines and $M$ is the average length of a line. Grep scans each character once.
*   **Space Complexity:** $O(1)$ (or $O(M)$ for the internal buffer), as it processes the file line-by-line without storing the entire content in memory.

### 2. Correctness
The solution is **correct** for the LeetCode constraints. It precisely matches the two required formats:
1.  `xxx-xxx-xxxx`: Handled by `[0-9]{3}-` followed by the suffix.
2.  `(xxx) xxx-xxxx`: Handled by `\([0-9]{3}\) ` followed by the suffix.
The anchors `^` and `$` ensure no leading or trailing junk characters are allowed.

### 3. Optimization
While `grep -E` is efficient, performance on extremely large files can be improved by setting the locale to C:
```bash
LC_ALL=C grep -E '^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$' file.txt
```
This bypasses Unicode/multibyte character processing, making the regex engine significantly faster.

### 4. Key Algorithmic Pattern
**Regular Expression Matching**: Utilizing a Deterministic Finite Automaton (DFA) or Nondeterministic Finite Automaton (NFA) to perform linear-time pattern recognition.
