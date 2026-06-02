# Longest Substring Without Repeating Characters

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-longest-substring-without-repeating-characters` |
| Topics | Hash Table, String, Sliding Window |
| Solved | 2024-08-11 |
| Runtime | 51 ms (beats 11.762000000000004%) |
| Memory | 16.5 MB (beats 100%) |

## Problem Statement

Given a string `s`, find the length of the **longest** **substring** without duplicate characters.

 

**Example 1:**

**Input:** s = "abcabcbb"
**Output:** 3
**Explanation:** The answer is "abc", with the length of 3. Note that `"bca"` and `"cab"` are also correct answers.

**Example 2:**

**Input:** s = "bbbbb"
**Output:** 1
**Explanation:** The answer is "b", with the length of 1.

**Example 3:**

**Input:** s = "pwwkew"
**Output:** 3
**Explanation:** The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

 

**Constraints:**

	- `0 <= s.length <= 5 * 104`

	- `s` consists of English letters, digits, symbols and spaces.

## Hints

<details>
<summary>Hint 1</summary>

Since maximum string size is at most 26, generate and check all possible substrings with length at most 26.

</details>

## Solutions

```Python3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # max_length = 1
        # if s is "":
        #     return 0
        # for i in range(len(s)):
        #     st = ""
        #     for ch in s[i:]:
        #         if ch not in st:
        #             st += ch
        #             max_length=max(max_length,len(st))
        #         else:
        #             break
        # print(max_length)
        # return max_length

        start = 0  
        max_length = 0  
        seen_chars = set()  

        for end in range(len(s)):
            while s[end] in seen_chars:
                seen_chars.remove(s[start])
                start += 1
            
            seen_chars.add(s[end])
            
            max_length = max(max_length, end - start + 1)

        return max_length
```

## AI Review

### Review

**1. Complexity**
*   **Time Complexity:** $O(n)$, where $n$ is the length of the string. Each character is added to and removed from the set at most once.
*   **Space Complexity:** $O(min(n, m))$, where $m$ is the size of the character set (e.g., ASCII).

**2. Correctness**
The solution is **correct** and handles all edge cases effectively:
*   **Empty string:** Returns `0`.
*   **Single character:** Returns `1`.
*   **Identical characters ("bbbbb"):** Returns `1`.
*   **All unique characters:** Returns `len(s)`.

**3. Optimization**
Use a **Hash Map (Dictionary)** to store the *last seen index* of each character instead of a set. This allows the `start` pointer to "jump" directly past the duplicate character instead of incrementing one by one:
```python
char_map = {}
for end in range(len(s)):
    if s[end] in char_map and char_map[s[end]] >= start:
        start = char_map[s[end]] + 1
    char_map[s[end]] = end
    max_length = max(max_length, end - start + 1)
```
This reduces the number of operations inside the loop.

**4. Key Algorithmic Pattern**
**Sliding Window** (Dynamic size) using the **Two Pointers** technique.
