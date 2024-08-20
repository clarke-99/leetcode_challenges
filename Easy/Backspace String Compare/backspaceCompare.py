class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def remove_chars(string):
            final = list(string)
            i = 0
            while i < len(final):
                if final[i] == '#':
                    if i > 0:
                        final.pop(i)
                        final.pop(i-1)
                        i -= 1
                    else:
                        final.pop(i)
                else:
                    i+=1
            return final

        return remove_chars(s) == remove_chars(t)
                    
                

        
