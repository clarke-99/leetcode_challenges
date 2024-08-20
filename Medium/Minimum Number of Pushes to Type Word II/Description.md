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
