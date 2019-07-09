_author_ = 'jake'
_project_ = 'leetcode'















class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        operations = 0
        while n > 1:
            operations += 1
            if n % 2 == 0:
                n //= 2
            elif n == 3 or (n - 1) % 4 == 0:
                n -= 1
            else:
                n += 1
        return operations