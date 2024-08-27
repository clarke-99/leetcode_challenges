## Challenge 848. Shifting Letters

**Problem:** You are given a string s of lowercase English letters and an integer array shifts of the same length.
Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a'). Return the final string after all such shifts to s are applied.

## Examples

**Example 1:**

- **Input:** `s = "abc"`, `shifts = [3,5,9]`
- **Output:** `"rpl"`
- **Explanation:** We start with "abc".
After shifting the first 1 letter of s by 3, we have "dbc".
After shifting the first 2 letters of s by 5, we have "igc".
After shifting the first 3 letters of s by 9, we have "rpl", the answer.


**Example 2:**

- **Input:** `s = "aaa"`, `shifts = [1,2,3]`
- **Output:** `"gfd"`
 

## Constraints:

`1 <= s.length <= 10^5`
`s` consists of `lowercase` English letters.
`shifts.length == s.length`
`0 <= shifts[i] <= 10^9`

## Approach

1. **Conversion to list**
   - `strings` are immutable, therefore modification requires new `string` creation
   - Conversion to a `list` allows for *in-place* modification and increases efficiency
  
2. **Iterate Backwards**
   - Cumulative `shifts` require that all subsequent shifts influence each character's shift
   - Iterating from the end of the list of `shifts` to the beginning, you can maintain a running total of cumulative shifts and apply it correctly to each `character`.
  
3. **Handling Wrap**
   - *Convert to 0-Based Index:* Subtract 97 from the `ASCII value` of the character to shift it into a `0-based index` (where 'a' = 0, 'b' = 1, ..., 'z' = 25).
   - *Apply Modulo 26:* Use modulo 26 to handle wrapping around the alphabet if the index goes beyond 25.
   - *Convert Back to ASCII:* Add 97 to shift it back to the `ASCII range` for lowercase letters.
  
