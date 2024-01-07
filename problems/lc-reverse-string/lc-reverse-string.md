# Reverse String

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-reverse-string` |
| Topics | Two Pointers, String |
| Solved | 2024-01-07 |
| Runtime | 21 ms (beats 2.0054999999999943%) |
| Memory | 23.9 MB (beats 100%) |

## Problem Statement

Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array in-place with `O(1)` extra memory.

 

**Example 1:**

**Input:** s = ["h","e","l","l","o"]
**Output:** ["o","l","l","e","h"]
**Example 2:**

**Input:** s = ["H","a","n","n","a","h"]
**Output:** ["h","a","n","n","a","H"]

 

**Constraints:**

	- `1 <= s.length <= 105`

	- `s[i]` is a printable ascii character.

## Solutions

```C++
class Solution {
public:
    void reverseString(vector<char>& s) {
        reverse(s, 0, s.size() - 1);
    }
private:
    void reverse(vector<char>& s, int left, int right) {
        if (left < right) {
            swap(s[left], s[right]);
            reverse(s, left + 1, right - 1);
        }
    }
};
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(n)$, where $n$ is the length of the string. Every element is visited once.
*   **Space Complexity:** $O(n)$ due to the recursion stack. Since each call processes two characters, the stack depth is $n/2$.

### 2. Correctness
The logic is correct and handles edge cases well:
*   **Empty string:** `s.size() - 1` results in `-1`. The condition `left < right` (0 < -1) correctly skips execution.
*   **Single character:** `left` equals `right`, so no swap occurs.
*   **Even/Odd lengths:** Correctly terminates when pointers meet or cross.

### 3. Optimization
**Convert to an iterative approach.**
The current recursive solution uses $O(n)$ auxiliary space, which violates the common LeetCode constraint of $O(1)$ extra space for this problem. Replace recursion with a `while` loop:

```cpp
void reverseString(vector<char>& s) {
    int left = 0, right = s.size() - 1;
    while (left < right) {
        swap(s[left++], s[right--]);
    }
}
```
This reduces space complexity to **$O(1)$**.

### 4. Key Algorithmic Pattern
**Two Pointers:** Using two indices starting at opposite ends and moving toward the center.
