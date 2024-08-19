class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        nums.sort()
        # = sorted(nums)
        
        low, high = 0, (nums[-1]- nums[0])
    
        while low<high:
            mid = (low+high)//2
            count = 0
            for i in range(len(nums)):
                j = i +1
                while j < len(nums) and nums[j] - nums[i] <= mid:
                    j += 1
                    
                count += j - i - 1
            if count < k:
                low = mid + 1
            else:
                high = mid 

        return low
    
# class Solution(object):
#     def smallestDistancePair(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """

#         nums = sorted(nums)
#         low, high = 0, nums[-1] - nums[0]  # Set the binary search bounds

#         while low < high:
#             mid = (low + high) // 2
#             count = 0
#             for i in range(len(nums)):
#                 j = i + 1
#                 while j < len(nums) and nums[j] - nums[i] <= mid:
#                     j += 1
#                 count += j - i - 1  # Update the count after finding valid pairs for nums[i]

#             if count < k:
#                 low = mid + 1  # Move to the right half
#             else:
#                 high = mid  # Move to the left half

#         return low  # The k-th smallest distance



nums = [62,100,4]
# print(sorted(nums))
s = Solution()
print(s.smallestDistancePair(nums, 2))