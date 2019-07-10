










class Solution(object):
    def find132pattern(self, nums):

        two = float("-inf")
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < two:
                return True
            while stack and stack[-1] < nums[i]:
                two = stack.pop()
            stack.append(nums[i])
        return False
