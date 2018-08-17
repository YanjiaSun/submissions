class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        left = max(A, E)
        right = min(C, G)
        low = max(B, F)
        hight = min(H, D)
        area1 = (C - A) * (D - B)
        area2 = (G - E) * (H - F)
        share = (right - left) * (hight - low)
        return area1 + area2 - share
