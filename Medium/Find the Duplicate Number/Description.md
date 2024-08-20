## Challenge 287. Find the Duplicate Number

**Problem:** Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive, return the duplicate number that appears more than once.

## Examples

**Example 1:**

- **Input:** `nums = [1,3,4,2,2]`
- **Output:** `2`
- **Explanation:** The number 2 appears more than once.

**Example 2:**

- **Input:** `nums = [3,1,3,4,2]`
- **Output:** `3`
- **Explanation:** The number 3 appears more than once.

**Example 3:**

- **Input:** `nums = [3,3,3,3,3]`
- **Output:** `3`
- **Explanation:** The number 3 is the only number that repeats.

## Constraints

- `1 <= n <= 10^5`
- `nums.length == n + 1`
- `1 <= nums[i] <= n`
- All the integers in `nums` appear only once except for precisely one integer which appears two or more times.
- Solve the problem without modifying the array `nums`.
- Use only constant extra space.

## Approach

Due to the constraints of the problem, the `Hare and the Tortoise` algorithm is applicable. As there is a single duplicate within the array, it creates a cycle if viewed as a `linked list`, where each value points to the index of the next value.

### Steps

1. **Initialisation**
   - `Tortoise` and `Hare` begin at index 0.
  
2. **Cycle Detection**
   - The `Tortoise` moves a *single* step at a time.
   - The `Hare` moves *two* steps at a time
   - Eventually, the two will meet and this signifies the `beginning` of the cycle

3. **Finder**
   - Initialisation of a `Finder` at index 0.
   - Move the `Finder` and the `Tortoise` (or `Hare`) a *single* step at a time.
   - The `duplicate` is found where the pointers meet

### Notes 

This challenge was particularly difficult due to the concept of using the algorithm in the context of an array, rather than a traditional linked list. Understanding the cycle detection mechanism and adapting it to array indices provided a significant learning experience.

