## Challenge 3016. Minimum Number of Pushes to Type Word II

**Problem:** 

You are given a string `word` containing lowercase English letters. Telephone keypads have keys mapped with distinct collections of lowercase English letters, which can be used to form words by pushing them. For example, the key 2 might be mapped to ["a","b","c"], where you need to push the key one time to type "a", two times to type "b", and three times to type "c".
The keys can be remapped to any number of letters, but each letter must be mapped to exactly one key. You need to find the minimum number of key pushes required to type the string `word` after optimally remapping the keys.

## Examples

**Example 1:**

- **Input:** `word = "abcde"`
- **Output:** `5`
- **Explanation:** By remapping keys optimally:
  - "a" -> 1 push on key 2
  - "b" -> 1 push on key 3
  - "c" -> 1 push on key 4
  - "d" -> 1 push on key 5
  - "e" -> 1 push on key 6
  Total cost is 1 + 1 + 1 + 1 + 1 = 5.

**Example 2:**

- **Input:** `word = "xyzxyzxyzxyz"`
- **Output:** `12`
- **Explanation:** By remapping keys optimally:
  - "x" -> 1 push on key 2
  - "y" -> 1 push on key 3
  - "z" -> 1 push on key 4
  Total cost is 1 * 4 + 1 * 4 + 1 * 4 = 12.

**Example 3:**

- **Input:** `word = "aabbccddeeffgghhiiiiii"`
- **Output:** `24`
- **Explanation:** By remapping keys optimally:
  - "a" -> 1 push on key 2
  - "b" -> 1 push on key 3
  - "c" -> 1 push on key 4
  - "d" -> 1 push on key 5
  - "e" -> 1 push on key 6
  - "f" -> 1 push on key 7
  - "g" -> 1 push on key 8
  - "h" -> 2 pushes on key 9
  - "i" -> 1 push on key 9
  Total cost is 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 2 * 2 + 6 * 1 = 24.

## Constraints

- `1 <= word.length <= 10^5`
- `word` consists of lowercase English letters.

## Approach

This function calculates the minimum number of key presses required to type a given word on an old-style phone keypad. The keypad has 8 keys, and characters are assigned to these keys based on their frequency in the word. After assigning the most frequent characters to the first 8 keys, additional characters are assigned by increasing the number of key presses required.

### Steps:

1. **Count Frequency:**
   - Creates a dictionary that maps each character in the word to the number of times it appears.
   
3. **Sort by Frequency:**
   - Sorts the characters in descending order based on their frequency.
   - Ensures that the most frequent characters are considered first when assigning them to keys.

3. **Assign Keypresses:**
   - Characters are assigned to the 8 keys based on their frequency.
   - Initially, the most frequent characters are assigned to the first key (requiring one key press each).
   - Once all 8 keys are occupied, additional characters are assigned to the next available key, which increases the required number of presses for each subsequent character.


## Summary

The minimumPushes function simulates typing a word on an old mobile phone keypad with 8 keys. Characters are assigned to these keys based on how often they appear in the word. The most frequent characters are placed on the keys that require fewer presses. Once all 8 keys are used, additional characters are placed on the keys in a way that increases the number of presses required, simulating the behavior of typing on an old keypad where additional characters on a key require more key presses.
