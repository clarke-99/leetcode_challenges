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

### Approach

To solve this problem, you need to simulate the multiplication process manually, handling string operations and digit manipulations. This involves:

1. Initializing a result array to store intermediate results.
2. Multiplying each digit of `num1` by each digit of `num2`, and accumulating the results.
3. Managing carry-over and proper positioning in the result array.
4. Converting the result array back to a string format, handling leading zeros.
