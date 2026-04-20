# Solving Questions With Brainpower

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-solving-questions-with-brainpower` |
| Topics | Array, Dynamic Programming |
| Solved | 2026-04-20 |
| Runtime | 67 ms (beats 46.84690000000004%) |
| Memory | 55.8 MB (beats 95.8816%) |

## Problem Statement

You are given a **0-indexed** 2D integer array `questions` where `questions[i] = [pointsi, brainpoweri]`.

The array describes the questions of an exam, where you have to process the questions **in order** (i.e., starting from question `0`) and make a decision whether to **solve** or **skip** each question. Solving question `i` will **earn** you `pointsi` points but you will be **unable** to solve each of the next `brainpoweri` questions. If you skip question `i`, you get to make the decision on the next question.

	- For example, given `questions = [[3, 2], [4, 3], [4, 4], [2, 5]]`:

	
		If question `0` is solved, you will earn `3` points but you will be unable to solve questions `1` and `2`.

		- If instead, question `0` is skipped and question `1` is solved, you will earn `4` points but you will be unable to solve questions `2` and `3`.

	
	

Return _the **maximum** points you can earn for the exam_.

 

**Example 1:**

**Input:** questions = [[3,2],[4,3],[4,4],[2,5]]
**Output:** 5
**Explanation:** The maximum points can be earned by solving questions 0 and 3.
- Solve question 0: Earn 3 points, will be unable to solve the next 2 questions
- Unable to solve questions 1 and 2
- Solve question 3: Earn 2 points
Total points earned: 3 + 2 = 5. There is no other way to earn 5 or more points.

**Example 2:**

**Input:** questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
**Output:** 7
**Explanation:** The maximum points can be earned by solving questions 1 and 4.
- Skip question 0
- Solve question 1: Earn 2 points, will be unable to solve the next 2 questions
- Unable to solve questions 2 and 3
- Solve question 4: Earn 5 points
Total points earned: 2 + 5 = 7. There is no other way to earn 7 or more points.

 

**Constraints:**

	- `1 <= questions.length <= 105`

	- `questions[i].length == 2`

	- `1 <= pointsi, brainpoweri <= 105`

## Solutions

```Python3
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        l = len(questions)
        dp = [0]*(l+1)
        for i in range(l-1,-1,-1):
            skip = dp[min(l-1,i+1)]
            nexti = i + questions[i][1] + 1
            solve = questions[i][0] + dp[min(l, nexti)]
            dp[i] = max(skip,solve)
        return dp[0]
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(n)$, where $n$ is the number of questions. We iterate through the list exactly once.
*   **Space Complexity:** $O(n)$ to store the `dp` array.

### 2. Correctness
The solution is **correct**. It properly handles the two choices at each step (solve or skip) and uses a suffix DP approach to ensure subproblems are solved before they are needed. The `min(l, nexti)` logic correctly handles cases where the "brainpower" skip exceeds the array bounds.

### 3. Concrete Optimisation
In the line `skip = dp[min(l-1, i+1)]`, the `min` call is unnecessary because `i + 1` will never exceed `l` in a loop ranging to 0. It can be simplified to `skip = dp[i+1]`. This reduces overhead slightly and improves readability.

### 4. Key Algorithmic Pattern
**Dynamic Programming (Bottom-Up/Tabulation)**. Specifically, it uses **Suffix DP**, calculating the maximum points possible from index $i$ to the end of the array based on previously computed results for indices $j > i$.
