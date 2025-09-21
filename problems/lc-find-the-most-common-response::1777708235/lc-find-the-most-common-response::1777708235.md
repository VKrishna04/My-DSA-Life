# Find the Most Common Response

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-find-the-most-common-response::1777708235` |
| Topics | Array, Hash Table, String, Counting |
| Solved | 2025-09-21 |
| Runtime | 1051 ms (beats 5.081900000000191%) |
| Memory | 298.2 MB (beats 5.08360000000005%) |

## Problem Statement

You are given a 2D string array `responses` where each `responses[i]` is an array of strings representing survey responses from the `ith` day.

Return the **most common** response across all days after removing **duplicate** responses within each `responses[i]`. If there is a tie, return the _lexicographically smallest_ response.

 

**Example 1:**

**Input:** responses = [["good","ok","good","ok"],["ok","bad","good","ok","ok"],["good"],["bad"]]

**Output:** "good"

**Explanation:**

	- After removing duplicates within each list, `responses = [["good", "ok"], ["ok", "bad", "good"], ["good"], ["bad"]]`.

	- `"good"` appears 3 times, `"ok"` appears 2 times, and `"bad"` appears 2 times.

	- Return `"good"` because it has the highest frequency.

**Example 2:**

**Input:** responses = [["good","ok","good"],["ok","bad"],["bad","notsure"],["great","good"]]

**Output:** "bad"

**Explanation:**

	- After removing duplicates within each list we have `responses = [["good", "ok"], ["ok", "bad"], ["bad", "notsure"], ["great", "good"]]`.

	- `"bad"`, `"good"`, and `"ok"` each occur 2 times.

	- The output is `"bad"` because it is the lexicographically smallest amongst the words with the highest frequency.

 

**Constraints:**

	- `1 <= responses.length <= 1000`

	- `1 <= responses[i].length <= 1000`

	- `1 <= responses[i][j].length <= 10`

	- `responses[i][j]` consists of only lowercase English letters

## Solutions

```Python3
from collections import Counter
class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        ans = []
        for i in responses:
            ans.extend(set(i))
        # print(ans)
        count = Counter(ans)
        # print(count)
        a = sorted(count.items(), key=lambda x: (-x[1], x[0]))
        # print(a)
        return a[0][0]
```
