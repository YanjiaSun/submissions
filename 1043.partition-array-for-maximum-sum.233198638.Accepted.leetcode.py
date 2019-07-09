


class Solution(object):
    def maxSumAfterPartitioning(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if not A:
            return 0
        N = len(A)
        dp = [0] * (N + 1)
        for index_i in range(N):
            maxi = 0
            for index_j in range(index_i, index_i - K, -1):
                if index_j >= 0 and index_j < len(A):
                    maxi = max(maxi, A[index_j])
                    dp[index_i + 1] = max(dp[index_i + 1], maxi * (index_i - index_j + 1) + dp[index_j])
            # print index_i, maxi
            # print dp
        return dp[-1]
