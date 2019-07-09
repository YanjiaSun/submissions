_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            while nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp
            i += 1
        for i, num in enumerate(nums):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1