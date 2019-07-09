_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        min_val = root.val
        self.second_min = float("inf")

        def helper(node):
            if not node:
                return
            if node.val == min_val:
                helper(node.left)
                helper(node.right)
            else:
                self.second_min = min(node.val, self.second_min)
        helper(root)
        return -1 if self.second_min == float("inf") else self.second_min