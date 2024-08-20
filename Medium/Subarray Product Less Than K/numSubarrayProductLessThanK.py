class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0  # No product of subarray elements can be less than 1 if k <= 1

        count = 0
        product = 1
        left = 0
        
        for right in range(len(nums)):
            product *= nums[right]
            
            while product >= k and left <= right:
                product /= nums[left]
                left += 1
            
            count += (right - left + 1)
        
        return count
