## Challenge 20. Valid Parentheses

**Problem:** Given a string `s` consisting of characters `'(', ')', '{', '}', '['`, and `']'`, determine if the input string is valid.

## Definition of a Valid String

An input string is considered valid if:
1. Every open bracket must be closed by the same type of bracket.
2. Every open bracket must be closed in the correct order.
3. Every closing bracket must have a corresponding open bracket of the same type.

## Examples

**Example 1:**

- **Input:** `s = "()"`
- **Output:** `true`
- **Explanation:** The brackets are correctly paired and nested.

**Example 2:**

- **Input:** `s = "()[]{}"`
- **Output:** `true`
- **Explanation:** All types of brackets are correctly paired and nested.

**Example 3:**

- **Input:** `s = "(]"`
- **Output:** `false`
- **Explanation:** The brackets are not correctly paired.

## Constraints

- `1 <= s.length <= 10^4`
- `s` consists of parentheses only `'()[]{}'`.

