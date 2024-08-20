class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        fs = [0, 1]
        if n < 2:
            return fs[n]
        else:
            for n in range(2, n+1):
                fs.append((fs[n-1] + fs[n-2]))
            return fs[-1]
        
