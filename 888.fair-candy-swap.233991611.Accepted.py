_author_ = 'jake'
_project_ = 'leetcode'
















class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        A_candy, B_candy = sum(A), sum(B)
        difference = (A_candy - B_candy) // 2
        B_set = set(B)
        for a in A:
            if a - difference in B_set:
                return [a, a - difference]
        return []