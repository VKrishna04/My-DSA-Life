# Best Time to Buy and Sell Stock

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-best-time-to-buy-and-sell-stock` |
| Topics | Array, Dynamic Programming |
| Solved | 2024-10-19 |
| Runtime | 1 ms (beats 99.9206%) |
| Memory | 61.6 MB (beats 99.90949999999998%) |

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

```Java
class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE;
        int maxProfit = 0;

        for (int price : prices) {
            if (price < minPrice) {
                minPrice = price;
            } else if (price - minPrice > maxProfit) {
                maxProfit = price - minPrice;
            }
        }

        return maxProfit;
    }
}

```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(n)$, where $n$ is the length of the `prices` array. The algorithm performs a single pass.
*   **Space Complexity:** $O(1)$. It uses only two scalar variables regardless of input size.

### 2. Correctness
The solution is **correct** and handles all standard edge cases:
*   **Empty or single-element array:** The loop completes, returning the initial `maxProfit` of 0.
*   **Strictly decreasing prices:** `minPrice` updates, but the `else if` never triggers, returning 0 (no profit possible).
*   **Price volatility:** Correctly tracks the lowest price seen *so far* to calculate the potential profit at each step.

### 3. Optimization
The solution is already **optimally efficient** in terms of Big-O. For code readability, you could use `Math.min()` and `Math.max()`:
```java
minPrice = Math.min(minPrice, price);
maxProfit = Math.max(maxProfit, price - minPrice);
```
However, your current `if-else` structure is slightly more performant as it avoids calculating `price - minPrice` when a new `minPrice` is found.

### 4. Key Algorithmic Pattern
**One Pass / Greedy:** It makes the locally optimal choice (tracking the minimum price found so far) to find the global maximum profit in a single traversal.
