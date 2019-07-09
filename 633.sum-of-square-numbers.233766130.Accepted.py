_author_ = 'jake'
_project_ = 'leetcode'





from math import sqrt


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        a = 0
        while a <= sqrt(c / 2):
            b = sqrt(c - a ** 2)
            if int(b) == b:
                return True
            a += 1
        return False