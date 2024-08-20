class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """

        def reduce_string(s):
            stack = []
    
            for char in s:
                if stack and stack[-1].lower() == char.lower() and stack[-1] != char:
                    stack.pop()  
                else:
                    stack.append(char) 
    
            return ''.join(stack)

        return reduce_string(s)

        
