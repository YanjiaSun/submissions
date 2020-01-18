class Solution(object):
    def rightSideView(self, root):
        queue = [root]
        result = []
        while queue and root:
            for _ in range(len(queue)):
                root = queue.pop(0)
                if root.left:
                    queue += [root.left]
                if root.right:
                    queue += [root.right]
            result += [root.val]
        return result
