## Challenge 1137: N-th Tribonacci Number

**Problem:**
The Tribonacci sequence is defined as follows:
- T₀ = 0
- T₁ = 1
- T₂ = 1
- For n >= 0, Tₙ₊₃ = Tₙ + Tₙ₊₁ + Tₙ₊₂

Given an integer `n`, return the value of Tₙ.

## Examples:

 **Example 1:**
 
 - **Input:** `n = 4`
 - **Output:** `4`
 - **Explanation:** 
   -- T₃ = T₀ + T₁ + T₂ = 0 + 1 + 1 = 2
   -- T₄ = T₁ + T₂ + T₃ = 1 + 1 + 2 = 4

 **Example 2:**
 
 - **Input:** `n = 25`
 - **Output:** `1389537`
 - **Explanation:** This is the 25th number in the Tribonacci sequence.

## Constraints:

- 0 <= `n` <= 37
- The result is guaranteed to fit within a 32-bit integer (answer <= 2^31 - 1).

