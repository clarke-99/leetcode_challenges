## Challenge 1700: Number of Students Unable to Eat Lunch

**Problem:**
In the school cafeteria, there are two types of sandwiches: circular (0) and square (1). Students in a queue have preferences for these sandwiches. The number of sandwiches matches the number of students, and they are stacked such that the topmost sandwich is served first. The process to serve sandwiches is as follows:

1. If the student at the front of the queue prefers the sandwich on the top of the stack, they take the sandwich and leave the queue.
2. If the student does not prefer the sandwich, they go to the end of the queue, and the sandwich remains on top of the stack.

This process continues until no student in the queue wants the top sandwich, at which point the students remaining in the queue are unable to eat.

Return the number of students who are unable to eat.

## Examples:

 **Example 1:**
 - **Input:** `students = [1, 1, 0, 0]`, `sandwiches = [0, 1, 0, 1]`
 - **Output:** `0`
 - **Explanation:** All students eventually get the sandwich they prefer, so no student is unable to eat.

 **Example 2:**
 - **Input:** `students = [1, 1, 1, 0, 0, 1]`, `sandwiches = [1, 0, 0, 0, 1, 1]`
 - **Output:** `3`
 - **Explanation:** After serving the sandwiches, 3 students cannot get the sandwich they prefer.

## Constraints:

- 1 <= `students.length`, `sandwiches.length` <= 100
- `students.length` == `sandwiches.length`
- `sandwiches[i]` and `students[i]` are either 0 or 1.

