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

### Notes

- Your algorithm should run in O(n) time complexity.
- You should use only constant extra space.

