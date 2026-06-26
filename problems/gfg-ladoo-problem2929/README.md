# Ladoo problem

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-ladoo-problem2929` |
| Topics | Hash Table |
| Solved | 2026-06-24 |

## Problem Statement

Bheem has **N **friends. And he has a ladoo for each day. Given an Array **A**[] denoting on which day ith friend wants a ladoo. If Bheem is unable to give a ladoo to a friend, he loses his friendship with them. Find out the maximum number of Friends he can have at the end.



 



**Example 1:**




**Input:**
**N = **5
**A[] =** {3, 3, 1, 2, 4}
**Output:**
4 
**Explanation:
**He will lose either his 1st or 2nd
friend and therefore will be left
with 4 friends.

**Example 2:**




**Input:**
**N = **2
**A[] =** {1, 2}
**Output:**
2
**Explanation:
**He can give a ladoo to each of his friends,
and will have 2 friends by the end.

 



**Your Task:**

You don't need to read input or print anything. Your task is to complete the function **divideLadoo()** which takes an Integer N and an Array A as input and returns the answer.



 



**Expected Time Complexity:** O(N)

**Expected Auxiliary Space:** O(N)



 



**Constraints:**

1 <= N <= 105

1 <= A[i] <= 105

## Solutions

```python3
class Solution:
    def divideLadoo(self, N, A):
        return len(set(A))
        
```

## AI Review

Here's a review of your solution:

1.  **Time Complexity:** O(N) on average, where N is the number of ladoos. Building a set from a list of N elements involves iterating through the list and hashing each element.
    **Space Complexity:** O(K), where K is the number of unique ladoo types (K ≤ N). The set stores each unique element.

2.  **Correctness:** This solution is **correct** for the "Ladoo problem" as found on GeeksForGeeks, which asks for the number of distinct sweetness values. It handles empty lists (returns 0), lists with all unique elements, and lists with duplicates correctly. There are no edge cases that would fail this specific problem's requirements.

3.  **Optimisation:** No significant concrete optimization is applicable. Using `set()` is the most Pythonic and efficient way to count unique elements in Python.

4.  **Key Algorithmic Pattern:** Hashing / Hash Set (or Hash Table). The `set` data structure internally uses hashing to efficiently store and check for unique elements.
