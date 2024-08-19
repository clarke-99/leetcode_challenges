class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        count = len(students)
        rot = 0
        while len(students) > 0 and rot < len(students):
            if students[0] == sandwiches[0]:
                count -= 1
                students.pop(0)
                sandwiches.pop(0)
                rot =0
            else:
                students.append(students.pop(0))
                rot += 1
        
        return count
