# Word Frequency

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-word-frequency` |
| Topics | Shell |
| Solved | 2025-06-02 |
| Runtime | 86 ms (beats 15.703799999999957%) |
| Memory | 3.9 MB (beats 24.560199999999995%) |

## Problem Statement

Write a bash script to calculate the frequency of each word in a text file `words.txt`.

For simplicity sake, you may assume:

	- `words.txt` contains only lowercase characters and space `' '` characters.

	- Each word must consist of lowercase characters only.

	- Words are separated by one or more whitespace characters.

**Example:**

Assume that `words.txt` has the following content:

the day is sunny the the
the sunny is is

Your script should output the following, sorted by descending frequency:

the 4
is 3
sunny 2
day 1

**Note:**

	- Don't worry about handling ties, it is guaranteed that each word's frequency count is unique.

	- Could you write it in one-line using Unix pipes?

## Solutions

```Bash
# Read from the file words.txt and output the word frequency list to stdout.
tr -s ' ' '\n' < words.txt | sort | uniq -c | sort -nr | awk '{print $2, $1}';
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(N \log N)$, where $N$ is the total number of words. The bottleneck is the initial `sort` operation.
*   **Space Complexity:** $O(N)$ to store words during the sorting phases.

### 2. Correctness
*   **Delimiter Issue:** The problem specifies words are separated by "one or more whitespace characters" (including tabs/newlines). `tr -s ' '` only handles spaces. 
*   **Empty Lines:** If the input has leading/trailing spaces or multiple newlines, `tr` will produce empty lines which `uniq -c` will count as a word. 
*   **Fix:** Use `tr -s '[:space:]' '\n'` and pipe through `sed '/^$/d'` to remove empty lines.

### 3. Concrete Optimization
Replace the first `sort | uniq -c` with a single `awk` command to count frequencies using an associative array. This reduces time complexity from $O(N \log N)$ to $O(N)$ for the counting phase.
```bash
awk '{for(i=1;i<=NF;i++) count[$i]++} END {for(w in count) print w, count[w]}' words.txt | sort -rnk2
```

### 4. Key Algorithmic Pattern
**Unix Pipeline (Pipes-and-Filters):** Transforming a data stream through a sequence of discrete processing stages.
