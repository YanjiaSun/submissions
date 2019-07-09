_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.tilt = 0

        def helper(node):
            if not node:
                return 0
            left, right = helper(node.left), helper(node.right)
            self.tilt += abs(left - right)
            return node.val + left + right
        helper(root)
        return self.tilt
