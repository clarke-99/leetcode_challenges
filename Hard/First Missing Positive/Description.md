## Challenge 41. First Missing Positive

**Problem:** Given an unsorted integer array `nums`, return the smallest positive integer that is not present in `nums`. You must implement an algorithm that runs in `O(n)` time and uses `O(1)` auxiliary space.

## Examples

**Example 1:**

- **Input:** `nums = [1,2,0]`
- **Output:** `3`
- **Explanation:** The numbers in the range `[1, 2]` are all in the array, so the smallest missing positive integer is `3`.

**Example 2:**

- **Input:** `nums = [3,4,-1,1]`
- **Output:** `2`
- **Explanation:** The number `1` is in the array, but `2` is missing.

**Example 3:**

- **Input:** `nums = [7,8,9,11,12]`
- **Output:** `1`
- **Explanation:** The smallest positive integer `1` is missing from the array.

## Constraints

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`

## Approach 

Initially, I tried to use the sort method, and then iterate through the sorted array. The idea was if there was a non-consecutive number it has to be the smallest missing value; this method did work, but it does not satisfy the time or space complexity requirements for this challenge. I instead choose to sort the array in place and then find the non-consecutive number. 

1. **Modify Array In-Place**
   - First, I filtered the positive integers in the array. Numbers outside the `range [1, n]` are not useful for finding the smallest missing positive integer.
   - For each number that is within the `range [1, n]`, place it in its correct position by swapping. If `nums[i]` is a positive integer, place `nums[i]` in the index `nums[i] - 1`.
   - This step is done in-place, which avoids additional space complexity and helps in maintaining  𝑂(𝑛) time complexity.

2. **Find Missing Positive Integer**
   - After sorting the numbers, iterate through the array. The first index `i` where the value `nums[i]` does not match `i + 1` indicates that `i + 1` is the smallest missing positive integer.
   - If all indices contain the correct values from 1 to n, then the smallest missing positive integer is `n + 1`.

