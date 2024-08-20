## Challenge 35: Search Insert Position 

**Problem:**
Given a sorted array of distinct integers `nums` and a target value `target`, return the index where `target` is found. If `target` is not found, return the index where it would be inserted to maintain the sorted order. 

Your algorithm should have a runtime complexity of \( O(\log n) \).

## Examples 

**Example 1:**

- **Input:** `nums = [1, 3, 5, 6]`, `target = 5`
- **Output:** `2`
- **Explanation:** The target value `5` is found at index `2`.

**Example 2:**

- **Input:** `nums = [1, 3, 5, 6]`, `target = 2`
- **Output:** `1`
- **Explanation:** The target value `2` is not found. It should be inserted at index `1` to maintain the sorted order.

**Example 3:**

- **Input:** `nums = [1, 3, 5, 6]`, `target = 7`
- **Output:** `4`
- **Explanation:** The target value `7` is not found. It should be inserted at index `4` to maintain the sorted order.

## Constraints:

- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` contains distinct values sorted in ascending order.
- `-10^4 <= target <= 10^4`

