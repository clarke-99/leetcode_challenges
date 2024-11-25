class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # convert immutable string to list
        s = list(s)

        # initialise a set for constant time lookups
        vowels = set(['a', 'e', 'i', 'o', 'u'])

        # initialise pointers
        left, right = 0, len(s) - 1

        while left < right:
            # increment left until vowel is reached
            while s[left].lower() not in vowels and left < right:
                left += 1
            # decrement right until a vowel is reached
            while s[right].lower() not in vowels and right > left:
                right -= 1

            # swap characters and move pointers
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        # return the joined string
        return ''.join(s)
