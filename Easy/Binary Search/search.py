class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sorted_nums = sorted(nums)
        low, high = 0, len(sorted_nums) -1

        while low <= high:
            mid = (low + high) //2
            if sorted_nums[mid] == target:
                return mid
            elif sorted_nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
