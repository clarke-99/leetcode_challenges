class Solution(object):
    def maxCount(self, banned, n, maxSum):
        """
        :type banned: List[int]
        :type n: int
        :type maxSum: int
        :rtype: int
        """
        allowed = sorted(set(range(1,n+1)) - set(banned))

        current = 0
        num = 0

        for x in allowed:
            if current + x <= maxSum:
                current += x 
                num += 1
            else:
                return num
        return num

            


        
