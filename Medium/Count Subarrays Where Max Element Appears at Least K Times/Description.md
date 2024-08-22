## Challenge 2962. Count Subarrays Where Max Element Appears at Least K Times

**Problem:** You are given an integer array nums and a positive integer k. Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

**Info:** A subarray is a contiguous sequence of elements within an array.

## Examples

**Example 1:**

**Input:** nums = [1,3,2,3,3], k = 2
**Output:** 6
**Explanation:** The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].


**Example 2:**

**Input:** nums = [1,4,2,1], k = 3
**Output:** 0
**Explanation:** No subarray contains the element 4 at least 3 times.
 

## Constraints:

`1 <= nums.length <= 10^5`
1 <= nums[i] <= 10^6`
1 <= k <= 10^5`

## Approach

The sliding window method is appropriate for this challenge...

1. **Check if Max Element Appears K Times**
   - By checking the count of `max_element` before initiating the sliding window and associated variables, the average runtime
      and memory usage is reduced.
2. **Initialise Variables**
   - Set the count variables, `max_count` and `subarr_count`, and the `left pointer` to 0
   - Iterate over the array with the `right pointer`

3. **Count Max Element**
   - Whenever the `right pointer` is `max_element`, increment the `count`
   - Once the `count` > `k`, then every subarray from `right pointer` to the end of the array, `n`, is a valid subarray; therefore,
     the `subarr_count` can be incremented by `n - right`

4. **Increment Left Pointer**
   - Adjust the window by moving the `left pointer`. Each time `subarr_count` updates, check if the `left pointer` needs to be
     moved to narrow the window.
   - Update `max_count` accordingly when you shift the `left pointer`.
