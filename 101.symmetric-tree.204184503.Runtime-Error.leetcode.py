class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True

        left = self.isSymmetric(root.left)
        right = self.isSymmetric(root.right)
        return left and right and left.val == right.val