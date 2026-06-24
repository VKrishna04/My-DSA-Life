# Uncommon Words from Two Sentences

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-uncommon-words-from-two-sentences` |
| Topics | Hash Table, String, Counting |
| Solved | 2026-06-23 |
| Runtime | 0 ms (beats 100%) |
| Memory | 19.4 MB (beats 10.244299999999996%) |

## Problem Statement

A **sentence** is a string of single-space separated words where each word consists only of lowercase letters.

A word is **uncommon** if it appears exactly once in one of the sentences, and **does not appear** in the other sentence.

Given two **sentences** `s1` and `s2`, return _a list of all the **uncommon words**_. You may return the answer in **any order**.

 

**Example 1:**

**Input:** s1 = "this apple is sweet", s2 = "this apple is sour"

**Output:** ["sweet","sour"]

**Explanation:**

The word `"sweet"` appears only in `s1`, while the word `"sour"` appears only in `s2`.

**Example 2:**

**Input:** s1 = "apple apple", s2 = "banana"

**Output:** ["banana"]

 

**Constraints:**

	- `1 <= s1.length, s2.length <= 200`

	- `s1` and `s2` consist of lowercase English letters and spaces.

	- `s1` and `s2` do not have leading or trailing spaces.

	- All the words in `s1` and `s2` are separated by a single space.

## Solutions

```Python3
from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        words = s1.split() + s2.split()
        count = Counter(words)
        return [word for word in count if count[word] == 1]
```

## AI Review

### Review

**1. Complexity**
*   **Time Complexity:** $O(N + M)$, where $N$ and $M$ are the lengths of `s1` and `s2`. Splitting the strings and iterating through the words to populate the hash map are linear operations.
*   **Space Complexity:** $O(N + M)$. The `words` list and the `Counter` dictionary store all unique words from both strings.

**2. Correctness**
*   **Logic:** The solution correctly implements the problem definition: a word is uncommon if it appears exactly once across both sentences.
*   **Edge Cases:**
    *   **Multiple occurrences in one sentence:** Handled correctly (e.g., `s1="apple apple", s2=""` returns `[]`).
    *   **Single word sentences:** Handled correctly.
    *   **Empty inputs:** Per LeetCode constraints, strings contain at least one word.

**3. Optimization**
To improve **memory efficiency**, avoid creating the intermediate `words` list (concatenation). Instead, update the counter in place:
```python
count = Counter(s1.split())
count.update(s2.split())
```
This reduces peak memory usage by avoiding the creation of a third, combined list of all words.

**4. Key Algorithmic Pattern**
**Frequency Counting** using a Hash Map (Hash Table).
