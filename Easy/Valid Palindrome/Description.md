## Challenge 125. Valid Palindrome

A phrase is considered a palindrome if, after converting all uppercase letters to lowercase and removing all non-alphanumeric characters, it reads the same forwards and backwards. Alphanumeric characters include letters and numbers.

**Problem:** Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

## Examples

**Example 1:**

- **Input:** `s = "A man, a plan, a canal: Panama"`
- **Output:** `true`
- **Explanation:** After processing, the string becomes `"amanaplanacanalpanama"`, which is a palindrome.

**Example 2:**

- **Input:** `s = "race a car"`
- **Output:** `false`
- **Explanation:** After processing, the string becomes `"raceacar"`, which is not a palindrome.

**Example 3:**

- **Input:** `s = " "`
- **Output:** `true`
- **Explanation:** The string is an empty string after processing. An empty string is considered a palindrome.

## Constraints

- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.

