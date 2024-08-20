class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return n
        elif n == (1 or 2):
            return 1
        else:
            ts = [0, 1, 1]

            for n in range(3, n+1):
                tn = ts[n-3] + ts[n-2] + ts[n-1]
                ts.append(tn)
            return ts[-1]
