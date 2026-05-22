# Create Hello World Function

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-create-hello-world-function` |
| Topics | Higher-Order Functions, Closures, Functional Programming |
| Solved | 2024-10-23 |
| Runtime | 55 ms (beats 5%) |
| Memory | 49 MB (beats 100%) |

## Problem Statement

Write a function `createHelloWorld`. It should return a new function that always returns `"Hello World"`.
 

**Example 1:**

**Input:** args = []
**Output:** "Hello World"
**Explanation:**
const f = createHelloWorld();
f(); // "Hello World"

The function returned by createHelloWorld should always return "Hello World".

**Example 2:**

**Input:** args = [{},null,42]
**Output:** "Hello World"
**Explanation:**
const f = createHelloWorld();
f({}, null, 42); // "Hello World"

Any arguments could be passed to the function but it should still always return "Hello World".

 

**Constraints:**

	- `0 <= args.length <= 10`

## Solutions

```JavaScript
/**
 * @return {Function}
 */
var createHelloWorld = function() {
    
    return function(...args) {
        return "Hello World";
    }
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */
```

## AI Review

### Review

1. **Complexity**: 
   - **Time Complexity**: $O(1)$. Both the creation of the function and its execution take constant time, regardless of the number or size of arguments passed.
   - **Space Complexity**: $O(1)$. No additional data structures are scaled with input; the returned string is constant.

2. **Correctness**: 
   The solution is perfectly correct. By using the rest parameter (`...args`), it captures any number of arguments passed to the returned function and successfully ignores them to return the required string. It handles edge cases like zero arguments or null/undefined inputs implicitly.

3. **Optimization**: 
   While the current solution is optimal, you can slightly reduce memory overhead by removing the `...args` parameter: `return function() { return "Hello World"; };`. In JavaScript, functions can be called with any number of arguments even if none are defined in the signature, avoiding the allocation of an arguments array.

4. **Key Algorithmic Pattern**: 
   **Higher-Order Functions** and **Closures**. The outer function returns a new function that maintains its own scope.
