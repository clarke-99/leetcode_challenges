## Challenge 874. Walking Robot Simulation

**Problem:** A robot on an *infinite* XY-plane starts at point (0, 0) facing north. The robot can receive a sequence of these three possible 
types of `commands`:

- `-2:` Turn left 90 degrees.
- `-1:` Turn right 90 degrees.
- `1 <= k <= 9:` Move forward k units, one unit at a time.

Some of the grid squares are `obstacles`. The `ith` obstacle is at grid point `obstacles[i] = (xi, yi)`. If the robot runs into an `obstacle`,
then it will **stay** in its current location and move on to the **next command**.

Return the *maximum* Euclidean distance the robot ever gets from the origin squared (i.e. if the distance is 5, return 25).

**Notes:**

- North means `+Y` direction.
- East means `+X` direction.
- South means `-Y` direction.
- West means `-X` direction.
- There can be `obstacle` in `[0,0]`.
 
## Examples

**Example 1:**

- **Input:** `commands = [4,-1,3]`, `obstacles = []`
- **Output:** 25
- **Explanation:** The robot starts at (0, 0):
  1. Move north 4 units to (0, 4).
  2. Turn right.
  3. Move east 3 units to (3, 4).
  4. The furthest point the robot ever gets from the origin is (3, 4), which squared is 32 + 42 = 25 units away.

**Example 2:**

- **Input:** `commands = [4,-1,4,-2,4]`, `obstacles = [[2,4]]`
- **Output:** 65
- **Explanation:** The robot starts at (0, 0):
  1. Move north 4 units to (0, 4).
  2. Turn right.
  3. Move east 1 unit and get blocked by the obstacle at (2, 4), robot is at (1, 4).
  4. Turn left.
  5. Move north 4 units to (1, 8).
  6. The furthest point the robot ever gets from the origin is (1, 8), which squared is 12 + 82 = 65 units away.
  
**Example 3:**

- **Input:** `commands = [6,-1,-1,6]`, `obstacles = []`
- **Output:** 36
- **Explanation:** The robot starts at (0, 0):
  1. Move north 6 units to (0, 6).
  2. Turn right.
  3. Turn right.
  4. Move south 6 units to (0, 0).
  5. The furthest point the robot ever gets from the origin is (0, 6), which squared is 62 = 36 units away.
 
## Constraints:

- `1 <= commands.length <= 10^4`
- `commands[i] is either -2, -1, or an integer in the range [1, 9].`
- `0 <= obstacles.length <= 10^4`
- `-3 * 10^4 <= xi, yi <= 3 * 10^4`
- The answer is guaranteed to be less than 2<sup>31</sup>.

## Approach

1. **Convert to Set**
   - Convert the list of `obstacles` into a set to ensure efficient `O(1)` average-time complexity for lookups.
   - This significantly speeds up the check for whether a `position` contains an `obstacle`.
  
2. **Helper Functions: `orient_robot` and `move_robot`**
   - Defining these functions modularises the code, making it more manageable, by separating the concerns of orientation adjustment and movement.
     1. `orient_robot(current_direction, move)`
         - Adjust the robot's direction based on the `turn command`.
         - Updates `current_direction` by adding or subtracting 90 degrees and ensures it stays within the range of 0 to 270 degrees.
         This is managed using conditional checks rather than modulo operations for efficiency.
     2. `move_robot(direct, move, position)`
        - Updates the robot's position step-by-step in the current direction.
        - If an `obstacle` is encountered, the loop breaks and the robot’s `position` is returned.
        
3. **Update `max_dist`**
   - After each `command` calculate the `Euclidean` distance
   - If the current distance is greater than `max_dist` update `max_dist`

 ## Complexity 

 1. **Time Complexity:** O(n+k)
    - n represents the number of commands. 
    - k represents the number of obstacles

 2. **Space Complexity:** O(k)
    - k represents number of obstacles stored within the set.
   
 ### Notes 

 I think this could be improved by checking if there are any obstacles in the range that the robot would move first and then setting the robot to that position, rather than increasing incrementally. 
