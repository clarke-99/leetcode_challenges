## Challenge 2554. Maximum Number of Integers to Choose From a Range I

**Problem:** You are given an integer array banned and two integers `n` and `maxSum`. You are choosing some number of integers following the rules.

#### Rules 
- The chosen integers have to be in the range [1, n].
- Each integer can be chosen at most once.
- The chosen integers should not be in the array `banned`.
- The sum of the chosen integers should not exceed `maxSum`.
- Return the *maximum number* of integers you can choose following the mentioned rules.

## Examples

### Example 1:

- **Input:** `banned` = [1,6,5], `n` = 5, `maxSum` = 6
- **Output:** 2
- **Explanation:** You can choose the integers 2 and 4.
    - 2 and 4 are from the range [1, 5]
    - Neither appears in `banned`
    - Sum = 6 < `maxSum`.

### Example 2:

- **Input:** `banned` = [1,2,3,4,5,6,7], `n` = 8, `maxSum` = 1
- **Output:** 0
- **Explanation:** You cannot choose any integer while following the mentioned conditions.

### Example 3:

- **Input:** `banned` = [11], `n` = 7, `maxSum` = 50
- **Output:** 7
- **Explanation:** You can choose the integers 1, 2, 3, 4, 5, 6, and 7.
    - They are from the range [1, 7]
    - None appear in banned
    - Sum = 28 < `maxSum`.
 

## Constraints:

- 1 <= `banned.length` <= 10^4
- 1 <= `banned[i]`, `n` <= 10^4
- 1 <= `maxSum` <= 10^9

## Approach 

1. **Create `allowed`:**
   - By using set exclusion can rapidly generate a set of `allowed` numbers
   - This is then *sorted* to ensure that the values are in *ascending* order
  
2. **Initialise counters:**
   - Initialise a `current` counter which will track the `current` sum
   - Initialise `num` counter to track the number of integers used

3. **Iterate Over `allowed`:**
   - Can then iterate through `allowed`
   - If `current` < `maxSum`: 
       - Add value to the `current` counter
       - Increment `num` counter by 1
   - If `current` > `maxSum` the `num` counter is returned early to allow for early termination
   - If `current` never exceeds `maxSum`, the `num` counter will be returned after termination of the loop.
  
## Complexity Analysis 

1. **Time:**
   - Removing the `banned` set contributes O(b) time, where b is the length of the `banned` set
   - Iterating through `allowed` contributes O(a)
   - Leetode analysis says that the overall time complexity is O(n), but I am unsure of how and would appreciate an explanation

2. **Space:**
   - Counters are negligible
   - Range of [1, n] contribute O(1)
   - The `banned` set is a temporary variable and does not contribute to overall complexity
   - The difference between `allowed` and `banned` is at most *n* therefore the complexity is O(n)
