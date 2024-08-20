## Challenge 43. Multiply Strings

**Problem:** Given two non-negative integers `num1` and `num2` represented as strings, return the product of `num1` and `num2`, also represented as a string.

## Examples

**Example 1:**

- **Input:** `num1 = "2"`, `num2 = "3"`
- **Output:** `"6"`

**Example 2:**

- **Input:** `num1 = "123"`, `num2 = "456"`
- **Output:** `"56088"`

## Constraints

- You must not use any built-in BigInteger library or convert the inputs to integers directly.
- `1 <= num1.length, num2.length <= 200`
- `num1` and `num2` consist of digits only.
- Both `num1` and `num2` do not contain any leading zeros, except the number 0 itself.

## Approach

To tackle this problem, I reversed the input strings and converted the characters at each index into their corresponding integer values by multiplying them with the appropriate power of 10. This recreates the integers from the strings without using built-in conversion methods. 

1. **Reversing the Input Strings:**
   - Reversing makes it easier to handle the positional value of each digit.

3. **Manual Conversion:**
   - I wrote a `get_num` function that simulates converting each character to its corresponding integer value by using a list of digit characters.
   - This is an attempt to avoid direct conversion but might still indirectly violate the problem's constraints.

3. **Multiplication:**
   - The strings are multiplied after conversion, and the result is then converted back to a string.
  
### Challenges

1. Ensuring no direct integer conversion is used.
2. Handling carry-over during the multiplication.
3. Efficiently managing large inputs up to 200 digits long.
