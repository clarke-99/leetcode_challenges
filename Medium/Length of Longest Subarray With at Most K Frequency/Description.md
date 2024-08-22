## Challenge 2958. Length of Longest Subarray With at Most K Frequency

**Problem:** You are given an integer array nums and an integer k. The frequency of an element x is the number of times it occurs in an array.
Return the length of the longest good subarray of nums.

**Info:** 
- An array is called good if the frequency of each element in this array is less than or equal to k
- A subarray is a contiguous non-empty sequence of elements within an array.

## Examples

**Example 1:**

- **Input:** `nums = [1,2,3,1,2,3,1,2]`, `k = 2`
- **Output:** `6`
- **Explanation:** The longest possible `good subarray` is `[1,2,3,1,2,3]` since the values 1, 2, and 3 occur at most twice in this subarray. Note that the subarrays [2,3,1,2,3,1] and [3,1,2,3,1,2] are also good.

**Example 2:**

- **Input:** `nums = [1,2,1,2,1,2,1,2]`, `k = 1`
- **Output:** `2`
- **Explanation:** The longest possible `good subarray` is `[1,2]` since the values 1 and 2 occur at most once in this subarray. Note that the subarray [2,1] is also good.

**Example 3:**

- **Input:** `nums = [5,5,5,5,5,5,5]`, `k = 4`
- **Output:** `4`
- **Explanation:** The longest possible `good subarray` is `[5,5,5,5]` since the value 5 occurs 4 times in this subarray.
 

## Constraints:

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= k <= nums.length`

## Approach

For this challenge, I used the sliding window method combined with a frequency dictionary.

1. **Initialise**
   - Initialise the `left pointer` and `max_length` to 0, and create an empty `frequency dictionary`.
   - Iterate over the array with a `right pointer`

2.**Count Occurences**
   - If the number at the `right pointer` is not in the dictionary, set its count to 1.
   - If the number is already in the dictionary, increment its frequency by 1.
   - If the frequency of the number exceeds `k`:
       - Move the `left pointer` to the right while the frequency of the number at the `right pointer` is greater than `k`.
       - Decrement the frequency of the number at the `left pointer`, and remove it from the dictionary if its frequency reaches 0.
       - Increment the `left pointer`.
    
3. **Compare Lengths**
   - Use the `max()` function to compare the length of the current subarray with `max_length`. Update `max_length` to be the larger of the two.
   - Continue this process until the `right pointer` has iterated over the entire array.
     
By the end of the iteration, `max_length` will represent the length of the longest good subarray.
    

