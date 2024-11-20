# Smallest Number in Infinite Set

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-smallest-number-in-infinite-set` |
| Topics | Hash Table, Design, Heap (Priority Queue), Ordered Set |
| Solved | 2025-09-20 |
| Runtime | 22 ms (beats 45.25490000000001%) |
| Memory | 18.5 MB (beats 100%) |

## Problem Statement

You have a set which contains all positive integers `[1, 2, 3, 4, 5, ...]`.

Implement the `SmallestInfiniteSet` class:

	- `SmallestInfiniteSet()` Initializes the **SmallestInfiniteSet** object to contain **all** positive integers.

	- `int popSmallest()` **Removes** and returns the smallest integer contained in the infinite set.

	- `void addBack(int num)` **Adds** a positive integer `num` back into the infinite set, if it is **not** already in the infinite set.

 

**Example 1:**

**Input**
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]
**Output**
[null, null, 1, 2, 3, null, 1, 4, 5]

**Explanation**
SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
                                   // is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.

 

**Constraints:**

	- `1 <= num <= 1000`

	- At most `1000` calls will be made **in total** to `popSmallest` and `addBack`.

## Hints

<details>
<summary>Hint 1</summary>

Based on the constraints, what is the maximum element that can possibly be popped?

</details>

<details>
<summary>Hint 2</summary>

Maintain whether elements are in or not in the set. How many elements do we consider?

</details>

## Solutions

```Python3
class SmallestInfiniteSet:

    def __init__(self):
        self.sm = 1
        self.rm = set()

    def popSmallest(self) -> int:
        ans = self.sm
        self.rm.add(ans)
        while self.sm in self.rm:
            self.sm += 1
        return ans

    def addBack(self, num: int) -> None:
        if num in self.rm:
            self.rm.remove(num)
            if num < self.sm:
                self.sm = num


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
```

## AI Review

### 1. Complexity
*   **Time Complexity:** 
    *   `popSmallest`: **$O(N)$** worst-case (where $N$ is the number of elements added back), as the `while` loop may iterate through the `rm` set.
    *   `addBack`: **$O(1)$** average (set operations).
*   **Space Complexity:** **$O(N)$** to store the `rm` set.

### 2. Correctness
The logic is **correct**. It handles the "infinite" nature by using a pointer (`sm`) and tracks exceptions in a set. 
*   **Edge Cases:** If `addBack` is called for a number already present in the "infinite" portion (i.e., `num >= self.sm`), it correctly ignores it because `num` won't be in `self.rm`.

### 3. Optimization
While your solution passes due to small constraints ($1000$ calls), the $O(N)$ `popSmallest` is inefficient.
**Optimization:** Use a **Min-Heap** combined with a **Set** to track "added-back" numbers specifically.
*   Keep an integer `threshold` (starting at 1) for the infinite sequence.
*   Only store numbers in the heap if they are `< threshold`.
*   `popSmallest`: If heap exists, pop min; otherwise, return `threshold` and increment it.
*   This reduces `popSmallest` to **$O(\log N)$**.

### 4. Key Algorithmic Pattern
**Design with auxiliary data structures** (using a Set/Heap to track deviations from a contiguous range).
