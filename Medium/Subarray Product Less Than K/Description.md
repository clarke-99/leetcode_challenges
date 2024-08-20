## Challenge 713. Subarray Product Less Than K

**Problem:** Given an array of integers `nums` and an integer `k`, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than `k`.

## Examples

**Example 1:**

- **Input:** `nums = [10,5,2,6]`, `k = 100`
- **Output:** `8`
- **Explanation:** The 8 subarrays with a product less than 100 are:
  - `[10]`, `[5]`, `[2]`, `[6]`
  - `[10, 5]`, `[5, 2]`, `[2, 6]`
  - `[5, 2, 6]`
  - Note: `[10, 5, 2]` is excluded as its product is not strictly less than 100.

**Example 2:**

- **Input:** `nums = [1,2,3]`, `k = 0`
- **Output:** `0`
- **Explanation:** No subarray has a product less than 0.

## Constraints

- `1 <= nums.length <= 30,000`
- `1 <= nums[i] <= 1,000`
- `0 <= k <= 1,000,000`

### Approach

To solve this problem, you can use the sliding window technique:

1. **Initialize** two pointers (`left` and `right`) and a variable to keep track of the product of elements in the current window.
2. **Expand** the right pointer to include more elements while the product of the subarray remains less than `k`.
3. **Contract** the left pointer to maintain the condition when the product exceeds `k`.
4. **Count** the number of valid subarrays ending at each position of the right pointer.

This approach ensures that you traverse the array in linear time while dynamically adjusting the window to satisfy the product constraint.
