class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        max_depth = 0
        for char in s:
            if char == "(":
                count += 1
            elif char == ')':
                count -= 1
            if count > max_depth:
                max_depth = count

        return max_depth
        