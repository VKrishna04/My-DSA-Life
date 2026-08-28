# Return Length of Arguments Passed

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-return-length-of-arguments-passed` |
| Topics | Array, Math |
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

1. **Complexity**: 
   - **Time**: $O(N)$, where $N$ is the number of arguments. While accessing `.length` is $O(1)$, the `...args` syntax must iterate through and "gather" all passed values into a new array.
   - **Space**: $O(N)$. This syntax allocates a new array to store all arguments. Given your history with space complexity flags, note that this allocation grows linearly with input size.

2. **Correctness**: 
   The solution is robust. It correctly handles zero arguments (returning 0) and accommodates any data type (null, objects, or nested arrays) because the rest parameter captures everything passed to the function.

3. **Optimization**: 
   In standard functions (non-arrow), you can use the built-in `arguments` object: `return arguments.length;`. This avoids the overhead of creating a new array via the spread operator, making it more memory-efficient.

4. **Pattern**: 
   **Variadic Functions** (Rest Parameters).
