class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        available = {5:0, 10:0, 20:0}

        for bill in bills:
            available[bill] += 1

            if bill == 10:
                if available[5] > 0:
                    available[5] -= 1
                else:
                    return False
            elif bill == 20:
                if available[10] > 0 and available[5]>0:
                    available[10] -= 1
                    available[5] -= 1
                elif available[5]>2:
                    available[5] -= 3
                else:
                    return False

        return True
            

        
