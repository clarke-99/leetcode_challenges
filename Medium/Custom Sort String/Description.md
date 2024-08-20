## Challenge 791. Custom Sort String

**Problem:**

You are given two strings: `order` and `s`. All characters in `order` are unique and sorted according to some custom order. Your task is to permute the characters in `s` so that they match the order specified in `order`. Specifically, if a character `x` appears before a character `y` in `order`, then `x` should appear before `y` in the permuted string.

## Examples

**Example 1:**

- **Input:** `order = "cba"`, `s = "abcd"`
- **Output:** `"cbad"`
- **Explanation:**
  - Characters "a", "b", and "c" appear in `order`, so their order in `s` should be "c", "b", and "a".
  - Character "d" does not appear in `order`, so it can be placed anywhere in the resulting string.
  - Valid outputs include "dcba", "cdba", "cbda", etc.

**Example 2:**

- **Input:** `order = "bcafg"`, `s = "abcd"`
- **Output:** `"bcad"`
- **Explanation:**
  - Characters "b", "c", and "a" from `order` dictate their relative order in `s`.
  - Character "d" is not in `order` and can be placed anywhere in the result.
  - Valid outputs include "bcad", "bacd", "bcda", etc., as long as "b", "c", and "a" maintain their order.

## Constraints

- `1 <= order.length <= 26`
- `1 <= s.length <= 200`
- `order` and `s` consist of lowercase English letters.
- All characters in `order` are unique.