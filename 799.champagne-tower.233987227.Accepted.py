_author_ = 'jake'
_project_ = 'leetcode'















class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        glasses = [poured]
        for row in range(query_row):
            new_glasses = [0 for _ in range(len(glasses) + 1)]
            for i, glass in enumerate(glasses):
                pour = max(glass - 1, 0) / 2.0
                new_glasses[i] += pour
                new_glasses[i + 1] += pour
            glasses = new_glasses
        return min(glasses[query_glass], 1)