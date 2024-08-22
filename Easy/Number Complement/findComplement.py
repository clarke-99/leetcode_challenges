class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binary = str(bin(num))
        com = ['1' if n == '0' else '0' for n in binary[2:]]
        return int(''.join(com), 2)


class Solution2(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binary = bin(num)
        com = ['1' if n == '0' else '0' for n in binary[2:]]
        return int(''.join(com), 2)

class Solution3(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binary = str(bin(num))
        # com = ['1' if n == '0' else '0' for n in binary[2:]]
        return int(''.join(['1' if n == '0' else '0' for n in binary[2:]]), 2)

        

        
