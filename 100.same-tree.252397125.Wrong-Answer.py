class Solution(object):
    def isSameTree(self, p, q):
        try:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        except:
            return False
        return False