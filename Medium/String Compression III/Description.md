## 3163. String Compression III

**Problem:** Begin with an *empty* string `comp`. While `word` is not empty, use the following operation: 
Remove a maximum length prefix of `word` made of a single character c repeating at most 9 times.
Append the length of the prefix followed by c to `comp`. Return the string comp.

## Examples 

**Example 1:**

- **Input:** `word` = "abcde"
- **Output:** "1a1b1c1d1e"
- **Explanation:** Apply the operation 5 times, choosing "a", "b", "c", "d", and "e" as the prefix in each operation.
-   For each prefix, append "1" followed by the character to comp.

**Example 2:**

- **Input:** `word` = "aaaaaaaaaaaaaabb"
- **Output:** "9a5a2b"
- **Explanation:** Apply the operation 3 times, choosing "aaaaaaaaa", "aaaaa", and "bb" as the prefix in each operation.
-   For prefix "aaaaaaaaa", append "9" followed by "a" to comp.
-   For prefix "aaaaa", append "5" followed by "a" to comp.
-   For prefix "bb", append "2" followed by "b" to comp.
 

## Constraints:

- `1 <= word.length <= 2 * 10^5`
- `word` consists only of lowercase English letters.

## Approach

1. **Initialise Variables:**
   - Create the *empty* string `comp`, a `left` pointer and the list `prefix_char`
2. **Outer Loop:**
   - The outer loop runs as long as `left` is less than the length of `word`, this prevents index errors
   - The `right` pointer is assigned as `left + 1`, this prevents checking the exact same letter reducing time complexity from O(N^2) to O(N)
   - Due to the initialisation of `right` the count *must* start at one
3. **Inner Loop:**
   - The inner loop runs as long as:
   -    `right` is less than the length of `word`
   -    `left` and `right` point to the same letter
   -    `count` is less than 9
4. **Append The List and Increment `left`:**
   - Once the inner loop terminates, add a tuple containing the `count` and the associated letter
   - This was required due to a very large test case that resulted in run-time errors when modifying `comp` in place with a string conversion
     and concatenation
   - Once complete `left` must be set to equal `right` to skip the accounted-for letters
5. **Join and Return:**
   - As the challenge specified using the *empty* string `comp`, the result can be obtained by joining the `prefix_char` list and concatenating
     the result to `comp`


## Complexity Analysis

**Time:** O(N)
- This is because each character in `word` is only iterated over once
**Space:** O(N)
- The memory usage will scale linearly as the length of the additional list, `prefix_char`, will be equal to the length of `word`

