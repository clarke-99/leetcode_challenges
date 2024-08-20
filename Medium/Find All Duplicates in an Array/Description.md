## Challenge 442. Find All Duplicates in an Array

**Problem:** Given an integer array `nums` of length `n` where all the integers are in the range `[1, n]` and each integer appears once or twice, return an array containing all the integers that appear exactly twice.

## Examples

**Example 1:**

- **Input:** `nums = [4,3,2,7,8,2,3,1]`
- **Output:** `[2, 3]`
- **Explanation:**
  - The number 2 appears twice.
  - The number 3 appears twice.

**Example 2:**

- **Input:** `nums = [1,1,2]`
- **Output:** `[1]`
- **Explanation:**
  - The number 1 appears twice.

**Example 3:**

- **Input:** `nums = [1]`
- **Output:** `[]`
- **Explanation:**
  - No numbers appear twice.

## Constraints

- `n == nums.length`
- `1 <= n <= 10^5`
- `1 <= nums[i] <= n`
- Each element in `nums` appears once or twice.
- Your algorithm should run in O(n) time complexity.
- You should use only constant extra space.

## Approach

The approach utilises the fact that the `num` in nums can be used as indices to track which elements have been seen. Here’s how the algorithm works:

1. **Iterate**
   - For each `num` in the array, calculate abs(`num`) and subtract 1 to account for zero-indexing.

2. **Check and Mark**
   - Check the value at the index calculated:
     -- If *positive*, change the value in the array to be negative, this marks the `num` as seen.
     -- If *negative*, the value has been seen and you can add the `num` to the list of `duplicates`


