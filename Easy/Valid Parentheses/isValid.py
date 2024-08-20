class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        matching_bracket = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in matching_bracket.values():  
                stack.append(char)
            elif char in matching_bracket.keys(): 
                if stack and stack[-1] == matching_bracket[char]:
                    stack.pop()
                else:
                    return False

    
        return not stack
                


