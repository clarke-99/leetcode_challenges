class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        def count_frequencies(word):
            frequency_dict = {}
            word_set = set(word)
            for char in word_set:
                frequency_dict[char] = word.count(char)
            return frequency_dict

        def sort_by_frequency(frequency_dict):
            sorted_chars = sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True)
            return sorted_chars

        def assign_keypresses(sorted_chars, threshold):
            total_presses = 0
            presses = 1
            count = 0
            
            for char, freq in sorted_chars:
                if count == threshold:
                    presses += 1
                    count = 0
                total_presses += freq * presses
                count += 1
            
            return total_presses

        frequency_dict = count_frequencies(word)
        sorted_chars = sort_by_frequency(frequency_dict)
        return assign_keypresses(sorted_chars, 8)
            
        
