class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        for nums in nums2:
            nums1.append(nums)

        nums1.sort()
        l = float((len(nums1)+1))/2
        if '.5' in str(l):
            l1 = int(l - 0.5) -1
            l2 = int(l + 0.5) -1
            return float(nums1[l1] + nums1[l2])/2
        else:
            m = nums1[int(l-1)]
        return m

