class Solution(object):
    def rotate(self, nums, k):
        for i in range(k):
            for j in range(len(nums) - 1, 0, -1):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
