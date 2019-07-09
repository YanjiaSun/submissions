_author_ = 'jake'
_project_ = 'leetcode'


















class Solution(object):
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        heights = [float("inf")] + heights + [float("inf")]
        K += 1
        while V > 0:
            V -= 1
            i = K
            lowest, lowest_i = heights[K], K
            while heights[i - 1] <= lowest:
                i -= 1
                if heights[i] < lowest:
                    lowest, lowest_i = heights[i], i
            if lowest < heights[K]:
                heights[lowest_i] += 1
                continue
            i = K
            lowest, lowest_i = heights[K], K
            while heights[i + 1] <= lowest:
                i += 1
                if heights[i] < lowest:
                    lowest, lowest_i = heights[i], i
            if lowest < heights[K]:
                heights[lowest_i] += 1
            else:
                heights[K] += 1
        return heights[1:-1]