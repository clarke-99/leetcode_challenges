## Challenge 4. Median of Two Sorted Arrays

**Problem:** Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays. The overall run time complexity should be `O(log (m+n))`.

## Examples

**Example 1:**

- **Input:** `nums1 = [1,3]`, `nums2 = [2]`
- **Output:** `2.00000`
- **Explanation:** The merged array is `[1,2,3]`, and the median is `2`.

**Example 2:**

- **Input:** `nums1 = [1,2]`, `nums2 = [3,4]`
- **Output:** `2.50000`
- **Explanation:** The merged array is `[1,2,3,4]`, and the median is `(2 + 3) / 2 = 2.5`.

## Constraints

- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`

## Approach

A `median` is the exact middle value in a *sorted* array; therefore, the first step was to combine and sort the two arrays. Once this has been done it is a simple matter of calculating the index position of the median. If the `median` index position is a `float`, the median value will be the average of the values on either side of the median index.

1. **Calculate Midpoint**
   - To find the median, first calculate the midpoint of the combined length of the two arrays. This is given by m = (length of merged array + 1) / 2.

2. **Handling Float `m`**
   - If the calculated midpoint results in a float (which indicates an even-length combined array), adjust the midpoint calculation to determine the indices around which the median will be computed.
   
     
3. **Finding the Median**
   - Convert the midpoint(s) to an integer for indexing purposes.
   - In zero-indexed arrays, after merging:
    -- If the combined length is odd, return the value at the midpoint index.
    -- If the combined length is even, return the average of the values at the midpoint index and the one immediately before it.

### Notes

Now that I have written this, I realise it may have been more efficient to use the isinstance method to determine if the median index was a float or integer rather than the conversion to a string.
