# Compare two fractions

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-compare-two-fractions4438` |
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
