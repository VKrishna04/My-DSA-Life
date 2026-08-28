# Camelcase Pattern Matching

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-camelcase-pattern-matching2259` |
| Topics | String, Trie, Advanced Data Structure |
| Solved | 2026-06-24 |

## Problem Statement

Given a dictionary of words `arr[]` where each word follows **PascalCase notation**, print all words in the dictionary that match with a given pattern `pat` consisting of uppercase characters only. **PascalCase** is the practice of writing compound words or phrases such that each word or abbreviation begins with a capital letter. 
i.e. PowerPoint, Wikipedia, GeeksForGeeks, CodeBlocks, etc.

 

A word matches the pattern if the sequence of its uppercase letters, when concatenated, forms a string that has `pat` as a prefix.

Note: The driver code will sort your answer before checking and return the answer in any order.

**Examples:**

**Input: **arr[] = ["WelcomeGeek", "WelcomeToGeeksForGeeks", "GeeksForGeeks"], pat = "WTG"
**Output: **["WelcomeToGeeksForGeeks"]
**Explanation: **Since only "WelcomeToGeeksForGeeks" matches the pattern, it is the only answer.
**Input: **arr[] = ["Hi", "Hello", "HelloWorld", "HiTech", "HiGeek", "HiTechWorld", "HiTechCity", "HiTechLab"], pat = "HA"
**Output: **[]
**Explanation: **None of the words matches the given pattern.
**Constraints:**
1 &le; arr.size() &le; 1000
1 &le; pat.size() &le; 100
1 &le; arr[i].size() &le; 100

## AI Review

1. **Complexity**: Time complexity is $O(N \times L)$, where $N$ is the number of words and $L$ is the maximum length of a word. Space complexity is $O(N \times L)$ to store the output list, with $O(L)$ auxiliary space for the temporary string `curr`.

2. **Correctness**: The solution is logically correct but inefficient. Using `pat in curr[:len(pat)]` is an indirect way of checking `curr.startswith(pat)`. It correctly handles the "pascalCase" logic by filtering for uppercase characters first.

3. **Optimisation**: **Early Exit**. Instead of extracting every uppercase character into a new string (which hits your recurring space complexity flag), compare the word's uppercase letters against `pat` character-by-character. If an uppercase letter doesn't match the current index of `pat`, or if you finish the word before matching `pat`, you can immediately skip to the next word. This reduces auxiliary space to $O(1)$.

4. **Pattern**: String Filtering / Prefix Matching. While a **Trie** is the optimal structure for multiple pattern queries, a linear scan with early exit is sufficient for a single pattern.
