## Challenge 345. Reverse Vowels of a String

**Problem:** Given a string `s`, reverse only all the vowels in the string and return it. 
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

## Examples 

### Example 1:

- **Input:** `s = "IceCreAm"`
- **Output:** "AceCreIm"
- **Explanation:** The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, `s` becomes "AceCreIm".

### Example 2:

- **Input:** `s = "leetcode"`
- **Output:** "leotcede"

## Constraints:

- `1 <= s.length <= 3 * 10^5`
- `s` consist of printable ASCII characters.

## Approach 

1. **Initiliase variables and convert `s`:**
   - `s` is a string, which are immutable objects in Python, so conversion to a mutable list is required
   - Initialising two pointers, `left` and `right` which will iterate through the list `s`
   - Initialise a set `vowels` which will allow for the lookup of characters in constant time
2. **Outer Loop:**
   - Create a loop that will terminate when `left` meets `right`
   - This ensures that every character in `s` is checked
3. **Inner Loops:**
   - Increment and decrement `left` and `right` pointers respectively until they reach a vowel
   - The condition checking if `left` is less than `right` prevents the loop from incrementing/decrementing the pointers too much
4. **Swap Vowels:**
   - Once the pointers have reached a vowel, they can be swapped
   - The pointers then need to be moved to the next position to prevent an infinite loop
5. **Join and Return:**
   - At this point, the list `s` has the vowels correctly swapped but the problem requires the output be a string
   - This conversion is easily applied with the `.join()` method

## Complexity Analysis

1. **Time:** As the list `s` is only iterated through once, the runtime will be `O(n)`
2. **Space:** The only additional space usage is in the set which is minimal and the list created from `s`. This will also be `O(n)`
