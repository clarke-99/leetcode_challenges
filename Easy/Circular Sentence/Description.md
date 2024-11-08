## 2490. Circular Sentence

**Problem:** Given a string sentence, return true if it is circular. Otherwise, return false.

### Definitions 

**Sentence:** A list of words that are separated by a single space with no leading or trailing spaces.

**Circular Sentence:**
- The last character of a word is equal to the first character of the next word.
- The last character of the last word is equal to the first character of the first word.
- For example, "leetcode exercises sound delightful", "eetcode", "leetcode eats soul" are all circular sentences. However, "Leetcode is cool", "happy Leetcode", "Leetcode" and "I like Leetcode" are not circular sentences.

## Examples
 
**Example 1:**

- **Input:** `sentence = "leetcode exercises sound delightful"`
- **Output:** true
- **Explanation:** The words in `sentence` are ["leetcode", "exercises", "sound", "delightful"].
  - leetcode's last character is equal to exercises's first character.
  - exercises's last character is equal to sound's first character.
  - sound's last character is equal to delightful's first character.
  - delightful's last character is equal to leetcode's first character.

**Example 2:**

- **Input:** `sentence = "eetcode"`
- **Output:** true
- **Explanation:** The words in `sentence` are ["eetcode"].
  - eetcode's last character is equal to eetcode's first character.

**Example 3:**

- **Input:** `sentence = "Leetcode is cool"`
- **Output:** false
- **Explanation:** The words in `sentence` are ["Leetcode", "is", "cool"].
  - Leetcode's last character is not equal to is's first character.

 ## Constraints:

- `1 <= sentence.length <= 500`
- `sentence` consists of only lowercase and uppercase English letters and spaces.
- The words in `sentence` are separated by a single space.
- There are no leading or trailing spaces.

## Approach 

1. **Split Sentence:**
   - By splitting the string into a list of `words` the lookup times are improved and the logic made simpler
  
2. **Iterate Over List:**
   - This is simple enough but the main aspect of this is checking the last word against the first
   - To do this I used a modulo operation which allows for efficient wrapping around at the end of the list
  
3. **Result:**
   - If at any point the condition fails, the loop is broken and return False
   - If the loop completes then the condition is True and returns as such.
  
### Complexity 

- **Time: O(n)**
  -  The algorithm runtime grows linearly with input size as it only iterates through each word once
- **Space: O(n)**
  -  The space complexity will also grow linearly as the size of the list `words` will be equal to the input size and is the only additional
    space used
