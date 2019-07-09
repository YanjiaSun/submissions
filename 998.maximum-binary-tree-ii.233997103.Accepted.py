_author_ = 'jake'
_project_ = 'leetcode'





















class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        new_root = TreeNode(float("inf"))
        new_root.right = root
        node = new_root
        while node.right and node.right.val > val:
            node = node.right
        right_subtree = node.right
        node.right = TreeNode(val)
        node.right.left = right_subtree
        return new_root.right
