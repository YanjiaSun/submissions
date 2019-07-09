_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        sequence = [1]
        for _ in range(n - 1):
            next = []
            for num in sequence:
                if not next or next[-1] != num:
                    next += [1, num]
                else:
                    next[-2] += 1
            sequence = next
        return "".join(map(str, sequence))