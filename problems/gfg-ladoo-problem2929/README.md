# Ladoo problem

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-ladoo-problem2929` |
| Topics | Hash, Data Structures |
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

```Python3
class Solution:
    def divideLadoo(self, N, A):
        return len(set(A))
        
```

## AI Review

### Review

**Complexity:**
*   **Time Complexity:** $O(N)$, where $N$ is the number of elements in array $A$. Converting a list to a set requires a single pass to hash each element.
*   **Space Complexity:** $O(N)$ in the worst case (where all elements are unique) to store the set in memory.

**Correctness:**
The logic is correct for finding the number of distinct elements.
*   **Edge Cases:** It correctly handles an empty list (returns 0) and a list where all elements are the same (returns 1). 

**Optimization:**
The solution is already time-optimal ($O(N)$). If memory is a critical constraint and the input list can be modified, you could sort the array in-place ($O(N \log N)$ time) and iterate through it to count unique adjacent elements, reducing auxiliary space to $O(1)$. However, in Python, the current `set()` approach is the most idiomatic and fastest for general use.

**Key Algorithmic Pattern:**
Hashing (using a Set data structure to filter duplicates).
