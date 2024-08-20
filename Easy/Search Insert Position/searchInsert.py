class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        def binary_search(array, target):
            left, right = 0, len(array) - 1
            
            while left <= right:
                mid = (left + right) // 2
                if array[mid] == target:
                    return mid
                elif array[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return left

        return binary_search(nums, target)
