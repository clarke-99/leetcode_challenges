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
