_author_ = 'jake'
_project_ = 'leetcode'









from collections import defaultdict


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def dist_squared(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        boomerangs = 0
        for middle in points:
            distances = defaultdict(int)
            for i, other in enumerate(points):
                distances[dist_squared(middle, other)] += 1
            for count in distances.values():
                boomerangs += count * (count - 1)
        return boomerangs