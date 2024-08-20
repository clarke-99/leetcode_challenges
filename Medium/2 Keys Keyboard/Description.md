## Challenge 650. 2 Keys Keyboard

**Problem:** There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:

1. **Copy All:** You can copy all the characters present on the screen (a partial copy is not allowed).
2. **Paste:** You can paste the characters which were copied last time.

Given an integer `n`, return the minimum number of operations needed to get the character 'A' exactly `n` times on the screen.

## Examples

**Example 1:**

- **Input:** `n = 3`
- **Output:** `3`
- **Explanation:**
  1. Initially, we have one character 'A'.
  2. In step 1, use the **Copy All** operation.
  3. In step 2, use the **Paste** operation to get 'AA'.
  4. In step 3, use the **Paste** operation to get 'AAA'.

**Example 2:**

- **Input:** `n = 1`
- **Output:** `0`
- **Explanation:** No operations are needed as we already have 'A' on the screen.

## Constraints

- `1 <= n <= 1000`

## Approach

To solve this problem efficiently, we use a method based on the highest prime factors of the number `n`. The key insight is that the number of operations required to reach exactly `n` characters 'A' is related to the prime factorisation of `n`.

1. **Prime Factorisation**
   - To determine the minimum number of operations; break down the problem by finding the prime factors of `n`.
   - Each prime factor represents a required step.

2. **Operations Calculation**
   - Each prime factor, is added to a list. The sum of these prime factors is the minimum number of operations required.


