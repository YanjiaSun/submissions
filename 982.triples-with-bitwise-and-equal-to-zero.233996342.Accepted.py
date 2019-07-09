_author_ = 'jake'
_project_ = 'leetcode'











from collections import defaultdict


class Solution:
    def countTriplets(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        pairs = defaultdict(int)
        for num1 in A:
            for num2 in A:
                pairs[num1 & num2] += 1
        result = 0
        for pair, count in pairs.items():
            for num3 in A:
                if pair & num3 == 0:
                    result += count
        return result