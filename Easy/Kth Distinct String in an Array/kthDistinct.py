class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        count = 0
        not_unique = set()
        unique = []
        for s in arr:
            if s not in not_unique:
                not_unique.add(s)
                count = arr.count(s)
                if count == 1:
                    unique.append(s)
                    if len(unique) == k:
                        return s
        return ''



