_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n <= 2:
            return n
        stairs, prev = 2, 1
        for _ in range(3, n + 1):
            stairs, prev = stairs + prev, stairs
        return stairs
