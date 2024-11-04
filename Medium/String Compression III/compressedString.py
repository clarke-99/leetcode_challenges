class Solution(object):
    def compressedString(self, word):
        """
        :type word: str
        :rtype: str
        """
        l = len(word)
        left = 0
        prefix_char = []
        comp = ''

        while left < l:
            right = left + 1
            count = 1
            while right < l and word[left] == word[right] and count < 9:
                count += 1
                right += 1
            prefix_char.append((count, word[left]))
            left = right
        
        comp += ''.join([str(count) + char for count, char in prefix_char])

        return comp

        
