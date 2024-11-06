## 1957. Delete Characters to Make Fancy String


**Problem:** Given a string `s`, delete the minimum possible number of characters from `s` to make it fancy. 
Return the final string after the deletion. It can be shown that the answer will always be unique.
A fancy string is a string where no three consecutive characters are equal.

## Examples 

**Example 1:**

- **Input:** `s = "leeetcode"`
- **Output:** "leetcode"
- **Explanation:** Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".

**Example 2:**

- **Input:** `s = "aaabaaaa"`
- **Output:** "aabaa"
- **Explanation:**
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".

**Example 3:**

- **Input:** `s = "aab"`
- **Output:** "aab"
- **Explanation:** No three consecutive characters are equal, so return "aab".
 

## Constraints:

- `1 <= s.length <= 10^5`
- `s` consists only of lowercase English letters.

## Approach 

1. **Define Early Exit**
   - If the length of `s` is less than 3, the string can be returned directly.
  
2. **Initialise List:**
   - Initialising a list of characters with the first two characters allows the loop to start from the third character and simply check backwards

3. **Iterate over `s`:**
   - Then iterate through `s` checking the two previous characters
   - If they are not the same as the current, append the current to the list `chars`

4. **Join List:**
   - Can now return the list after joining it to form the resulting string

## Complexity 

- **Time Complexity:** The loop will iterate through the characters only once so the runtime will grow linearly therefore it will be O(n)
- **Space Complexity:** With the added list, the space complexity will also grow linearly therefore O(n)
