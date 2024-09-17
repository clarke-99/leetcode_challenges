## Challenge 884. Uncommon Words from Two Sentences

**Problem:** A sentence is a string of single-space separated words where each word consists only of lowercase letters. 
A word is *uncommon* if it appears *exactly once* in one of the sentences, and *does not appear* in the other sentence.
Given two sentences `s1` and `s2`, return a list of all the uncommon words. You may return the answer in any order.

## Examples

**Example 1:**

- **Input:** `s1 = "this apple is sweet"`, `s2 = "this apple is sour"`
- **Output:** ["sweet","sour"]
- **Explanation:**
    - The word "sweet" appears only in s1, while the word "sour" appears only in s2.

**Example 2:**
- **Input:** `s1 = "apple apple"`, `s2 = "banana"`
- **Output:** ["banana"]

 ## Constraints:

- `1 <= s1.length, s2.length <= 200`
- `s1` and `s2` contain lowercase English letters and spaces.
- `s1` and `s2` do not have leading or trailing spaces.
- A *single space* separates all the words in `s1` and `s2`.

## Approach

1. **Helper Function: `get_f`**
   - This iterates through the `list` of the words from each `sentence`
   - Return a `frequency dictionary`
  
2. **Helper Function: `check_common`**
   - Iterates through a `frequency dictionary` (`f1`) checking if each key occurs once, and if it *does not* occur in the other dictionary (`f2`)
   - If *both* conditions are satisfied that key is appended to the list `uncommon`
  
3. **Concatenation of Lists:**
   - Split `s1` and `s2` into words, and pass them into the `get_f` function to create two frequency dictionaries (`f1` and `f2`).
   - Use the `check_common` function to find uncommon words from both dictionaries.
   - Return the concatenated lists from the lists of uncommon words from `s1` and `s2`.
  
### Complexity

**Time Complexity O(N):**
  - Iterates through lists of words exactly once
  - For each word, it performs a dictionary lookup and potentially an update, both of which are `O(1)` operations on average.
  - So, for a sentence with `N` words, the overall time complexity is O(N).

**Space Complexity O(N):**
  - Creates a dictionary to store the frequency of each word.
  - The size of the dictionary depends on the number of unique words, which in
    the worst case is `N` (if all words are unique).
  
   
