_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(bits) - 1:
            if bits[i] == 1:
                i += 1
            i += 1
        return i == len(bits) - 1