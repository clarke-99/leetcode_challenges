class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def transform(s):
            total = 0
            for num in s:
                total += int(num)
            return total, str(total)

        s_num = ''.join([str(ord(char)-96) for char in s])
        while k>=1:
            total, s_num = transform(s_num)
            k -= 1
        return total



        
        
