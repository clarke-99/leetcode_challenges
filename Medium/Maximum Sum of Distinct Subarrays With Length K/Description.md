## Challenge 2461. Maximum Sum of Distinct Subarrays With Length K

**Problem:** You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the 
conditions:

1. The length of the subarray is k, and
2. All the elements of the subarray are distinct.
3. Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.

## Examples

### Example 1:

- **Input:** `nums = [1,5,4,2,9,9,9]`, `k = 3`
- **Output**: 15
- **Explanation:** The subarrays of nums with length 3 are:
  - [1,5,4] which meets the requirements and has a sum of 10.
  - [5,4,2] which meets the requirements and has a sum of 11.
  - [4,2,9] which meets the requirements and has a sum of 15.
  - [2,9,9] which does not meet the requirements because element 9 is repeated.
  - [9,9,9] which does not meet the requirements because element 9 is repeated.

### Example 2:

- **Input:** `nums = [4,4,4]`, `k = 3`
- **Output:** 0
- **Explanation:** The subarrays of nums with length 3 are:
  - [4,4,4] which does not meet the requirements because element 4 is repeated.


## Constraints:

- `1 <= k <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`

## Approach

1. **Initialise Window and Tracking Variables:**
   - create the set `window` to keep track of duplicates
   - create variables `current_sum` and `max_sum` which will allow for dynamically calculating the sum of the current window
     and comparison with the largest total sum.
   - create `start` which points to the beginning of the current `window`
2. **Iterate through Array `nums`:**
   - Go through each element of `nums` checking if the current element is already in `window`
   - while the current element is in `window` shrink the window by incrementing the `start` pointer reducing `current_sum` and removing the
     corresponding element from `window`
   - add the current element to `window` and `current_sum`
3. **Compare `max_sum` and `current_sum`:**
   - If the difference between `i` and the `start` pointer is equal to `k`, then the number of elements within the subarray is correct
   - Update `max_sum` using the inbuilt max() method
   - Update the `window` and `start` pointer

## Complexity Analysis

1. **Time:**
   - The list is only iterated through once which would be O(n)
   - The while loop *seems* like it *could* increase the time complexity to O(n^2), if all values were duplicates
   - However, as the addition and removal operations are only performed once per element, the overall runtime is linear O(n)

2. **Space:**
   - The only additional space used is the set to track duplicates which will grow with respect to `k`
   - Therefore O(k) 
