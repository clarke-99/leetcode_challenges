class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        if len(original) != m*n:
            return []
        return [original[x:n+x] for x in range(0,len(original),n)]
