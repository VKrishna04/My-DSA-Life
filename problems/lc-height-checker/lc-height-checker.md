# Height Checker

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-height-checker` |
| Topics | Array, Sorting, Counting Sort |
| Solved | 2024-09-19 |
| Runtime | 2 ms (beats 87.05189999999999%) |
| Memory | 41.5 MB (beats 100%) |

## Problem Statement

A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in **non-decreasing order** by height. Let this ordering be represented by the integer array `expected` where `expected[i]` is the expected height of the `ith` student in line.

You are given an integer array `heights` representing the **current order** that the students are standing in. Each `heights[i]` is the height of the `ith` student in line (**0-indexed**).

Return _the **number of indices** where _`heights[i] != expected[i]`.

 

**Example 1:**

**Input:** heights = [1,1,4,2,1,3]
**Output:** 3
**Explanation:** 
heights:  [1,1,4,2,1,3]
expected: [1,1,1,2,3,4]
Indices 2, 4, and 5 do not match.

**Example 2:**

**Input:** heights = [5,1,2,3,4]
**Output:** 5
**Explanation:**
heights:  [5,1,2,3,4]
expected: [1,2,3,4,5]
All indices do not match.

**Example 3:**

**Input:** heights = [1,2,3,4,5]
**Output:** 0
**Explanation:**
heights:  [1,2,3,4,5]
expected: [1,2,3,4,5]
All indices match.

 

**Constraints:**

	- `1 <= heights.length <= 100`

	- `1 <= heights[i] <= 100`

## Solutions

```Java
import java.util.Arrays;

class Solution {
    public int heightChecker(int[] heights) {
        int j = 0;
        int length = heights.length;
        int[] results = new int[length];
        int[] expected = Arrays.copyOf(heights, length);

        Arrays.sort(expected);

        for (int i = 0; i < length; i++) {
            if (expected[i] != heights[i]) {
                results[j++] = i;
            }
        }

        // if(j==0){
        // System.out.println("All indices do not match.");
        // }else if (j==length){
        // System.out.println("All indices match.");
        // return 0;
        // }else{
        // System.out.print("Indices ");
        // for(int i=0;i<j-1;i++){
        // System.out.print(results[i]+", ");
        // }
        // System.out.print("and "+results[j-1]+ " do not match.");

        return j;
    }
}
```

## AI Review

### Analysis

**1. Complexity**
*   **Time:** $O(N \log N)$ due to `Arrays.sort()`, where $N$ is the length of the array. The final loop is $O(N)$.
*   **Space:** $O(N)$ to store the `expected` and `results` arrays.

**2. Correctness**
The logic is correct. It creates a sorted version of the input and counts the discrepancies.
*   **Edge Cases:** Handles empty arrays (returns 0), already sorted arrays (returns 0), and all-identical elements correctly. 
*   **Note:** The `results` array is allocated but only its counter `j` is used for the return value; this is redundant memory usage.

**3. Optimization**
Since the problem constraints usually specify heights are between 1 and 100, you can use **Counting Sort** (Bucket Sort) to achieve **$O(N)$ time** and **$O(1)$ extra space** (excluding the frequency array of size 101). Simply count occurrences of each height and iterate through the counts to compare with the original array.

**4. Key Algorithmic Pattern**
**Comparison via Sorting:** Creating a reference (sorted) state to identify elements out of their natural order.
