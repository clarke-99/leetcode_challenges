class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        score = 0
        s = s.strip()
        length = len(s)


        for i in range(length - 1):
            val_1 = ord(s[i])
            val_2= ord(s[i+1])
            score += abs(val_1 - val_2)
        return score
