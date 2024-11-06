class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 3:
            return s

        chars = [s[0], s[1]]

        for i in range(2, len(s)):
            if not (s[i] == s[i-1] == s[i-2]):
                chars.append(s[i])
        
        return ''.join(chars)
        
