class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapping = {}
        i = 0
        j = 0
        for i in range(len(s)):
            if s[i] not in mapping:
                if t[i] not in mapping.values():
                    mapping[s[i]] = t[i]
                else:
                    return False
            elif mapping[s[i]] != t[i]:
                return False


        return True

        
