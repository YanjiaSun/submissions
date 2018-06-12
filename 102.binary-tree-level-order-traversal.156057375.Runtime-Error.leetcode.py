class Solution(object):
    def levelOrder(self, root):
        queue = [root]
        result = []

        while queue:
            current = []
            size = len(queue)

            for _ in range(size):
                root = queue.pop(0)
                current.append(root.val)

                if root.left:
                    queue.append(root.left)

                if root.right:
                    queue.append(root.right)
            result.append(current)
        return result
