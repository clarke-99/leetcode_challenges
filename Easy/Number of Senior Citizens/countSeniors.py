class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        count = [s[11:13] for s in details if int(s[11:13]) > 60]
        return len(count)
        
