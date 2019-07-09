_author_ = 'jake'
_project_ = 'leetcode'














class Solution:
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        if N == 1:
            return [1]
        evens = self.beautifulArray(N // 2)
        if N % 2 == 0:
            odds = evens[:]
        else:
            odds = self.beautifulArray((N + 1) // 2)
        odds = [(2 * i) - 1 for i in odds]
        evens = [2 * i for i in evens]
        return evens + odds