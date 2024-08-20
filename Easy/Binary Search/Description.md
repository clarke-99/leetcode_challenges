## Challenge 704: Binary Search

**Problem:**
Given a sorted array of integers `nums` and an integer `target`, implement a function to find the index of `target` in `nums`. If `target` is not found, return `-1`. The algorithm should have a runtime complexity of O(log n).

## Examples:

 **Example 1:**
 
- **Input:** `nums = [-1,0,3,5,9,12]`, `target = 9`
- **Output:** `4`
- **Explanation:** `9` is found at index `4` in `nums`.

 **Example 2:**
 - **Input:** `nums = [-1,0,3,5,9,12]`, `target = 2`
 - **Output:** `-1`
 - **Explanation:** `2` is not present in `nums`, so return `-1`.

## Constraints:

- 1 <= `nums.length` <= 10^4
- -10^4 < `nums[i]`, `target` < 10^4
- All integers in `nums` are unique.

