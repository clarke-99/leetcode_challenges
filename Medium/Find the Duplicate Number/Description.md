## Challenge 287. Find the Duplicate Number

**Problem:** Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive, return the duplicate number that appears more than once.

## Examples

**Example 1:**

- **Input:** `nums = [1,3,4,2,2]`
- **Output:** `2`
- **Explanation:** The number 2 appears more than once.

**Example 2:**

- **Input:** `nums = [3,1,3,4,2]`
- **Output:** `3`
- **Explanation:** The number 3 appears more than once.

**Example 3:**

- **Input:** `nums = [3,3,3,3,3]`
- **Output:** `3`
- **Explanation:** The number 3 is the only number that repeats.

## Constraints

- `1 <= n <= 10^5`
- `nums.length == n + 1`
- `1 <= nums[i] <= n`
- All the integers in `nums` appear only once except for precisely one integer which appears two or more times.

### Notes

- Solve the problem without modifying the array `nums`.
- Use only constant extra space.

