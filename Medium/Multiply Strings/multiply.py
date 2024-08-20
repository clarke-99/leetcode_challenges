class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        def rev_string(num):
            num = num[::-1]
            return num
        
        num1, num2 = rev_string(num1), rev_string(num2)

        def get_num(num):
            values = [str(i) for i in range(0, 10)]
            val = 0
            for i, char in enumerate(num):
                val += values.index(char) * (10**i)
            return val

        return str(get_num(num1)*get_num(num2))

            
