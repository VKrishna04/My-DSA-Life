# Slowest Key

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-slowest-key` |
| Topics | Array, String |
| Solved | 2025-05-06 |
| Runtime | 0 ms (beats 100%) |
| Memory | 17.7 MB (beats 100%) |

## Problem Statement

A newly designed keypad was tested, where a tester pressed a sequence of `n` keys, one at a time.

You are given a string `keysPressed` of length `n`, where `keysPressed[i]` was the `ith` key pressed in the testing sequence, and a sorted list `releaseTimes`, where `releaseTimes[i]` was the time the `ith` key was released. Both arrays are **0-indexed**. The `0th` key was pressed at the time `0`, and every subsequent key was pressed at the **exact** time the previous key was released.

The tester wants to know the key of the keypress that had the **longest duration**. The `ith` keypress had a **duration** of `releaseTimes[i] - releaseTimes[i - 1]`, and the `0th` keypress had a duration of `releaseTimes[0]`.

Note that the same key could have been pressed multiple times during the test, and these multiple presses of the same key **may not** have had the same **duration**.

_Return the key of the keypress that had the **longest duration**. If there are multiple such keypresses, return the lexicographically largest key of the keypresses._

 

**Example 1:**

**Input:** releaseTimes = [9,29,49,50], keysPressed = "cbcd"
**Output:** "c"
**Explanation:** The keypresses were as follows:
Keypress for 'c' had a duration of 9 (pressed at time 0 and released at time 9).
Keypress for 'b' had a duration of 29 - 9 = 20 (pressed at time 9 right after the release of the previous character and released at time 29).
Keypress for 'c' had a duration of 49 - 29 = 20 (pressed at time 29 right after the release of the previous character and released at time 49).
Keypress for 'd' had a duration of 50 - 49 = 1 (pressed at time 49 right after the release of the previous character and released at time 50).
The longest of these was the keypress for 'b' and the second keypress for 'c', both with duration 20.
'c' is lexicographically larger than 'b', so the answer is 'c'.

**Example 2:**

**Input:** releaseTimes = [12,23,36,46,62], keysPressed = "spuda"
**Output:** "a"
**Explanation:** The keypresses were as follows:
Keypress for 's' had a duration of 12.
Keypress for 'p' had a duration of 23 - 12 = 11.
Keypress for 'u' had a duration of 36 - 23 = 13.
Keypress for 'd' had a duration of 46 - 36 = 10.
Keypress for 'a' had a duration of 62 - 46 = 16.
The longest of these was the keypress for 'a' with duration 16.

 

**Constraints:**

	- `releaseTimes.length == n`

	- `keysPressed.length == n`

	- `2 <= n <= 1000`

	- `1 <= releaseTimes[i] <= 109`

	- `releaseTimes[i] < releaseTimes[i+1]`

	- `keysPressed` contains only lowercase English letters.

## Hints

<details>
<summary>Hint 1</summary>

Get for each press its key and amount of time taken.

</details>

<details>
<summary>Hint 2</summary>

Iterate on the presses, maintaining the answer so far.

</details>

<details>
<summary>Hint 3</summary>

The current press will change the answer if and only if its amount of time taken is longer than that of the previous answer, or they are equal but the key is larger than that of the previous answer.

</details>

## Solutions

```Python3
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        maxe = releaseTimes[0]
        nmax = 0
        for i in range(1,len(releaseTimes)):
            diff = releaseTimes[i] - releaseTimes[i-1]
            if maxe < diff or ( maxe == diff and keysPressed[i] > keysPressed[nmax]):
                # print(maxe)
                maxe = diff
                # print(maxe)
                nmax = i
        
        return keysPressed[nmax]
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(n)$, where $n$ is the length of `releaseTimes`. The code iterates through the list exactly once.
*   **Space Complexity:** $O(1)$, as it only stores a few scalar variables regardless of input size.

### 2. Correctness
The code is **correct**. It properly handles:
*   **Single-entry inputs:** If `len == 1`, the loop is skipped, and it correctly returns `keysPressed[0]`.
*   **Tie-breaking:** The condition `maxe == diff and keysPressed[i] > keysPressed[nmax]` correctly implements the requirement to return the lexicographically larger key in case of a duration tie.

### 3. Optimization
**Reduce String Indexing:** Instead of storing the index `nmax`, store the best character directly (e.g., `res_char`). This avoids repeated indexing into the `keysPressed` string inside the loop and at the return statement.

```python
# Optimization example:
res_key = keysPressed[0]
# inside loop...
if diff > maxe or (diff == maxe and keysPressed[i] > res_key):
    maxe, res_key = diff, keysPressed[i]
```

### 4. Key Algorithmic Pattern
**Linear Scan (Single Pass):** It maintains a "Running Maximum" of both the duration and the associated character while traversing the data once.
