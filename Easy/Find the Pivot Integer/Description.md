**Challenge 2485: Find the Pivot Integer**

**Problem:**
Given a positive integer `n`, find the pivot integer `x` such that:
- The sum of all integers from 1 to `x` (inclusive) is equal to the sum of all integers from `x` to `n` (inclusive).

If such an integer `x` exists, return it. Otherwise, return `-1`. It is guaranteed that there will be at most one pivot integer for the given input.

**Examples:**

1. **Input:** `n = 8`  
   **Output:** `6`  
   **Explanation:** For `x = 6`, the sum of numbers from 1 to 6 is 21, which equals the sum of numbers from 6 to 8 (21).

2. **Input:** `n = 1`  
   **Output:** `1`  
   **Explanation:** For `x = 1`, the sum of numbers from 1 to 1 is 1, which equals the sum of numbers from 1 to 1 (1).

3. **Input:** `n = 4`  
   **Output:** `-1`  
   **Explanation:** No such integer exists where the sum of numbers up to `x` equals the sum from `x` to `n`.

**Constraints:**

- 1 <= `n` <= 1000

