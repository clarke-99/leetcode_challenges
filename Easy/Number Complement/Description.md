## Challenge 476. Number Complement

**Problem**: The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary 
representation.

## Examples

**Example 1:**

- **Input:** `num = 5`
- **Output:** `2`
- **Explanation:** The binary representation of 5 is `101` (no leading zero bits), and its complement is `010`. Therefore, the output is `2`.
  
**Example 2:**

- **Input:** `num = 1`
- **Output:** `0`
- **Explanation:** The binary representation of 1 is `1` (no leading zero bits), and its complement is `0`. Therefore, the output is `0`.
 

## Constraints:

`1 <= num < 2^31` 

## Approach 

1. **Conversion to Binary**
  - The built-in `bin` method converts `num` to its binary representation.
  - `bin(num)` returns the binary string prefixed with `0b`, indicating a `binary representation`,
     which can be easily iterated for processing.

2. **Create the Complement**
  - Since the binary representation includes the 0b prefix, we slice the string using [2:] to focus on the binary digits.
  - A list comprehension with ternary logic is used to flip the bits:
    - 1 becomes 0 and 0 becomes 1.
  - The resulting list of binary digits (as strings) is joined back into a single string.
  - Finally, int(complement, 2) converts the binary string back into an integer, specifying that it is a binary (base-2) number.

### Notes

I tried two methods, one of which called the `str` method on `bin(num)`, and one that used the string generated directly by `bin(num)`. I had thought the 
direct method would be the faster of the two; however, the code using `str(bin(num))` was better in terms of runtime and memory usage. 
