class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        result = []
        for _, num in enumerate(nums):
            index = abs(num) - 1
            if nums[index] < 0:
                result.append(index + 1)
            nums[index] *= -1
        return result
