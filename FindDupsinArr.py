class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = {}
        for num in nums:
            count = 1
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = count

        duplicates = [num for num, count in freq.items() if count > 1]
        return duplicates