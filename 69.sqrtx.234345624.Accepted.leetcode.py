class Solution:
    def mySqrt(self, x):
        if x == 0:
            return 0
        left, right = 1, x
        while True:
            mid = left + (right - left) / 2
            if mid > x / mid:
                right = mid - 1
            elif mid + 1 > x / (mid + 1):
                return mid
            else:
                left = mid + 1
