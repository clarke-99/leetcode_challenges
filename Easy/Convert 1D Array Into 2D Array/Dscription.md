## Challenge 2022. Convert 1D Array Into 2D Array

**Problem:** You are given a 0-indexed 1-dimensional (1D) integer array original, and two integers, `m` and `n`. You are tasked with creating a 
2-dimensional (2D) array with  `m rows` and `n columns` using all the elements from original. The elements from indices 0 to n - 1 (inclusive) of
original should form the first row of the constructed 2D array, the elements from indices `n` to `2 * n - 1` (inclusive) should form the 
second row of the constructed 2D array, and so on. Return an `m x n` 2D array constructed according to the above procedure, or an empty 2D 
array if it is impossible.

## Examples
 
**Example 1:**

- **Input:** `original = [1,2,3,4]`, `m = 2`, `n = 2`
- **Output:** [[1,2],[3,4]]
- **Explanation:** The constructed 2D array should contain 2 rows and 2 columns.
The first group of n=2 elements in original, [1,2], becomes the first row in the constructed 2D array.
The second group of n=2 elements in original, [3,4], becomes the second row in the constructed 2D array.

**Example 2:**

- **Input:** `original = [1,2,3]`, `m = 1`, `n = 3`
- **Output:** [[1,2,3]]
- **Explanation:** The constructed 2D array should contain 1 row and 3 columns.
Put all three elements in original into the first row of the constructed 2D array.

**Example 3:**

- **Input:** `original = [1,2]`, `m = 1`, `n = 1`
- **Output:** []
- **Explanation:** There are 2 elements in original.
It is impossible to fit 2 elements in a 1x1 2D array, so return an empty 2D array.
 

## Constraints:

- `1 <= original.length <= 5 * 10^4`
- `1 <= original[i] <= 10^5`
- `1 <= m`, `n <= 4 * 10^4`

## Approach 

1. **Check Length Compatibility:**
   - The first step is to verify whether the length of original is exactly equal to `m * n`.
     This ensures that the total number of elements can be perfectly divided into a 2D array with `m` rows and `n` columns.
   - If the length is not equal, it's impossible to reshape the array as required, so the function immediately returns an empty array.

2. **Construct 2D Array using List Comprehension:**
   - If the length check passes, the solution uses list comprehension to construct the 2D array.
   - The list comprehension iterates over the original array in steps of `n`, slicing out subarrays of length n to form each row of the
     new 2D array.
   - Specifically, the expression `[original[x:n+x]` for `x` in `range(0, len(original), n)]` efficiently slices the original list starting at
     index `x` and ending at `x+n`, incrementing `x` by `n` in each step.

### Time and Space Complexity:

The approach operates with an `O(m * n)` time complexity, as it needs to iterate over all elements in original.
The space complexity is also `O(m * n)`, given that a new 2D list is created to hold the elements in the required shape.
