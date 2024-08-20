## Challenge 13: Roman to Integer

**Problem:**
Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M, with specific values associated with each symbol. For example:
- I = 1
- V = 5
- X = 10
- L = 50
- C = 100
- D = 500
- M = 1000

Roman numerals are typically written from largest to smallest from left to right. However, for certain values, subtraction is used: 
- I before V or X makes 4 or 9.
- X before L or C makes 40 or 90.
- C before D or M makes 400 or 900.

Given a Roman numeral string `s`, convert it to its corresponding integer value.

## Examples:

 **Example 1:**
 - **Input:** `s = "III"`
 - **Output:** `3`
 - **Explanation:** The Roman numeral III is 3.

 **Example 2:**
 - **Input:** `s = "LVIII"`
 - **Output:** `58`
 - **Explanation:** L = 50, V = 5, III = 3, so the total is 58.

 **Example 3:**
 - **Input:** `s = "MCMXCIV"`
 - **Output:** `1994`
 - **Explanation:** M = 1000, CM = 900, XC = 90, IV = 4, so the total is 1994.

## Constraints:

- `1 <= s.length <= 15`
- `s` contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
- It is guaranteed that `s` is a valid Roman numeral in the range [1, 3999].

