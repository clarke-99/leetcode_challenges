class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        missing = None
        s = sorted(nums)
        i = 0
        # return s
        while i < len(s):
            if 1 not in s:
                return 1
            if i + 1 < len(s):
                j = i +1
                if s[i] == s[j]:
                    pass
                elif s[i] > -1 and (s[i] + 1 != s[j]):
                    return s[i] + 1
                
            
            i += 1
    
        return s[-1] +1


        
        
