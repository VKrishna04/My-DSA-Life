# Nearly Sorted

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-nearly-sorted-1587115620` |
| Topics | Sorting, Array, Heap (Priority Queue) |
| Solved | 2026-06-24 |

## Problem Statement

Given an array **arr[]**, where each element is at most **k positions away** from its correct position in the sorted order.
Your task is to **restore **the sorted order of arr[] by rearranging the elements **in place**.

**Note:** Don't use any sort() method.

**Examples:**

**Input:** arr[] = [2, 3, 1, 4], k = 2
**Output: **[1, 2, 3, 4]**
Explanation: **All elements are at most k = 2 positions away from their correct positions.
Element 1 moves from index 2 to 0
Element 2 moves from index 0 to 1
Element 3 moves from index 1 to 2
Element 4 stays at index 3
**Input:** arr[]= [7, 9, 14], k = 1
**Output: **[7, 9, 14]
**Explanation: **All elements are already stored in the sorted order.
**Constraints:**
1 &le; arr.size() &le; 106
0 &le; k < arr.size()
1 &le; arr[i] &le; 106

## Solutions

```python3
from heapq import heapify, heappush, heappop

class Solution:
    def nearlySorted(self, arr, k):  
        heap = arr[:k]
        heapify(heap)
        index = 0
        for i in range(k,len(arr)):
            heappush(heap,arr[i])
            arr[index] = heappop(heap)
            index += 1
        
        for j in range(k):
            arr[index] = heappop(heap)
            index += 1
            
        return arr
```

## AI Review

### Analysis
**1. Complexity**
*   **Time:** $O(N \log K)$, where $N$ is the array length. Each of the $N$ elements is inserted into and removed from a heap of size $K+1$.
*   **Space:** $O(K)$ to maintain the priority queue. This is efficient given your history of space complexity flags.

**2. Correctness**
The logic is sound. For an element at index $i$ to be at most $k$ positions away, its correct value must be within the range $[i-k, i+k]$. By maintaining a heap of size $k+1$, you ensure the smallest available element for the current index is always present. 
*   **Edge Cases:** Works for $k=0$ (already sorted) and $k \geq \text{len}(arr)$ (equivalent to heap sort).

**3. Optimization**
Use `heapq.heapreplace(heap, arr[i])` inside the loop instead of `heappush` followed by `heappop`. `heapreplace` is more efficient as it performs both operations in a single $O(\log K)$ down-heap pass.

**4. Key Algorithmic Pattern**
**Sliding Window with a Priority Queue**: Using a heap to maintain a "moving window" of candidates to find the minimum for the current position.
