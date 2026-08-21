# Buy Stock

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-buy-stock-2` |
| Topics | Greedy, Array |
| Solved | 2026-06-24 |

## Problem Statement

Given an array **prices[]** of non-negative integers, representing the prices of the stocks on different days. The task is to find the maximum profit possible by buying and selling the stocks on different days when **at most one **transaction is allowed. Here one transaction means 1 buy + 1 Sell. If it is not possible to make a profit then **return 0**.

Note: Stock must be bought before being sold.

**Examples:**

**Input: **prices[] = [7, 10, 1, 3, 6, 9, 2]
**Output:** 8
**Explanation:** You can buy the stock on day 2 at price = 1 and sell it on day 5 at price = 9. Hence, the profit is 8.
**Input: **prices[] = [7, 6, 4, 3, 1]
**Output:** 0 
**Explanation****:** Here the prices are in decreasing order, hence if we buy any day then we cannot sell it at a greater price. Hence, the answer is 0.

**Input: **prices[] = [1, 3, 6, 9, 11]
**Output:** 10 
**Explanation****:** Since the array is sorted in increasing order, we can make maximum profit by buying at price[0] and selling at price[n-1].
**Constraint:**
1 &le;  prices.size() &le;  105
0 &le;  prices[i] &le;  104

## Solutions

```python3
class Solution:
    def maxProfit(self, prices):
        minp = prices[0]
        ans = 0
        
        for i in range(len(prices)):
            minp = min(minp, prices[i])
            ans = max(ans, prices[i]-minp)
            
        return ans
```

## AI Review

### Analysis

*   **Time Complexity**: **$O(n)$**, where $n$ is the length of the `prices` array. We iterate through the list exactly once.
*   **Space Complexity**: **$O(1)$**. We only maintain two scalar variables (`minp` and `ans`) regardless of input size. 
*   **Correctness**: This code will **crash** on an empty list input (`prices = []`) with an `IndexError` at `prices[0]`. This is a recurring flag for you; always validate if the input exists before accessing indices. It correctly handles cases with no profit (returns 0).
*   **Concrete Optimization**: Add a guard clause for empty inputs and start the loop from the second element to skip the redundant first comparison:
    ```python3
    if not prices: return 0
    minp = prices[0]
    for i in range(1, len(prices)): # Start at index 1
        # ... logic ...
    ```
*   **Key Algorithmic Pattern**: **Greedy**. At each step, you make the locally optimal choice (updating the lowest buy price seen so far) to calculate the potential maximum global profit.
