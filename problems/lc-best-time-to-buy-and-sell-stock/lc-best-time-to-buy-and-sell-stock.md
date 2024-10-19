# Best Time to Buy and Sell Stock

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-best-time-to-buy-and-sell-stock` |
| Topics | Array, Dynamic Programming |
| Solved | 2024-10-19 |
| Runtime | 21 ms (beats 94.6538%) |
| Memory | 26.1 MB (beats 99.9985%) |

## Problem Statement

You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return _the maximum profit you can achieve from this transaction_. If you cannot achieve any profit, return `0`.

 

**Example 1:**

**Input:** prices = [7,1,5,3,6,4]
**Output:** 5
**Explanation:** Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

**Example 2:**

**Input:** prices = [7,6,4,3,1]
**Output:** 0
**Explanation:** In this case, no transactions are done and the max profit = 0.

 

**Constraints:**

	- `1 <= prices.length <= 105`

	- `0 <= prices[i] <= 104`

## Solutions

```Python3
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit
```

## AI Review

**1. Complexity**
*   **Time Complexity:** $O(N)$, where $N$ is the number of prices. We iterate through the list exactly once.
*   **Space Complexity:** $O(1)$, as we only store two scalar variables (`min_price` and `max_profit`) regardless of input size.

**2. Correctness**
The solution is **correct** and handles all standard edge cases:
*   **Empty or single-element list:** Returns 0 (correct, as no profit can be made).
*   **Descending prices:** `max_profit` remains 0 (correct, as you shouldn't buy/sell).
*   **Large price gaps:** Correct buyers' logic by tracking the global minimum encountered so far.

**3. Optimization**
While the logic is already $O(N)$, you can improve **readability** by using Python’s built-in `min` and `max` functions. This often translates to faster execution in CPython for larger datasets:
```python
for price in prices:
    min_price = min(min_price, price)
    max_profit = max(max_profit, price - min_price)
```

**4. Key Algorithmic Pattern**
*   **Greedy Algorithm:** At each step, we make the locally optimal choice (tracking the lowest price seen so far) to find the global maximum profit.
*   It is also a simplified variation of **Kadane’s Algorithm**.
