class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        steps = 0
        num_a = 1
        copied = 0

        def prime_factors(n):
            k = 1
            hcf = n

            if n % 2 ==0:
                return 2
            elif n %3 == 0:
                return 3
            else:
                while 6*k - 1 <= n:
                    high = 6*k+1
                    low = 6*k-1
                    if n % low == 0:
                        hcf = low
                        break
                    if n % high == 0:
                        hcf = high
                        break
                    k += 1

            return hcf
        k = n
        factors = []
        while k > 1:
            factor = prime_factors(k)
            while k % factor ==0:
                factors.append(factor)
                k //= factor

        if n ==0:
            return 0
        else:
            return sum(factors)



            
s = Solution()
print(s.minSteps(18))
                