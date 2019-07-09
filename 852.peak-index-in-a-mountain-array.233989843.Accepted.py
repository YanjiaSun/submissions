_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def peakIndexInMountainArray(self, nums):
        """
        :type A: List[int]
        :rtype: int
        """
        left, right = 1, len(nums) - 2
        while left < right:
            mid = (left + right) // 2
            if nums[mid + 1] < nums[mid]:
                right = mid
            else:
                left = mid + 1
        return left