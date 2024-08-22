class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        f = {}
        left = 0
        max_length = 0
        
        for right in range(len(nums)):
            if nums[right] in f:
                f[nums[right]] += 1
                while f[nums[right]] > k:
                    f[nums[left]] -= 1
                    if f[nums[left]] == 0:
                        del f[nums[left]]
                    left += 1

            else:
                f[nums[right]] = 1

            max_length = max(max_length, right - left + 1)


        return max_length


        
