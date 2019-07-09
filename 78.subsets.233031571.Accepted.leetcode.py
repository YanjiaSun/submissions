


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for num in nums:
            for j in range(len(result)):
                result.append(result[j] + [num])
        return result
