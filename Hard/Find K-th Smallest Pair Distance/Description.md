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

## Approach

The approach efficiently finds the k-th smallest distance using a combination of sorting, binary search, and a two-pointer technique. Sorting helps in applying the two-pointer method effectively, binary search narrows down the smallest valid distance, and the two-pointer technique counts the number of valid pairs within the distance constraint.

1. **Sort the Array**
   - This ensures that you can use a `two-pointer` approach to efficiently count valid pairs with a given maximum distance.

2. **Initialize Binary Search**
   - Set `low` to 0 and `high` to `nums[-1] - nums[0]`
   - The binary search continues while `low < high`.
     
3. **Calculate Midpoint**
   - `mid = (low + high) // 2`
   - This is the midpoint distance being tested to see if there are at least `k` pairs.

4. **Count Valid Pairs**
   - The function `count_pairs_with_max_distance(max_dist)` counts the number of pairs (i, k) such that `nums[k] - nums[i] <= max_dist`.
   - How it works:
       - For each index `i`, use a second pointer `j` to find the *furthest index* such that the distance between `nums[i]` and `nums[j]` is within `max_dist`.
       - The *number of valid pairs* with `i` as the starting index is `(j - i - 1)`, since `j` itself is not counted and we want pairs strictly between i and j.

5. **Adjust Search Range**
   - If the `count` of valid pairs is less than `k`, it means mid is too small to have at least `k` pairs, and the search range must be adjusted higher by setting `low = mid + 1`.
   - If the `count` is at least `k`, it means mid is a *potential candidate*, but a smaller distance might also work; adjust the search range to lower distances by setting `high = mid`.

6. **Loop Exit and Result**
- The loop continues adjusting `low` and `high` until they converge.
- When `low == high`, it represents the smallest distance such that there are at least `k` pairs with that distance or less.


