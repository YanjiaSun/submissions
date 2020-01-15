from itertools import combinations
class Solution1:
    def triangleNumber(self, nums):
        def is_triangle(*args):
            a, b, c = args
            if a + b > c > 0 and a + c > b > 0 and b + c > a > 0:
                return 1
            return 0
        return sum([is_triangle(*com) for com in combinations(nums, 3)])
class Solution2:
    def triangleNumber(self, nums):
        nums.sort()
        count = 0
        for i in range(2, len(nums)):
            l, r = 0, i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    count += r - l
                    r -= 1
                else:
                    l += 1
        return count
    t = Solution1()
