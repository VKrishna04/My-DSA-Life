# Return Length of Arguments Passed

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-return-length-of-arguments-passed` |
| Solved | 2024-08-11 |
| Runtime | 52 ms (beats 10.593999999999944%) |
| Memory | 48.7 MB (beats 100%) |

## Problem Statement

Write a function `argumentsLength` that returns the count of arguments passed to it.
 

**Example 1:**

**Input:** args = [5]
**Output:** 1
**Explanation:**
argumentsLength(5); // 1

One value was passed to the function so it should return 1.

**Example 2:**

**Input:** args = [{}, null, "3"]
**Output:** 3
**Explanation:** 
argumentsLength({}, null, "3"); // 3

Three values were passed to the function so it should return 3.

 

**Constraints:**

	- `args` is a valid JSON array

	- `0 <= args.length <= 100`

## Solutions

```JavaScript
/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    return args.length;
};

/**
 * argumentsLength(1, 2, 3); // 3
 */
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(1)$. Accessing the `length` property of an array is a constant time operation.
*   **Space Complexity:** $O(n)$. The rest parameter syntax (`...args`) spreads the arguments into a new array, requiring space proportional to the number of arguments passed.

### 2. Correctness
The code is **fully correct**. It adheres to ES6 standards and correctly handles:
*   **Zero arguments:** Returns `0`.
*   **Mixed types:** Correctly counts `null`, `undefined`, objects, and primitives.
*   **Large argument counts:** Limited only by the JavaScript engine's stack/memory limits.

### 3. Optimization
To optimize **space complexity** from $O(n)$ to $O(1)$, use the legacy `arguments` object. This avoids the allocation of a new array:
```javascript
var argumentsLength = function() {
    return arguments.length;
};
```
*Note: In modern engines, the performance difference is negligible for small inputs, but the `arguments` object exists by default without extra allocation.*

### 4. Key Algorithmic Pattern
**Rest Parameters (Variadic Function):** The pattern of using `...args` to capture an indefinite number of arguments into a single array structure.
