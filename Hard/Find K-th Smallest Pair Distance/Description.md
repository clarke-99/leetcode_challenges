## Challenge 719. Find K-th Smallest Pair Distance

**Problem:** Given an integer array `nums` and an integer `k`, return the k-th smallest distance among all pairs `(nums[i], nums[j])` where `0 <= i < j < nums.length`. The distance of a pair of integers `a` and `b` is defined as the absolute difference between `a` and `b`.

## Examples

**Example 1:**

- **Input:** `nums = [1,3,1]`, `k = 1`
- **Output:** `0`
- **Explanation:** All pairs and their distances:
  - `(1,3)` -> `2`
  - `(1,1)` -> `0`
  - `(3,1)` -> `2`
  The 1st smallest distance is `0`.

**Example 2:**

- **Input:** `nums = [1,1,1]`, `k = 2`
- **Output:** `0`
- **Explanation:** All pairs have a distance of `0`. Thus, the 2nd smallest distance is `0`.

**Example 3:**

- **Input:** `nums = [1,6,1]`, `k = 3`
- **Output:** `5`
- **Explanation:** All pairs and their distances:
  - `(1,6)` -> `5`
  - `(1,1)` -> `0`
  - The `3rd` smallest distance is `5`.

## Constraints

- `n == nums.length`
- `2 <= n <= 10^4`
- `0 <= nums[i] <= 10^6`
- `1 <= k <= n * (n - 1) / 2`

