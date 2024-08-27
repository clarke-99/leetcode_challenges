class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        s,n = list(s), len(s)
        shift = 0

        for i in range(n-1, -1, -1):
            shift += shifts[i]
            new_ord = ord(s[i]) + shift

            while new_ord>122:
                new_ord = ((new_ord - 97) % 26) + 97

            s[i] = chr(new_ord)

        return  ''.join(s)
