# Compare two fractions

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-compare-two-fractions4438` |
| Topics | String Parsing, Mathematics, Cross Multiplication |
| Solved | 2026-06-23 |

## Solutions

```Python3
class Solution:
    def compareFrac(self, str_val):
        fracs = str_val.split(", ")
        f1_num, f1_den = map(int, fracs[0].split("/"))
        f2_num, f2_den = map(int, fracs[1].split("/"))
        
        val1 = f1_num / f1_den
        val2 = f2_num / f2_den
        
        if val1 > val2:
            return fracs[0]
        elif val2 > val1:
            return fracs[1]
        else:
            return "equal"
```

## AI Review

### Analysis

1. **Complexity**
   * **Time Complexity:** $O(N)$, where $N$ is the length of the input string. Splitting the string and parsing integers both take linear time.
   * **Space Complexity:** $O(N)$ to store the split substrings and integer values.

2. **Correctness**
   The solution uses **floating-point division**, which is risky. For very large numerators/denominators or fractions that are nearly identical (e.g., differing at the 16th decimal place), precision errors can lead to incorrect comparisons. 

3. **Optimization**
   Use **cross-multiplication** to compare fractions using integers only, avoiding precision issues. 
   Instead of `f1_num / f1_den > f2_num / f2_den`, compare `f1_num * f2_den > f2_num * f1_den`. This is mathematically equivalent ($a/b > c/d \iff ad > bc$) and 100% accurate for integers.

4. **Key Algorithmic Pattern**
   **String Parsing** and **Basic Arithmetic**. The problem focuses on extracting numerical data from a formatted string and applying comparative logic.
