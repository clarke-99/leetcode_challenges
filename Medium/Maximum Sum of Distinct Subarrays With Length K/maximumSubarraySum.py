class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        current_sum, max_sum = 0, 0
        window = set()
        start = 0

        for i in range(len(nums)):
            while nums[i] in window:
                window.remove(nums[start])
                current_sum -= nums[start]
                start += 1

            window.add(nums[i])
            current_sum += nums[i]
            
            if i - start + 1 == k:
                max_sum = max(max_sum, current_sum)
                window.remove(nums[start])
                current_sum -= nums[start]
                start += 1

        return max_sum 
