## Challenge 273. Integer to English Words

**Problem:** Convert a non-negative integer num to its word representation in English.

## Examples

**Example 1:**

- **Input:** `num = 123`
- **Output:** "One Hundred Twenty Three"

**Example 2:**

- **Input:** `num = 12345`
- **Output:** "Twelve Thousand Three Hundred Forty Five"
  
**Example 3:**

- **Input:** `num = 1234567`
- **Output:** "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
 

## Constraints:

`0 <= num <= 2^31 - 1`

## Approach

I tackled this problem in two attempts, refining my approach to improve readability and modularity. The first attempt (numberToWord.py) 
worked for most cases but struggled with larger numbers like 1,000,000, due to a simplistic approach to appending suffixes like "Thousand."
In the second attempt (numberToWord2.py), I focused on better coding practices, using a helper function to enhance modularity and readability. 
This second approach successfully handled all test cases. Below is the detailed methodology used in numberToWord2.py.

1. **Initialisation of Lists and Dictionary**
   - **`num_list:`** A list to store the digits of the number, enabling independent processing of digit groups.
   - **`below_20` and `tens` Lists:** These lists store word equivalents for numbers from 1 to 19 and multiples of ten (20, 30, ..., 90),
     respectively.
   - **`suffix` Dictionary:** A dictionary mapping large numbers like "Thousand," "Million," and "Billion" to their respective powers of ten.

2. **Splitting into Chunks**
   - **Modular Arithmetic:** The input number is split into three-digit chunks using modulo and integer division, simplifying the addition
     of appropriate suffixes (e.g., "Thousand," "Million").
   - Each `chunk`, representing a number less than 1,000, is passed to a helper function `find_num`.
  
3. **Recursive Function `find_num`**
   - This function processes a three-digit number (n). It returns the word representation by either directly mapping the number to a
     value in the lists (`below_20` or `tens`) or combining values from the lists with recursive calls to handle numbers like "21" or "315."

4. **Applying the Suffix**
   - The `suffix` is determined by the number of zeros following the current `chunk`, calculated as `l - chunk_position`. The corresponding
     suffix (e.g., "Thousand," "Million") is then appended by looking up the `suffix dictionary`.

5. **Updating the List**
   - After processing a `chunk`, `num_list` is updated to remove the processed digits, and the process repeats until all chunks have been
     converted.


### Complexity Analysis

**Time Complexity:** O(log(n)) – The time complexity is logarithmic relative to the input number, as the algorithm splits the number into 
manageable three-digit chunks.
**Space Complexity:** O(1) – The space complexity is constant since the space used by the algorithm does not grow with the input size.


   
