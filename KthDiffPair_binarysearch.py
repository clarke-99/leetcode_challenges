class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()  
        
        def count_pairs_with_max_distance(max_dist):
            count = 0
            j = 0
            for i in range(len(nums)):
                while j < len(nums) and nums[j] - nums[i] <= max_dist:
                    j += 1
                count += j - i - 1  
            return count
        
        low, high = 0, nums[-1] - nums[0]  

        while low < high:
            mid = (low + high) // 2
            if count_pairs_with_max_distance(mid) < k:
                low = mid + 1
            else:
                high = mid
        
        return low


