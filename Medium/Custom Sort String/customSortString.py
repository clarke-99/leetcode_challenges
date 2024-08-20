class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        new_s = ''
        for char in order:
            count = s.count(char)
            if count > 0:
                new_s += char*count
        extras = ''
        for x in s:
            if x not in new_s:
                extras += x
        return new_s+extras

        


        
