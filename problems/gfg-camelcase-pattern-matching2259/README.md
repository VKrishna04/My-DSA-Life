# Camelcase Pattern Matching

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-camelcase-pattern-matching2259` |
| Topics | Strings, Trie, Data Structures, Advanced Data Structure |
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
