_author_ = 'jake'
_project_ = 'leetcode'















class Solution(object):
    def atMostNGivenDigitSet(self, D, N):
        """
        :type D: List[str]
        :type N: int
        :rtype: int
        """
        S = str(N)
        K = len(S)
        dp = [0] * K + [1]
        for i in range(K - 1, -1, -1):
            for d in D:
                if d < S[i]:
                    dp[i] += len(D) ** (K - i - 1)
                elif d == S[i]:
                    dp[i] += dp[i + 1]
        return dp[0] + sum(len(D) ** i for i in range(1, K))