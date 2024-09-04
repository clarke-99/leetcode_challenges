class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        obstacles = set(map(tuple, obstacles))

        def orient_robot(current_direction, move):
            if move == -2:
                current_direction -= 90
            elif move == -1:
                current_direction += 90
            if current_direction < 0:
                current_direction = 270
            elif current_direction > 270:
                current_direction = 0
            return current_direction
        
        movement = {0: (0, 1), 90:(1, 0), 180:(0, -1), 270:(-1, 0)}

        def move_robot(direct, move, position):
            x, y = movement[direct]
            for n in range(move):
                new_position = (position[0]+x, position[1]+y)
                if new_position in obstacles:
                    break
                position = new_position
            
            return list(position)

        position = [0, 0]
        direct = 0
        max_dist = 0

        for command in commands:
            if command < 0:
                direct = orient_robot(direct, command)
            else:
                position = move_robot(direct, command, position)
            dist = position[0]**2 + position[1]**2
            max_dist = max(max_dist, dist)


        return max_dist



            



        
