# Sort 0s, 1s and 2s

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-sort-an-array-of-0s-1s-and-2s4231` |
| Topics | Arrays, Sorting, Data Structures, Algorithms |
| Solved | 2026-06-24 |

## Solutions

```Python3
class Solution:
    def sort012(self, arr):
        l, m, h = 0, 0, len(arr) - 1
        while m <= h:
            if arr[m] == 0:
                arr[l], arr[m] = arr[m], arr[l]
                l += 1
                m += 1
            elif arr[m] == 1:
                m += 1
            else:
                arr[m], arr[h] = arr[h], arr[m]
                h -= 1
```
