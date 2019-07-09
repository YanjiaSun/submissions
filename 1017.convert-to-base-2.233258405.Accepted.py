_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def baseNeg2(self, N):
        """
        :type N: int
        :rtype: str
        """
        if N == 0:
            return "0"
        result = []
        while N != 0:
            N, bit = divmod(N, 2)
            N *= -1
            result.append(str(bit))
        return "".join(reversed(result))
