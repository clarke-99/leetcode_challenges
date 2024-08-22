class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_element = max(nums)

        if nums.count(max_element) < k:
            return 0
        else:
            subarr_count = 0
            left = 0
            n = len(nums)
            max_count = 0
            for right in range(n):
                if nums[right] == max_element:
                    max_count += 1
                while max_count >= k:
                    subarr_count += n - right 
                    if nums[left] == max_element:
                        max_count -= 1
                    left += 1
                
            return subarr_count



        
