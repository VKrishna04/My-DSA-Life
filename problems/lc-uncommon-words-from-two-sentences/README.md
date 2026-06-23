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

Here's a review of your solution:

1.  **Time Complexity**: O(L1 + L2), where L1 and L2 are the lengths of `s1` and `s2` respectively. This accounts for splitting strings and populating the `Counter`.
    **Space Complexity**: O(W1 + W2), where W1 and W2 are the number of words in `s1` and `s2`. This stores all words and their counts.

2.  **Correctness**: The solution is correct and robust. It correctly handles empty sentences, single-word sentences, and words repeated within or across sentences. It accurately identifies words that appear exactly once in total. It assumes case-sensitive word comparison, which is standard unless otherwise specified.

3.  **Optimisation**: A minor memory optimization is to avoid creating the intermediate `words` list by using `itertools.chain`:
    ```python
    from itertools import chain
    # ... inside method ...
    count = Counter(chain(s1.split(), s2.split()))
    ```
    This prevents one full list allocation for all words, potentially saving memory for very long sentences, though its performance impact is often negligible.

4.  **Key Algorithmic Pattern**: Frequency Counting / Hashing (using a hash map, specifically `collections.Counter`).
