class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fast, slow = nums[0], nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        finder = nums[0]
        while finder != slow:
            finder = nums[finder]
            slow = nums[slow]

        return finder
        
