class Solution(object):
    def buildTree(self, inorder, postorder):
        if not inorder:
            return None
        inorder_index = inorder.index(postorder.pop())
        root = TreeNode(inorder[inorder_index])
        root.right = self.buildTree(inorder[inorder_index + 1:], postorder)
        root.left = self.buildTree(inorder[:inorder_index], postorder)
        return root
