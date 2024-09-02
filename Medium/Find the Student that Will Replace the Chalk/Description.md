## Challenge 1894. Find the Student that Will Replace the Chalk

**Problem:** There are n students in a class numbered from 0 to n - 1. The teacher will give each student a problem starting with the student number 0, then the student number 1, and so on until the teacher reaches the student number n - 1. After that, the teacher will restart the process, starting with the student number 0 again.
You are given a 0-indexed integer array chalk and an integer k. There are initially k pieces of chalk. When the student number i is given a problem to solve, they will use chalk[i] pieces of chalk to solve that problem. However, if the current number of chalk pieces is strictly less than chalk[i], then the student number i will be asked to replace the chalk.
Return the index of the student that will replace the chalk pieces.

## Examples

**Example 1:**

- **Input:** `chalk = [5,1,5]`, `k = 22`
- **Output:** 0
- **Explanation:** The students go in turns as follows:
  - Student number 0 uses 5 chalk, so k = 17.
  - Student number 1 uses 1 chalk, so k = 16.
  - Student number 2 uses 5 chalk, so k = 11.
  - Student number 0 uses 5 chalk, so k = 6.
  - Student number 1 uses 1 chalk, so k = 5.
  - Student number 2 uses 5 chalk, so k = 0.
*Student number 0 does not have enough chalk, so they will have to replace it.*

**Example 2:**

- **Input:** chalk = [3,4,1,2], k = 25
- **Output:** 1
 
## Constraints:

`chalk.length == n`
`1 <= n <= 10^5`
`1 <= chalk[i] <= 10^5`
`1 <= k <= 10^9`

## Approach

1. **Find the Remainder**
   - Using `k % sum(chalk)` you get what is left of `k` after `n` full rotations of `chalk`
   - This massively reduces the time required in comparison to iteration over the array until `k<0`
2. **Find the Index**
   - Now that `k` has been sufficiently reduced, simply iterate over the array until `k` is too small for a student to get any chalk and return
     the index of that student.
