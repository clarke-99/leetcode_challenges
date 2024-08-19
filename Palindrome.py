# Palindrome
class Solution():
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        puncs = [',', ';', ':', '!', '?', '.', '/', '\'', ' ', '']
        for punc in puncs:
            s = s.replace(punc, '')
            
        s = s.lower()
        reverse = ''.join(reversed(s))
        print(s, reverse)

        return s == reverse


s = "A man, a plan, a canal: Panama"  
sol = Solution()

sol.isPalindrome(s)








