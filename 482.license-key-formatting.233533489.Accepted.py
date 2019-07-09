_author_ = 'jake'
_project_ = 'leetcode'
















class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        key = S.replace("-", "").upper()
        formatted = []
        i = len(key) - K
        while i >= 0:
            formatted.append(key[i:i + K])
            i -= K
        if i != -K:
            formatted.append(key[:i + K])
        return "-".join(formatted[::-1])
        return "-".join(formatted)