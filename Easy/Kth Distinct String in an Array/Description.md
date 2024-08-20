## Challenge 2053: Kth Distinct String in an Array

**Problem:**
Given an array of strings `arr` and an integer `k`, find the `k`th distinct string in `arr`. A string is considered distinct if it appears only once in the array. If there are fewer than `k` distinct strings, return an empty string `""`.

## Examples:

 **Example 1:**
 
 - **Input:** `arr = ["d","b","c","b","c","a"]`, `k = 2`
 - **Output:** `"a"`
 - **Explanation:** The distinct strings are `"d"` and `"a"`. The 2nd distinct string is `"a"`.

 **Example 2:**
 
 - **Input:** `arr = ["aaa","aa","a"]`, `k = 1`
 - **Output:** `"aaa"`
 - **Explanation:** All strings are distinct, so the 1st string `"aaa"` is returned.

 **Example 3:**
 
 - **Input:** `arr = ["a","b","a"]`, `k = 3`
 - **Output:** `""`
 - **Explanation:** The only distinct string is `"b"`. Since there are fewer than 3 distinct strings, return `""`.

## Constraints:

- 1 <= `k` <= `arr.length` <= 1000
- 1 <= `arr[i].length` <= 5
- `arr[i]` consists of lowercase English letters.
