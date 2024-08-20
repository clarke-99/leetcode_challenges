**Challenge 205: Isomorphic Strings**

**Problem:**
Given two strings `s` and `t`, determine if they are isomorphic. Two strings are considered isomorphic if there is a one-to-one mapping between the characters of `s` and `t`, such that replacing each character in `s` with its mapped character results in `t`, and vice versa.

**Conditions:**

- Each character in `s` maps to exactly one character in `t`.
- Each character in `t` maps to exactly one character in `s`.
- All occurrences of a character must be replaced consistently, preserving the order of characters.
- No two characters in `s` or `t` can map to the same character.

**Examples:**

1. **Input:** `s = "egg"`, `t = "add"`  
   **Output:** `true`  
   **Explanation:** Each 'e' maps to 'a' and 'g' maps to 'd'. The mapping is consistent.

2. **Input:** `s = "foo"`, `t = "bar"`  
   **Output:** `false`  
   **Explanation:** The character 'o' maps to 'a' in `t`, but both 'f' and 'o' in `s` map to 'b' and 'a', respectively. This is not a one-to-one mapping.

3. **Input:** `s = "paper"`, `t = "title"`  
   **Output:** `true`  
   **Explanation:** The mapping is consistent: 'p' maps to 't', 'a' to 'i', and 'e' to 'l'.

**Constraints:**

- 1 <= `s.length` <= 50,000
- `t.length` == `s.length`
- `s` and `t` consist of any valid ASCII characters.
